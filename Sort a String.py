def sortastring(stringin):
    stringin = stringin.split()
    stringin.sort()
    return stringin

stringin = input("Enter a string: ")
sortastring(stringin)