py = "Python is Amazing"
print(py.upper()) #대문자
print(py.lower()) #소문자
print(py[0].isupper())
print(py[1].isupper())
print(len(py))
print(py.replace("Python","Java"))

index = py.index("n")
print(index)

index = py.index("n", index + 1)
print(index)