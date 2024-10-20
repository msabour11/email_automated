from erpnext.accounts.doctype.subscription.subscription import Subscription
import frappe
from frappe.utils import add_days, cint
from datetime import date
from frappe.model.document import Document
from erpnext.accounts.party import get_party_account_currency
from erpnext import get_default_company, get_default_cost_center
from erpnext.accounts.doctype.accounting_dimension.accounting_dimension import (
	get_accounting_dimensions,
)
from erpnext.accounts.doctype.subscription_plan.subscription_plan import get_plan_rate
from frappe.utils import validate_email_address






DateTimeLikeObject = str | date


class CustomSubscription(Subscription):
	def create_invoice(
		self,
		from_date: DateTimeLikeObject | None = None,
		to_date: DateTimeLikeObject | None = None,
		posting_date: DateTimeLikeObject | None = None,
	) -> Document:
		"""
		Creates an `Invoice`, submits it, and returns it.
		Appends email details from the Subscription's 'email' child table
		to the invoice's emails child table.
		"""
		company = self.get("company") or get_default_company()
		if not company:
			frappe.throw(
				_(
					"Company is mandatory for generating an invoice. Please set a default company in Global Defaults."
				)
			)

		invoice = frappe.new_doc(self.invoice_document_type)
		invoice.company = company
		invoice.set_posting_time = 1

		# Determine posting date logic
		if self.generate_invoice_at == "Beginning of the current subscription period":
			invoice.posting_date = self.current_invoice_start
		elif self.generate_invoice_at == "Days before the current subscription period":
			invoice.posting_date = posting_date or self.current_invoice_start
		else:
			invoice.posting_date = self.current_invoice_end

		invoice.cost_center = self.cost_center

		# Set customer/supplier
		if self.invoice_document_type == "Sales Invoice":
			invoice.customer = self.party
		else:
			invoice.supplier = self.party
			if frappe.db.get_value("Supplier", self.party, "tax_withholding_category"):
				invoice.apply_tds = 1

		# Set currency for party
		invoice.currency = get_party_account_currency(self.party_type, self.party, self.company)

		# Add dimensions to invoice
		accounting_dimensions = get_accounting_dimensions()
		for dimension in accounting_dimensions:
			if self.get(dimension):
				invoice.update({dimension: self.get(dimension)})

		# Fetch items
		items_list = self.get_items_from_plans(self.plans, is_prorate())
		for item in items_list:
			item["cost_center"] = self.cost_center
			invoice.append("items", item)

		# Taxes
		tax_template = ""
		if self.invoice_document_type == "Sales Invoice" and self.sales_tax_template:
			tax_template = self.sales_tax_template
		elif self.invoice_document_type == "Purchase Invoice" and self.purchase_tax_template:
			tax_template = self.purchase_tax_template

		if tax_template:
			invoice.taxes_and_charges = tax_template
			invoice.set_taxes()

		# Payment schedule
		if self.days_until_due:
			invoice.append(
				"payment_schedule",
				{
					"due_date": add_days(invoice.posting_date, cint(self.days_until_due)),
					"invoice_portion": 100,
				},
			)

		# Apply email template
		if self.get("custom_template") and self.get("custom_email"):
			invoice.custom_email_template = self.custom_template
			for email_row in self.get("custom_email"): 
				if email_row.contact and email_row.email:
					if validate_email_address(email_row.email):
						invoice.append("custom_emails", {
							"contact": email_row.contact,  	
							"email": email_row.email  	
						})

		# Append email and contact details from Subscription's 'email' child table
			# if self.get("custom_email"):
			# 	for email_row in self.get("custom_email"): 
			# 		if email_row.contact and email_row.email:
			# 			if validate_email_address(email_row.email):
			# 			# Assuming the child table field is named 'email'
			# 				invoice.append("custom_emails", {
			# 					"contact": email_row.contact,  # Assuming child table has 'contact' field
			# 					"email": email_row.email  # Assuming child table has 'email' field
			# 				})


      

		# Discounts
		if self.is_trialling():
			invoice.additional_discount_percentage = 100
		else:
			if self.additional_discount_percentage:
				invoice.additional_discount_percentage = self.additional_discount_percentage

			if self.additional_discount_amount:
				invoice.discount_amount = self.additional_discount_amount

			if self.additional_discount_percentage or self.additional_discount_amount:
				discount_on = self.apply_additional_discount
				invoice.apply_discount_on = discount_on if discount_on else "Grand Total"

		# Subscription period
		invoice.subscription = self.name
		invoice.from_date = from_date or self.current_invoice_start
		invoice.to_date = to_date or self.current_invoice_end

		invoice.flags.ignore_mandatory = True

		invoice.set_missing_values()
		invoice.save()

		# Submit the invoice if necessary
		if self.submit_invoice:
			invoice.submit()

		return invoice













def is_prorate() -> int:
	return cint(frappe.db.get_single_value("Subscription Settings", "prorate"))