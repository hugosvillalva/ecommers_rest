from faker import Faker

from apps.expense_manager.models import Supplier

faker = Faker()

class SupplierFactory:


    def build_supplier_JSPM(self):
        return{
            'ruc' : str(faker.random_number(digits=11)),
            'bussines_name' : faker.company(),
            'addres' : faker.address(),
            'phone': faker.phone_number(),
            'email': faker.email()
        }


    def create_supplier(self):
        return Supplier.objects.create(**self.build_supplier_JSPM)