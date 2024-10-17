frappe.ui.form.on("Sales Invoice", {
  setup(frm) {
    // filters commissar based on company name
    frm.set_query("custom_contact", function (doc) {
      return {
        query: "email_automated.utils.get_contact.get_contacts_by_link",
        filters: {
          link_doctype: "Customer",
          link_name: doc.customer,
        },
      };
    });

    ////////////////////
    /// filter contacts in emails table based on customer

    frm.fields_dict["custom_emails"].grid.get_field("contact").get_query =
      function (doc) {
        return {
          query: "email_automated.utils.get_contact.get_contacts_by_link",
          filters: {
            link_doctype: "Customer",
            link_name: doc.customer,
          },
        };
      };
  },



  //     customer: function(frm) {
  //     if (frm.doc.customer) {

  //     frappe.call({
  //     method: "frappe.client.get_list",
  //     args: {
  //       doctype: "Contact",
  //       filters: [
  //         ["Dynamic Link", "link_doctype", "=", "Customer"],
  //         ["Dynamic Link", "link_name", "=", frm.doc.customer],
  //       ],
  //       fields: ["name", "email_id", "phone"],
  //     },
  //     callback: function (r) {
  //       if (r.message)
  //       {

  //           console.log("hi",r.message)
  //       }
  //     },
  //   });

  //         }
  //     },

  // custom_contact(frm) {
  //   if (frm.doc.customer && frm.doc.custom_contact) {
  //     frappe.call({
  //       method: "frappe.client.get",
  //       args: {
  //         doctype: "Contact",
  //         name: frm.doc.custom_contact,
  //       },
  //       callback: function (r) {
  //         let email = r.message.email_id;
  //         if (email) {
  //           console.log("the contact is ", email);

  //           frm.set_value("custom_customer_email", email);
  //         }
  //       },
  //     });
  //   } else frm.set_value("custom_customer_email", "");
  // },

  // before_save(frm) {
  //   var email = frm.doc.custom_customer_email;
  //   if (!email) {
  //     frappe.call({
  //       method: "frappe.client.get",
  //       args: {
  //         doctype: "Customer",
  //         name: frm.doc.customer,
  //       },
  //       callback: function (r) {
  //         if (r.message) {
  //           let customer_primary_contact = r.message.email_id;
  //           if (customer_primary_contact) {
  //             frm.set_value("custom_customer_email", customer_primary_contact);
  //           }
  //         }
  //       },
  //     });
  //   }
  // },
});

frappe.ui.form.on("Email Contact", {
  contact: function (frm, cdt, cdn) {
    var row = locals[cdt][cdn];
    frappe.msgprint("hdlllllllllll");

    if (row.contact) {
      frappe.call({
        method: "frappe.client.get",
        args: {
          doctype: "Contact",
          name: row.contact,
        },
        callback: function (r) {
          let contact_email = r.message.email_id;
          if (contact_email) {
            console.log("the contact from child is ", contact_email);

            frappe.model.set_value(cdt, cdn, "email", contact_email);
          }
        },
      });
    } else frappe.model.set_value(cdn, cdt, "email", "");
  },
});
