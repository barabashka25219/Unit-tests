# Модуль для объединения тестов в группы и их одновременного запуска

import unittest
from test_employee import TestEmployeeSalary, TestEmployeeName
from test_cities import TestCityName

# Протестируем набор тестов из модулей test_employee, test_cities

employeeTestSuite = unittest.TestSuite()
employeeTestSuite.addTest(unittest.makeSuite(TestEmployeeSalary))
employeeTestSuite.addTest(unittest.makeSuite(TestEmployeeName))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(employeeTestSuite)

cityTestSuite = unittest.TestSuite()
cityTestSuite.addTest(unittest.makeSuite(TestCityName))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(cityTestSuite)