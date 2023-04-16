from tests.test_setup import TestSetup
from tests.factorys.expense_manager.expense_factories import SupplierFactory
from rest_framework import status 
from apps.expense_manager.models import Supplier

class ExpenseTestCase(TestSetup):
    url = '/expense/expense/'
    def test_search_supplier(self):
        supplier = SupplierFactory().create_supplier
        responde = self.client.get(
            self.url +'search_supplier/',
            {
                'ruc_or_business_name': supplier.ruc

            },
            format = 'json'
        )

        self.assertEqual(responde.status_code, status.HTTP_200_OK)
        self.assertEqual(responde.data['ruc'], supplier.ruc) 


    def test_new_supplier(self):
        supplier = SupplierFactory().build_supplier_JSON()
        response = self.client.post(
            self.url + 'new_suplier/',
            supplier,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.all().count(), 1)
        self.assertEqual(response.data['supplier']['ruc'], supplier['ruc'])