from django.contrib import admin
from apps.expense_manager.models import *
# Register your models here.

admin.site.register(Supplier)
admin.site.register(PaymentType)
admin.site.register(Voucher)
admin.site.register(ExpenseCategory)
admin.site.register(Expense)