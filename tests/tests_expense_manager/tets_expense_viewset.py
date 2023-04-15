from tests.test_setup import TestSetup
from tests.factorys.expense_manager.expense_factories import SupplierFactory
from    rest_framework import status 

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