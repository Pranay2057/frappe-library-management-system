// Copyright (c) 2025, Pranay and contributors
// For license information, please see license.txt

frappe.ui.form.on("Library Membership", {
	refresh(frm) {
		frm.dashboard.add_comment("🟢 CUSTOM APP LOADED - Build Working!", "green", true);
	},
});
