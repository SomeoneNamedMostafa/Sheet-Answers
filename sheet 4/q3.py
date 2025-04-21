def substitute(equation, **kwargs):
    for x, y in kwargs.items():
        equation = equation.replace(x, str(y))
    return equation
print(substitute("x * 2 + y * 3 - z * 4", x=5,y=6,z=7))