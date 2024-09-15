import os
from module1 import TransLate

config_file = 'config.txt'
if not os.path.exists(config_file):
    print(f"Файл конфігурації {config_file} не знайдено.")
else:
    with open(config_file, 'r') as f:
        lines = f.readlines()

    # Отримання даних з файлу конфігурації
    text_file = lines[0].strip()
    dest_lang = lines[1].strip()
    output = lines[2].strip()

    if os.path.exists(text_file):
        with open(text_file, 'r') as f:
            text = f.read()

        # Переклад
        translation = TransLate(text, 'auto', dest_lang)

        if output == 'file':
            output_file = f"{text_file.split('.')[0]}_{dest_lang}.txt"
            with open(output_file, 'w') as f:
                f.write(translation)
            print(f"Переклад збережено в файл {output_file}")
        else:
            print(f"Переклад: {translation}")
    else:
        print(f"Файл {text_file} не знайдено.")
