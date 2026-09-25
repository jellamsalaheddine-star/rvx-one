"""Roles + RVX Ticket workflow. Idempotent; re-applied on every `bench migrate`
so the workflow in the database always matches the definition below."""

import frappe

from rvx_one.security import ADMIN_ROLE, CLIENT_ROLE, QUALITY_ROLE, TECHNICIAN_ROLE

WORKFLOW_NAME = "RVX Ticket Workflow"
DOCTYPE = "RVX Ticket"

ROLES = [ADMIN_ROLE, TECHNICIAN_ROLE, QUALITY_ROLE, CLIENT_ROLE]

# (state, docstatus, role allowed to edit in that state, badge style)
STATES = [
	("En attente", 0, ADMIN_ROLE, "Warning"),
	("Assigné", 0, ADMIN_ROLE, "Info"),
	("En cours", 0, TECHNICIAN_ROLE, "Primary"),
	("Sous contrôle", 0, QUALITY_ROLE, "Inverse"),
	("Terminé", 1, ADMIN_ROLE, "Success"),  # docstatus 1 => ticket is submitted (locked)
]

# (from, action, to, allowed role, condition, allow_self_approval)
# Conditions only decide which buttons are offered; the authoritative checks are
# in rvx_ticket.py (ALLOWED_TRANSITIONS + actor + QR verification).
TRANSITIONS = [
	("En attente", "Assigner", "Assigné", ADMIN_ROLE,
	 "doc.technician_provider and doc.assigned_user", 1),
	("Assigné", "Démarrer l'intervention", "En cours", TECHNICIAN_ROLE,
	 "doc.assigned_user == frappe.session.user", 1),
	("En cours", "Soumettre au contrôle", "Sous contrôle", TECHNICIAN_ROLE,
	 "doc.assigned_user == frappe.session.user and doc.intervention_report and doc.attachments_before_after", 1),
	("Sous contrôle", "Clôturer", "Terminé", ADMIN_ROLE,
	 "doc.assigned_user != frappe.session.user", 0),
	("Sous contrôle", "Clôturer", "Terminé", QUALITY_ROLE,
	 "doc.assigned_user != frappe.session.user", 0),
]


def after_install():
	sync_security_config()


def after_migrate():
	sync_security_config()


def sync_security_config():
	ensure_roles()
	if frappe.db.exists("DocType", DOCTYPE):
		ensure_workflow()
	frappe.db.commit()


def ensure_roles():
	for role in ROLES:
		if not frappe.db.exists("Role", role):
			frappe.get_doc({"doctype": "Role", "role_name": role, "desk_access": 1}).insert(
				ignore_permissions=True
			)


def ensure_workflow():
	for state, _docstatus, _role, style in STATES:
		if not frappe.db.exists("Workflow State", state):
			frappe.get_doc(
				{"doctype": "Workflow State", "workflow_state_name": state, "style": style}
			).insert(ignore_permissions=True)

	for action in {t[1] for t in TRANSITIONS}:
		if not frappe.db.exists("Workflow Action Master", action):
			frappe.get_doc({"doctype": "Workflow Action Master", "workflow_action_name": action}).insert(
				ignore_permissions=True
			)

	if frappe.db.exists("Workflow", WORKFLOW_NAME):
		wf = frappe.get_doc("Workflow", WORKFLOW_NAME)
	else:
		wf = frappe.new_doc("Workflow")
		wf.workflow_name = WORKFLOW_NAME

	wf.document_type = DOCTYPE
	wf.workflow_state_field = "status"  # re-uses the Select field of the DocType
	wf.is_active = 1
	wf.send_email_alert = 0
	wf.set("states", [])
	wf.set("transitions", [])

	for state, docstatus, allow_edit, _style in STATES:
		wf.append("states", {"state": state, "doc_status": str(docstatus), "allow_edit": allow_edit})

	for state, action, next_state, allowed, condition, self_approval in TRANSITIONS:
		wf.append(
			"transitions",
			{
				"state": state,
				"action": action,
				"next_state": next_state,
				"allowed": allowed,
				"condition": condition,
				"allow_self_approval": self_approval,
			},
		)

	wf.save(ignore_permissions=True)
