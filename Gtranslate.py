# -*- coding: utf-8 -*-
from wox import Wox, WoxAPI
from GoogleTranslate import GoogleTranslate
import re
import webbrowser
try:
    import pyperclip
    flag = True
except ImportError:
    flag = False


PREFIX_DICT = {"noun": "n", "verb": "v", "pronoun": "pron", "adjective": "adj",
               "adverb": "adv", "numeral": "num", "article": "art",
               "preposition": "prep", "conjunction": "conj", "interjection": "interj"}
ITEM_MAX_LEN = 7
ICO_PATH = "Images/Gtranslate.png"


class Gtranslate(Wox):
    def query(self, query):

        # 判断语言（全英文才翻译为中文）
        [SL, TL] = ["en", "zh-CN"]
        for ch in query:
            if u'\u4e00' <= ch <= u'\u9fff':
                [SL, TL] = ["zh-CN", "en"]
                break
        # if re.search('[a-z]', query):

        Jresponse = GoogleTranslate(query, SL, TL)

        results = []
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

        # 词
        if Jresponse[1] != None:
            for item in Jresponse[1]:
                prefix = item[0]
                if prefix in PREFIX_DICT:
                    prefix = PREFIX_DICT[prefix]

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

    def openUrl(self, url):
        webbrowser.open(url)

    def copy(self, ans):
        if flag:
            pyperclip.copy(ans)
        else:
            WoxAPI.change_query("ERROR: pacage pyperclip is not installed")


if __name__ == "__main__":
    Gtranslate()
