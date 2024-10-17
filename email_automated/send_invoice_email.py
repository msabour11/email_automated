


import frappe
from frappe.core.doctype.communication.email import make

def send_invoice_submission_email(doc, method):
    """
    Sends an email to the customer upon submission of the Sales Invoice.
    """
    # Send email to customer if custom_customer_email exists
    # customer_email = doc.get('custom_customer_email')
    customer_contact= doc.get("custom_contact")
    custom_email_template= doc.get("custom_email_template")
    doc_args = doc.as_dict()
    emails_table= doc.get("custom_emails")

    if emails_table:
        recipients=[row.email for row in emails_table if row.email]
    else:
        frappe.msgprint("No emails found in the table")
        return



    if recipients:
        send_email(doc, recipients, custom_email_template, doc_args=doc_args)
    else:
        frappe.msgprint("No valid email addresses found")



    




    


    # if customer_email and custom_email_template:
    #     send_email(doc, customer_email,custom_email_template,doc_args=doc_args)
    # else:
    #     frappe.msgprint("No email or tempalte  Found ")
    #     return
    

def send_email(invoice, recipients,template,doc_args):
    """
    Helper function to send an email notification to the customer.

    """


    if template:
        email_template = frappe.get_doc("Email Template", template)

    

    message = frappe.render_template(email_template.response,doc_args)
    subject = frappe.render_template(email_template.subject,doc_args)
    sender = frappe.session.user  and frappe.session.user or None

    # Send the email using make function
    make(
        recipients=recipients,
        subject=subject,
        content=message,
        doctype="Sales Invoice",
        name=invoice.name,
        send_email=True,
        sender=sender
    )
    frappe.msgprint(f"Email sent to customer at {recipients}")