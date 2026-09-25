# -*- coding: utf-8 -*-
# © 2026 RELVORIX SERVICES. All Rights Reserved.
# Financial Intelligence, Quoting, and Margin Calculation Engine for RVX ONE

class RVXFinanceEngine:
    @staticmethod
    def calculate_quote_margins(quote_doc):
        """حساب الأرباح الصافية ونسبة الهامش المالي تلقائياً لكل عرض سعر"""
        cout_fournisseur = quote_doc.get("cout_fournisseur") or 0.0
        prix_client = quote_doc.get("prix_client") or 0.0
        
        # حساب الربح الصافي: ثمن الزبون ناقص تكلفة المتدخل أو السلعة
        net_profit = round(prix_client - cout_fournisseur, 2)
        quote_doc.marge_beneficiaire = net_profit
        
        # حساب النسبة المئوية للأرباح لضمان المردودية المالية
        if prix_client > 0:
            quote_doc.pourcentage_marge = round((net_profit / prix_client) * 100, 2)
        else:
            quote_doc.pourcentage_marge = 0.0
            
        print(f"💰 [RVX Finance]: Financial Margin Calculated. Profit: {net_profit} DH ({quote_doc.pourcentage_marge}%)")

    @staticmethod
    def enforce_quote_approval_before_dispatch(ticket_doc):
        """قفل مالي: منع تحويل التذكرة للتنفيذ إذا كانت تحتاج لعرض سعر ولم يوافق عليه الزبون"""
        status = ticket_doc.get("status")
        requires_quote = ticket_doc.get("requires_quote") or False
        is_quote_approved = ticket_doc.get("is_quote_approved") or False
        
        if requires_quote and status == "SCHEDULED" and not is_quote_approved:
            raise Exception("🚨 [قفل مالي - RELVORIX]: لا يمكن جدولة التدخل! هذا الطلب يتطلب عرض سعر (Devis) وموافقة رقمية معتمدة من طرف الزبون أولاً.")
            
        print("✅ [RVX Finance]: Ticket workflow financial validation passed.")

    @staticmethod
    def generate_invoice_summary(ticket_doc):
        """توليد كشف الحساب النهائي والإجمالي مورا إغلاق التذكرة بنجاح"""
        if ticket_doc.get("status") == "CLOSED":
            total_hardware_cost = ticket_doc.get("total_hardware_cost") or 0.0
            labor_cost = ticket_doc.get("labor_cost") or 0.0
            ticket_doc.total_invoice_amount = round(total_hardware_cost + labor_cost, 2)
            print(f"📊 [RVX Billing]: Final Invoice Generated: {ticket_doc.total_invoice_amount} DH")
