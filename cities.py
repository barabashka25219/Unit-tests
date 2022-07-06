# Функция для получения форматированного имени города
def get_formatted_city_name(city, country, population=''):
	
	# Если указана численность населения города, то добавить в результат вывода
	if population:
		return f"{city} {country} {population}"

	return f"{city} {country}"