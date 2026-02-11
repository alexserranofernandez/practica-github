letra=input("")
vocales="AEIOUaeiou"
if letra.isupper():
    if letra in vocales:
        print("uppercase")
        print("vowel")
    else:
        print("uppercase")
        print("consonant")
else:
    if letra in vocales:
        print("lowercase")
        print("vowel")
    else:
        print("lowercase")
        print("consonant")