'''1) Создать следущие переменные
integer reg_year_days=365,
integer leap_year_days=366,
float real_year_days=365.25,
boolean is_leap_year=True,
string reg="Regular year"
string leap="Leap year"'''

reg_year_days=365 # Integer
leap_year_days=366 # Integer
real_year_days= 365.25 # Float
is_leap_year=True # Boolean
reg="Regular year" # String
leap="Leap year" # String

'''2) Создать tuples
year_2021 = (2021,False,reg_year_days)
year_2022 = (2022,False,reg_year_days)
year_2023 = (2023, False, reg_year_days)
year_2024 = (2024, is_leap_year, leap_year_days)
'''

year_2021 = (2021,False,reg_year_days)
year_2022 = (2022,False,reg_year_days)
year_2023 = (2023, False, reg_year_days)
year_2024 = (2024, is_leap_year, leap_year_days)

'''3) Попробовать поменять значения 2022 года на високосный год (leap year)
'''
# В кортеже нельзя изменять данные

'''4) Создать list years и добавить в него все года
'''
years=[year_2021,year_2022,year_2023,year_2024]

'''5) Пройти через лист при помощи цикла for и для каждого года вывести следущее сообщение при помощи конкатенации строк
 ("some text",variable, "another text",another_vaiable) или ("some text" + variable + "another text" + another_vaiable)
 Текст должен выглядеть вот так:
 	"2022 is regular year and has 365 days"
 	или
  	"2024 is leap year and has 366 days" (данная строка должна быть только заглавными буквами)
В зависимости от значения второй переменной в tuple (используйте if-else).
'''

for test in years:
    if test[1]==False:
        print(test[0], 'is', reg, 'and has', reg_year_days, "days")
    else:
        print(str.upper('2024 is'),str.upper(leap), str.upper('and has'), leap_year_days, str.upper('days'))

'''6) Добавить к листу с годами еще один год (в виде tuple смотри пункт 2) и вывести количество элементов на консоль:
"В Листе years <столько-то> элементов" 
'''
year_2025 = (2025, False, reg_year_days)
years.append(year_2025)
count_years= len([num for num in years if num !=0])
print('В листе years', count_years,'элементов')

'''5) Пройти через лист при помощи цикла for и для каждого года вывести следущее сообщение при помощи форматировнной строки
 (f"some text {variable} "another text" {another_vaiable}) или ("some text {} another text {}".format(variable,another_vaiable))
 Логика такая же как в пункте 5.
 '''
for test_2 in years:
    if test_2[1]==False:
        print(f"{test_2[0]} is {reg} and has {reg_year_days} days")
    else:
        print(str.upper("{} is {} and has {} days".format(test_2[0], leap, leap_year_days)))
'''6) Создайте словарь c годами где ключ год - значение количество дней (от 2020 до 2030)
'''

years_dict={"2020": 366, "2021": 365, "2022": 365, "2023": 365, "2024":366, "2025": 365, "2026": 365, "2027":365, "2028":366,"2029": 365, "2030":365}

'''7*) При помощи цикла for вывести из словаря только не високосные года. <--- Задание со звездочкой))) На пятерку)))
'''
for key, value in years_dict.items():
    if value == 365:
        print("Не високосный год это:",key)


