from django.test import TestCase
from webshop.models import products, vat_info

class ProductsTest(TestCase):

    def create_vat_info(self, country_id='SE', country_vat = 0.25):
        return vat_info.objects.create(
                                    country_id = country_id,
                                    country_vat = country_vat)

    def create_product(self, item_id='101777373', item_name='GARMIN VIVOFIT JR LAVA', item_price=99.00, manufacturing_country=8):
        return products.objects.create(
                                        item_id=item_id,
                                        item_name=item_name,
                                        item_price=item_price,
                                        manufacturing_country=self.create_vat_info())

    def test_product_creation(self):
        p = self.create_product()
        self.assertTrue(isinstance(p, products))
        self.assertAlmostEqual(p.__str__(), p.item_name)