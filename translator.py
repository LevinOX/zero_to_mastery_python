from translate import Translator
language = 'de'
translator = Translator(to_lang=language)

try:
    with open('test.txt', 'r') as f:
        text = f.read()
        translation = translator.translate(text)
        print(f"translated to: {translation}")
        with open(f"test_{language}.txt", 'w') as f:
            f.write(translation)
except FileNotFoundError as err:
    print(f"error occurred: {err}")
