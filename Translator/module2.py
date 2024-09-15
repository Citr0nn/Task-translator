from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translated = GoogleTranslator(source=scr, target=dest).translate(text)
        return translated
    except Exception as e:
        return f"Помилка: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        detected_langs = detect_langs(text)
        detected_lang = detected_langs[0]
        if set == "lang":
            return detected_lang.lang
        elif set == "confidence":
            return detected_lang.prob
        else:
            return f"Мова: {detected_lang.lang}, Впевненість: {detected_lang.prob}"
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
