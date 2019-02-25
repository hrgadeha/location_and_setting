# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "location_and_settings"
app_title = "Location And Settings"
app_publisher = "Hardik Gadesha"
app_description = "App to map location and warehouse with user"
app_icon = "octicon octicon-file-directory"
app_color = "pink"
app_email = "hardikgadesha@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/location_and_settings/css/location_and_settings.css"
# app_include_js = "/assets/location_and_settings/js/location_and_settings.js"

# include js, css files in header of web template
# web_include_css = "/assets/location_and_settings/css/location_and_settings.css"
# web_include_js = "/assets/location_and_settings/js/location_and_settings.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "location_and_settings.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "location_and_settings.install.before_install"
# after_install = "location_and_settings.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "location_and_settings.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"location_and_settings.tasks.all"
# 	],
# 	"daily": [
# 		"location_and_settings.tasks.daily"
# 	],
# 	"hourly": [
# 		"location_and_settings.tasks.hourly"
# 	],
# 	"weekly": [
# 		"location_and_settings.tasks.weekly"
# 	]
# 	"monthly": [
# 		"location_and_settings.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "location_and_settings.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "location_and_settings.event.get_events"
# }

