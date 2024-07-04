def add(x, y):
    return x + y


# x=1 ## definir asi variables da error en el lint
# y=2
# print(f"This is a sum: {x}, {y}, {add(x,y)}")

# bien hecho para el lint

result = (1, 2)
print("result sum: %s" % result)
