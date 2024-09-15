from googletrans import Translator

translator = Translator()

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translated = translator.translate(text, src=scr, dest=dest)
        return translated.text
    except Exception as e:
        return f"Помилка: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return detection.confidence
        else:
            return f"Мова: {detection.lang}, Впевненість: {detection.confidence}"
    except Exception as e:
        return f"Помилка: {e}"

def CodeLang(lang: str) -> str:
    languages = {
        'af': 'Afrikaans', 'sq': 'Albanian', 'en': 'English', 'uk': 'Ukrainian', 'es': 'Spanish'
    }
    if lang in languages:
        return languages[lang]
    elif lang.lower() in [v.lower() for v in languages.values()]:
        return [k for k, v in languages.items() if v.lower() == lang.lower()][0]
    else:
        return "Невідомий код або мова"
