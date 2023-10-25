def eggs(someParam):
    someParam.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# a return value is not used to assign a new value to spam. Instead, it modifies the list in place, directly.
# Even though spam and someParam contain separate references, they both refer to the same list. This is why the append('Hello') method call inside the function affects the list even after the function call has returned.