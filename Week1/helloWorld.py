# Week 1 of learning Python
# This program says hello, takes in input to ask for your name, and says hello!
# It also asks the user for age and calculates how old you'll be in a year.

print('Hello world!')

print('What is your name?')
userName = input() # takes input from user for name
print('It is nice to meet you, ' + userName + '!')

print('Your name has this many letters: ')
print (len(userName)) # calculats length of user's name

print('What is your age?')
userAge = input() # takes input from user for age
print('You will be ' + str(int(userAge) + 1) + ' in a year!')
