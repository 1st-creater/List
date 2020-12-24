my_pet = ['Zoophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in my_pet:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')