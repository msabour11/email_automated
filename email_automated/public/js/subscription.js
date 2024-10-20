frappe.ui.form.on("Subscription", {
  party(frm) {
    // if (frm.doc.party_type == "Customer" && frm.doc.party) {

    // }          frm.clear_table("custom_email");

    frm.clear_table("custom_email");
    console.log("the table is cleared");

    if (frm.doc.party) {
      frm.fields_dict["custom_email"].grid.get_field("contact").get_query =
        function (doc) {
          return {
            query: "email_automated.utils.get_contact.get_contacts_by_link",
            filters: {
              link_doctype: "Customer",
              link_name: doc.party,
            },
          };
        };
    }

    frm.refresh_field("custom_email");
  },
});

frappe.ui.form.on("Subscription Email", {
  contact: function (frm, cdt, cdn) {
    var row = locals[cdt][cdn];

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
