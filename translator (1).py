from translate import Translator
fromlanguage=input("Enter your input language:")
tolanguage=input("Enter the required language:")
translator= Translator(from_lang=fromlanguage,to_lang=tolanguage)
sentence=input("Enter the words you want to translate:")
translation = translator.translate(sentence)
print(translation)
