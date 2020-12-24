spam = ['apples', 'bananas', 'tofu', 'cats']

def change_form(name):
    for i in range(len(name) - 1):
        print(name[i] +', ' , end = '')
    print('and ' + name[-1])

change_form(spam)