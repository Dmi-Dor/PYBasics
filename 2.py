def my_func(name, surname, year, city, email, mobile):
    return ' '.join([name, surname, year, city, email, mobile])
print(my_func(surname='Petrov', name='Vasilyi', year='2001', city='Smolensk', email='petrov@mailru.ru',
              mobile='8-911-111-11-11'))