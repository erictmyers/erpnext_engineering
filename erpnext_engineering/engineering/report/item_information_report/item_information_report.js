// Copyright (c) 2016, Ability Engineering and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Item Information Report"] = {
	"filters": [
		{
			"fieldname": "item_code",
			"label": __("Item"),
			"fieldtype": "Link",
			"width": "80",
			"options": "Item",
			"get_query": function() {
				return {
					query: "erpnext.controllers.queries.item_query",
				};
			}
		}
	]
};
