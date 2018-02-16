#Nick Zapata - Daily lesson - 2/8/18

from datetime import datetime
name = input('Enter your name: ')
age = int(input('Enter your age: '))
hundred = int((100-age) + datetime.now().year)
print('Hello %s. you are %s years old. You will turn 100 years old in %s.' % (name, age, hundred))