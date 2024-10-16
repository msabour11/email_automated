app_name = "email_automated"
app_title = "Email Automated"
app_publisher = "mohamed sabour"
app_description = "Email automated feature"
app_email = "mohamedabdelsabour269@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "email_automated",
# 		"logo": "/assets/email_automated/logo.png",
# 		"title": "Email Automated",
# 		"route": "/email_automated",
# 		"has_permission": "email_automated.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/email_automated/css/email_automated.css"
# app_include_js = "/assets/email_automated/js/email_automated.js"

# include js, css files in header of web template
# web_include_css = "/assets/email_automated/css/email_automated.css"
# web_include_js = "/assets/email_automated/js/email_automated.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "email_automated/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {"Sales Invoice" : "public/js/sales_invoice.js"}

# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "email_automated/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "email_automated.utils.jinja_methods",
# 	"filters": "email_automated.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "email_automated.install.before_install"
# after_install = "email_automated.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "email_automated.uninstall.before_uninstall"
# after_uninstall = "email_automated.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "email_automated.utils.before_app_install"
# after_app_install = "email_automated.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "email_automated.utils.before_app_uninstall"
# after_app_uninstall = "email_automated.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "email_automated.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

doc_events = {
    "Sales Invoice": {
        "on_submit": "email_automated.send_invoice_email.send_invoice_submission_email"
    }
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"email_automated.tasks.all"
# 	],
# 	"daily": [
# 		"email_automated.tasks.daily"
# 	],
# 	"hourly": [
# 		"email_automated.tasks.hourly"
# 	],
# 	"weekly": [
# 		"email_automated.tasks.weekly"
# 	],
# 	"monthly": [
# 		"email_automated.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "email_automated.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "email_automated.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "email_automated.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["email_automated.utils.before_request"]
# after_request = ["email_automated.utils.after_request"]

# Job Events
# ----------
# before_job = ["email_automated.utils.before_job"]
# after_job = ["email_automated.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"email_automated.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

