# -*- coding: utf-8 -*-
from wox import Wox, WoxAPI
from GoogleTranslate import GoogleTranslate, RecgLang
import webbrowser
try:
    import pyperclip
    flag = True
except ImportError:
    flag = False


DICT_PREFIX = {"noun": "n", "verb": "v", "pronoun": "pron", "adjective": "adj",
               "adverb": "adv", "numeral": "num", "article": "art", "preposition": "prep",
               "conjunction": "conj", "interjection": "interj", "abbreviation": "abbr"}
ITEM_MAX_LEN = 10
ICO_PATH = "Images/Gtranslate.png"


class Gtranslate(Wox):
    # 翻译请求
    def query(self, query):
        
        # 识别语言
        [SL, TL] = RecgLang(query)
        # 翻译
        Jresponse = GoogleTranslate(SL, TL, query)

        results = []
        # 简单翻译
        results.append({
            "Title": Jresponse[0][0][0],
            "SubTitle": "复制到剪贴板",
            "IcoPath": ICO_PATH,
            "JsonRPCAction": {
                "method": "copy",
                "parameters": [Jresponse[0][0][0]],
                "dontHideAfterAction": True,
            },
        })

        # 词(组)详情
        if Jresponse[1] != None:
            for item in Jresponse[1]:
                prefix = item[0]
                if prefix in DICT_PREFIX:
                    prefix = DICT_PREFIX[prefix]

                str = "%s.  %s" % (prefix,
                                   ", ".join(item[1][:(min(len(item[1]), ITEM_MAX_LEN))]))
                results.append({
                    "Title": str,
                    "IcoPath": ICO_PATH,

                    "SubTitle": "浏览器查看详情",
                    "JsonRPCAction": {
                        "method": "openUrl",
                        "parameters": ["https://translate.google.cn/#view=home&op=translate&sl={}&tl={}&text={}"
                                       .format(SL, TL, query)],
                        "dontHideAfterAction": True,
                    },
                })

        return results

    def copy(self, ans):
        if flag:
            pyperclip.copy(ans)
        else:
            WoxAPI.change_query("ERROR: pacage pyperclip is not installed")

    def openUrl(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    Gtranslate()
