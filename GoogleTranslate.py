from tk import tk
import requests
from config import get_lang


BASE_URL = "https://translate.google.cn/translate_a/single"


def GoogleTranslate(SL, TL, QUERY):
    TK = tk.tk(QUERY)

    response = requests.get("%s%s" % (BASE_URL,
                                      '''?client=t&hl=en
                                      &dt=bd&dt=t&dt=ss
                                      &sl={}&tl={}&tk={}&q={}'''
                                      .format(SL, TL, TK, QUERY)))

    return response.json()


def RecgLang(QUERY):
    TK = tk.tk(QUERY)
    response = requests.get(url=BASE_URL,
                            params={"client": "t",
                                    "tk": TK, "q": QUERY,
                                    "sl": "auto", "tl": "auto"})
    re_lang = response.json()[2]
    my_lang = get_lang("My Language")
    if re_lang != my_lang:
        [SL, TL]=[re_lang, my_lang]
    else:
        obj_lang = get_lang("Obj Language")
        [SL, TL]=[my_lang, obj_lang]
    return [SL, TL]


if __name__ == "__main__":
    print(GoogleTranslate("en", "zh-CN", "round"))
    print(RecgLang("中文 Maximum number of shown per line"))
    print(RecgLang("Maximum number of shown per line"))
    print(RecgLang("行ごとに表示される最大数"))

