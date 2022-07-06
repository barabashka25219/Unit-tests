# Демонстрация тестирования отдельных функций

import unittest
from cities import get_formatted_city_name

class TestCityName(unittest.TestCase):

	# Тест на сравнение форматированного имени города без численности населения
	def test_city_country(self):
		result = get_formatted_city_name('pskov', 'russia')
		self.assertEqual(result, 'pskov russia')

	# Тест с чиленностью населения
	def test_city_country_population(self):
		result = get_formatted_city_name('new-york', 'usa', 8038000)
		self.assertEqual(result, 'new-york usa 8038000')

if __name__ == '__main__':
	unittest.main()