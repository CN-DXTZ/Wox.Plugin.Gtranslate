from tk import tk
import requests


def GoogleTranslate(QUERY, SL, TL):
    TK = tk.tk(QUERY)

    response = requests.get("https://translate.google.cn/translate_a/single?client=t&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&pc=1&otf=1&ssel=0&tsel=0&xid=1791806&kc=1&sl={}&tl={}&tk={}&q={}"
                            .format(SL, TL, TK, QUERY))
    return response.json()


if __name__ == "__main__":
    print(GoogleTranslate("round", "en", "zh-CN")[0][0][0])
