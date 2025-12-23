# Copyright (c) 2025, Pranay and contributors
# For license information, please see license.txt

from unittest.loader import VALID_MODULE_NAME

import frappe
from frappe.model.delete_doc import DocStatus
from frappe.model.document import Document


class LibraryTransaction(Document):
	def before_submit(self):
		pass

	def validate_membership(self):
		valid_membership = frappe.db.exists(
			"Library Membership",
			{
				"library_member": self.library_member,
				"docstatus": DocStatus.submitted(),
				"from_date": ("<", self.date),
				"to_date": (">", self.date),
			},
		)
		if not valid_membership:
			frappe.throw("The member doesn not have a valid membership")
