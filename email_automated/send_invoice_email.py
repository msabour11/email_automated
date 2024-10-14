


import frappe
from frappe.core.doctype.communication.email import make

def send_invoice_submission_email(doc, method):
    """
    Sends an email to the customer upon submission of the Sales Invoice.
    """
    # Send email to customer if custom_customer_email exists
    customer_email = doc.get('custom_customer_email')
    if customer_email:
        send_email(doc, customer_email)
    else:
        frappe.msgprint("No email Found continue")
        return

def send_email(invoice, recipient):
    """
    Helper function to send an email notification to the customer.
    """
    # Email subject and message content
    subject = f"Sales Invoice {invoice.name} Submitted"
    message = f"""
    Dear Customer,<br><br>
    The Sales Invoice <b>{invoice.name}</b> has been submitted.<br>
    Total Amount: {invoice.grand_total}<br>
    Due Date: {invoice.due_date}<br>
    <a href="{frappe.utils.get_url_to_form('Sales Invoice', invoice.name)}">View Invoice</a><br><br>
    Thank you!
    """
    
    # Send the email using Frappe's make function
    make(
        recipients=[recipient],
        subject=subject,
        content=message,
        doctype="Sales Invoice",
        name=invoice.name,
        send_email=True
    )
    frappe.msgprint(f"Email sent to customer at {recipient}")