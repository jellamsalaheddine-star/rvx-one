# -*- coding: utf-8 -*-
# © 2026 RELVORIX SERVICES. All Rights Reserved.
# Custom Digital Checklists and Quality Enforcement System for RVX ONE

class RVXChecklistEnforcer:
    @staticmethod
    def validate_cleaning_checklist(doc):
        """التحقق من لوائح الفحص الخاصة بـ خدمات النظافة العامة"""
        required_fields = ["sol_nettoye", "vitres_propres", "poubelles_videes"]
        for field in required_fields:
            if doc.get(field) == "NOK":
                raise Exception("🚨 [خطأ جودة - RELVORIX]: لا يمكن إغلاق الطلب! هناك عناصر غير مطابقة في لائحة النظافة العامة.")
        print("🧼 [RVX Quality]: Cleaning Checklist fully validated (OK).")

    @staticmethod
    def validate_gardening_checklist(doc):
        """التحقق من لوائح الفحص الخاصة بـ خدمات البستنة والمساحات الخضراء"""
        required_fields = ["gazon_arrose", "arbres_tailles", "insecticide_applique"]
        for field in required_fields:
            if doc.get(field) == "NOK":
                raise Exception("🚨 [خطأ جودة - RELVORIX]: لا يمكن إغلاق الطلب! يجب تصحيح عناصر لائحة البستنة وسقي المساحات الخضراء أولاً.")
        print("🌿 [RVX Quality]: Gardening Checklist fully validated (OK).")

    @staticmethod
    def validate_maintenance_checklist(doc):
        """التحقق من لوائح الفحص الخاصة بـ خدمات الصباغة والترميم والصيانة العامة"""
        required_fields = ["zone_preparee", "peinture_conforme", "protection_sols"]
        for field in required_fields:
            if doc.get(field) == "NOK":
                raise Exception("🚨 [خطأ جودة - RELVORIX]: لا يمكن إغلاق الطلب! لائحة الصباغة والترميم تحتوي على عناصر غير مطابقة للمعايير.")
        print("🛠️ [RVX Quality]: Maintenance & Painting Checklist fully validated (OK).")

    @staticmethod
    def enforce_quality_before_close(ticket_doc):
        """يربط استمارات الفحص بـ الشكاية الرئيسية ويمنع الإغلاق في حالة وجود أي خلل"""
        service_type = ticket_doc.get("service_type") # نوع الخدمة: Cleaning, Gardening, Maintenance
        
        if service_type == "Cleaning":
            RVXChecklistEnforcer.validate_cleaning_checklist(ticket_doc)
        elif service_type == "Gardening":
            RVXChecklistEnforcer.validate_gardening_checklist(ticket_doc)
        elif service_type == "Maintenance":
            RVXChecklistEnforcer.validate_maintenance_checklist(ticket_doc)
            
        print("✅ [RVX Core Engine]: Global Quality Audit Passed for Ticket: " + str(ticket_doc.get("name")))
