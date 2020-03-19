from tk import tk
import requests
from config import get_lang

BASE_URL = "https://translate.google.cn/translate_a/single"


def GoogleTranslate(SL, TL, QUERY):
    TK = tk.tk(QUERY)
    tt = BASE_URL + "?client=t&hl=en&dt=t&dt=bd&sl={}&tl={}&tk={}&q={}"\
        .format(SL, TL, TK, QUERY)
    response = requests.get(tt)
    return response.json()


def RecgLang(QUERY):
    TK = tk.tk(QUERY)
    response = requests.get(BASE_URL + "?client=t&sl=auto&tl=auto&tk={}&q={}"
                            .format(TK, QUERY))
    re_lang = response.json()[2]
    my_lang = get_lang("My_Language")
    if re_lang != my_lang:
        [SL, TL] = [re_lang, my_lang]
    else:
        obj_lang = get_lang("Obj_Language")
        [SL, TL] = [my_lang, obj_lang]
    return [SL, TL]


if __name__ == "__main__":
    print(GoogleTranslate("en", "zh-CN", "waste"))
    print(GoogleTranslate("zh-CN", "en", "计划"))
    print(RecgLang("中文 Maximum number of shown per line"))
    print(RecgLang("每行顯示的最大數量"))
    print(RecgLang("Maximum number of shown per line"))
    print(RecgLang("行ごとに表示される最大数"))
