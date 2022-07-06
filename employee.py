# Класс, описывающий работника

class Employee:
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.salary = salary
		self.annual_allowance = 5000

	# Метод увеличения заработной платы сотрудника
	def give_raise(self, custom_value=0):

		# Если указано кастомное значение, то увеличить на него
		if custom_value:
			self.salary += custom_value

		else:
			self.salary += self.annual_allowance

	# Получение форматированного имени сотрудника
	def get_formatted_name(self):
		return f"{self.first.title()} {self.last.title()}"