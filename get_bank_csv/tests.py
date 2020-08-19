from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse, resolve
from .views import uplode_csv,bank_statement_without_category_page,bank_statement_update_page,bank_statement_page,bank_allStatement_page
from .models import *

class TestUrls(SimpleTestCase):

	def test_home_url_is_resolved(self):
		url=reverse('get_bank_csv:home')
		#print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,bank_statement_page)
		self.assertEqual(resolve(url).route,'get_csv/')

	def test_uplode_csv_url_is_resolved(self):
		url=reverse('get_bank_csv:uplode_csv')
		#print(resolve(url))
		self.assertEquals(resolve(url).func,uplode_csv)
		self.assertEqual(resolve(url).route,'get_csv/uplode')

	def test_withoutCategoryList_url_is_resolved(self):
		url=reverse('get_bank_csv:withoutCategoryList')
		#print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,bank_statement_without_category_page)
		self.assertEqual(resolve(url).route,'get_csv/withoutCategoryList')

	def test_transiaction_edite_url_is_resolved(self):
		url=reverse('get_bank_csv:transiaction_edite',args=['20200812103020D2000'])
		#print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,bank_statement_update_page)
		self.assertEqual(resolve(url).route,'get_csv/<str:pk>/edit')

	def test_allTransiaction_url_is_resolved(self):
		url=reverse('get_bank_csv:allTransiaction')
		#print(resolve(url))
		self.assertEquals(resolve(url).func.view_class,bank_allStatement_page)
		self.assertEqual(resolve(url).route,'get_csv/allTransiaction')

	