from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Location Setting"),
			"items": [
				{
					"type": "doctype",
					"name": "Location List",
				},
				{
					"type": "doctype",
					"name": "User And Location Setting",
				}
				
			]
		},
		{
			"label": _("Invoice"),
			"items": [
				{
					"type": "doctype",
					"name": "Sales Invoice",
					"label": _("Cash Invoice"),
					"route" : "Form/Sales Invoice/New Sales Invoice 1",
					"route_options": {
						"invoice_type": "Cash Invoice"
					}
				},
				{
					"type": "doctype",
					"name": "Sales Invoice",
					"label": _("Credit Invoice"),
					"route" : "Form/Sales Invoice/New Sales Invoice 1",
					"route_options": {
						"invoice_type": "Credit Invoice"
					}
				}
			]
		}
]
