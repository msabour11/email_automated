// frappe.ui.form.on('Sales Invoice', {
//     customer: function(frm) {
//         if (frm.doc.customer) {
//             frappe.call({
//                 method: "frappe.client.get_list",
//                 args: {
//                     doctype: "Contact",
//                     filters: [
//                         ["Dynamic Link", "link_name", "=", frm.doc.customer],
//                         ["Dynamic Link", "link_doctype", "=", "Customer"]
//                     ],

//                 },
//                 callback: function(r) {
//                     if (r.message) {
//                         console.log(r.message);
//                     }
//                 }
//             });
//         }
//     }
// });

frappe.ui.form.on("Sales Invoice", {
  refresh(frm) {
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
  },

  //  custom_email_template(frm){

  //      frappe.call({
  //          method:"frappe.client.get",
  //          args:{
  //              doctype:"Email Template",
  //              name:frm.doc.custom_email_template
  //          },
  //          callback:function(r){

  //              console.log("email template is",r.message)
  //          }
  //      })

  //     },

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

  custom_contact(frm) {
    if (frm.doc.customer && frm.doc.custom_contact) {
      frappe.call({
        method: "frappe.client.get",
        args: {
          doctype: "Contact",
          name: frm.doc.custom_contact,
        },
        callback: function (r) {
          let email = r.message.email_id;
          if (email) {
            console.log("the contact is ", email);

            frm.set_value("custom_customer_email", email);
          }
        },
      });
    } else frm.set_value("custom_customer_email", "");
  },

  before_save(frm) {
    var email = frm.doc.custom_customer_email;
    if (!email) {
      frappe.call({
        method: "frappe.client.get",
        args: {
          doctype: "Customer",
          name: frm.doc.customer,
        },
        callback: function (r) {
          if (r.message) {
            let customer_primary_contact = r.message.email_id;
            if (customer_primary_contact) {
              frm.set_value("custom_customer_email", customer_primary_contact);
            }
          }
        },
      });
    }
  },
});
