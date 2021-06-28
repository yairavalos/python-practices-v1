def suma(a, b):
    if isinstance(a, str) and ~isinstance(a, str):
        return (str(a) + str(b))
    else:
        return (a + b)
def resta(a, b):
    return (a - b)