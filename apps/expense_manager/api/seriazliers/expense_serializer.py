from rest_framework import serializers


from apps.expense_manager.models import Expense,Supplier

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        exclude = ('state','created_date','modified_date','deleted_date') 

    def save(self, **kwargs):
        new_supplier = Supplier.objects.create(**self.validated_data)
        return new_supplier.to_dict()
    
class SupplierSerializerRegister(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        exclude = ('state','created_date','modified_date','deleted_date') 