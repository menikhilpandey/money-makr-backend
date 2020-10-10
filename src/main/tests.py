from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Wallet
from .models import Category

# Create your tests here.

class RestApiTests(APITestCase):

    def test_walletCreate(self):
        wallet = {
            'name': 'test_wallet_1',
            'wallet_type': 'bank',
            'currency': 'INR',
            'balance': 2000
        }
        response = self.client.post('/api/v1/wallet/', wallet, format = 'json')
        self.assertEqual(Wallet.objects.count(), 1)
        self.assertEqual(Wallet.objects.get().name, 'test_wallet_1')

    def test_walletUpdate(self):
        wallet_init = {
            'name': 'test_wallet_1',
            'wallet_type': 'digital_wallet',
            'currency': 'INR',
            'balance': 2000
        }
        response = self.client.post('/api/v1/wallet/', wallet_init, format = 'json')
        
        self.assertEqual(Wallet.objects.count(), 1)
        self.assertEqual(Wallet.objects.get().name, 'test_wallet_1')
        self.assertEqual(Wallet.objects.get().wallet_type, 'digital_wallet')
        self.assertEqual(Wallet.objects.get().slug, 'test_wallet_1-digital_wallet')

        wallet_update = {
            'name': 'test_wallet_1',
            'wallet_type': 'bank',
            'currency': 'INR',
            'balance': 20000
        }

        response = self.client.put("/api/v1/wallet/" + Wallet.objects.get().slug + "/", wallet_update, format = 'json')
        
        self.assertEqual(Wallet.objects.count(), 1)
        self.assertEqual(Wallet.objects.get().name, 'test_wallet_1')
        self.assertEqual(Wallet.objects.get().balance, 20000)
        self.assertEqual(Wallet.objects.get().wallet_type, 'bank')

    def test_categoryCreate(self):
        category_parent = {
            'name': 'shopping'
        }

        response = self.client.post('/api/v1/category/', category_parent, format = 'json')

        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'shopping')

        category_child = {
            'name': 'electronics',
            'parent': Category.objects.get().id
        }

        response = self.client.post('/api/v1/category/', category_child, format = 'json')

        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(Category.objects.get(name = "electronics").parent, Category.objects.get(name = "shopping"))

    def test_categoryUpdate(self):
        category = {
            'name': 'groceries'
        }

        response = self.client.post('/api/v1/category/', category, format = 'json')

        category_child = {
            'name': 'fruits',
            'parent': Category.objects.get().id
        }

        response = self.client.post('/api/v1/category/', category_child, format = 'json')

        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(Category.objects.get(name = "fruits").parent, Category.objects.get(name = "groceries"))
        
        category_updated = {
            'name': 'fruits and vegetables'
        }

        response = self.client.put('/api/v1/category/' + Category.objects.get(name = 'groceries').slug + "/", category_updated, format = 'json')
        
        self.assertEqual(Category.objects.count(), 2)
        self.assertEqual(Category.objects.get(name = "fruits").parent, Category.objects.get(name = "fruits and vegetables"))





