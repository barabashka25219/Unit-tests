# Демонстрация тестирования класса

from employee import Employee
import unittest

# Набор тестов увеличения заработной платы сотрудника
class TestEmployeeSalary(unittest.TestCase):

	# С помощью setUp() загружаем объект, который будем тестировать
	def setUp(self):
		self.e = Employee('john', 'week', 5000)

	# Тест увеличения заработной платы сотрудника по дефолту
	def test_give_raise_default(self):
		self.e.give_raise()
		self.assertEqual(self.e.salary, 10000)

	# Тест увеличения заработной платы по указанному значению
	def test_give_raise_custom(self):
		self.e.give_raise(10000)
		self.assertEqual(self.e.salary, 15000)


# Тест получения форматированного имени сотрудника
class TestEmployeeName(unittest.TestCase):
	def setUp(self):
		self.e = Employee('john', 'week', 5000)

	def test_formatted_name(self):
		name = self.e.get_formatted_name()
		self.assertEqual(name, 'John Week')

if __name__ == '__main__':
	unittest.main()