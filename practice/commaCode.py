spam = ['apples', 'bananas', 'tofu', 'cats']
dog = ['bone', 'collar']
cat = ['orange']

def commaCode(list):
    if len(list) > 1:
        list.insert(-1, 'and')
        print(', '.join(map(str, list)))
    else:
        print(list[0])

commaCode(spam)
commaCode(dog)
commaCode(cat)