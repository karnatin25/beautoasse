from django.test import TestCase

# # # Create your tests here.



from .models import Product_Beato

class ProductTestCase(TestCase):
    def setUp(self):
        Product_Beato.objects.create(name="Dell", description="4 GB Ram and 1 TB hard disk", cost_per_item=35000 ,stock_quantity=10)

    def test_product_value(self):

        data = Product_Beato.objects.get(name="Dell")

        self.assertEqual(data.volume,(data.cost_per_item*data.stock_quantity))
        print('hi test case passed')
