from module2 import TransLate, LangDetect

text = input("Введіть текст для перекладу: ")
src_lang = input("Введіть код мови оригіналу (або 'auto'): ")
dest_lang = input("Введіть код мови для перекладу: ")

# Переклад тексту
translation = TransLate(text, src_lang, dest_lang)
print(f"Переклад: {translation}")

# Визначення мови
detected_lang = LangDetect(text, "all")
print(f"Детекція мови: {detected_lang}")
