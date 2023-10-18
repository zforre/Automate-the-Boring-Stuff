spam = 42 #global variable

def eggs():
    spam = 42 #local variable

print('some code here') #global variable

def spam():
    eggs = 99

spam()
print(eggs) #error because eggs isnt available globally

eggs = 42

def spam():
    global eggs #I want to target the global eggs variable
    eggs = "hello" #changes gloabl variable eggs value to "hello"
    print(eggs)

spam()
print(eggs)