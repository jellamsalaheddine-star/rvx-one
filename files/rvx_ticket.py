import frappe
from frappe.model.document import Document
from rvx_one.security import CUSTOMER_SIGN_OFF_REQUIRED, MAX_RESOLUTION_HOURS

class RVXTicket(Document):
    def before_save(self):
        # التحقق من الأمان وعزل البيانات لـ RVX ONE
        if self.status == "Terminé" and CUSTOMER_SIGN_OFF_REQUIRED:
            if not self.get("customer_signature"):
                frappe.throw("خطأ أمني: لا يمكن إغلاق الشكاية بدون توقيع الزبون الرقمي المعتمد!")
