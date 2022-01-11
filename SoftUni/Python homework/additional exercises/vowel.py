def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation += "g"
        else:
            translation += letter
    return translation

print(translate(input("Enter a phrase: ")))