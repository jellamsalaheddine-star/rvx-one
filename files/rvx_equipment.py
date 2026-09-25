import frappe
from frappe.model.document import Document

class RVXEquipment(Document):
    def before_insert(self):
        # توليد كود الـ QR التلقائي والمشفر للمعدة بناءً على الرقم الترتيبي
        if self.serial_number:
            self.qr_code = f"RVX-QR-{self.serial_number}"
