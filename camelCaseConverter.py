import string

camelSentence = input("Please enter a sentence to be converted to camelcase. ")

convertedSentence = camelSentence.title().replace(" ", "")
convertedSentence = convertedSentence[0].lower() + convertedSentence[1:]

print(convertedSentence.find(string.punctuation))

if convertedSentence[0].isdigit() or convertedSentence.find(string.punctuation) != int:
    print("This will be an invalid variable name.")

print(convertedSentence)