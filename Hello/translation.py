def translate(text):
    translation = ""
    for letter in text:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "S"
            else:
                translation = translation + "s"

        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a text: ")))



