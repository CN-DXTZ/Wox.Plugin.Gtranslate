# -*- coding: utf-8 -*-
from wox import Wox, WoxAPI
from GoogleTranslate import GoogleTranslate, RecgLang
from config import get_list, set_lang
import webbrowser
try:
    import pyperclip
    flag_package = True
except ImportError:
    flag_package = False


DICT_PREFIX = {"noun": "n", "verb": "v", "pronoun": "pron", "adjective": "adj",
               "adverb": "adv", "numeral": "num", "article": "art", "preposition": "prep",
               "conjunction": "conj", "interjection": "interj", "abbreviation": "abbr"}
ICO_PATH = "Images/Gtranslate.png"
ITEM_MAX_LEN = 10
PREFIX_CONFIG = "tran _config"


class Gtranslate(Wox):

    def query(self, query):
        results = []
        # 翻译
        if query[0] != "_":
            # 识别语言
            [SL, TL] = RecgLang(query)
            # 翻译
            Jresponse = GoogleTranslate(SL, TL, query)

            # 简单翻译结果
            results.append({
                "IcoPath": ICO_PATH,
                "Title": Jresponse[0][0][0],
                "SubTitle": "复制到剪贴板",
                "JsonRPCAction": {
                    "method": "copy",
                    "parameters": [Jresponse[0][0][0]],
                    "dontHideAfterAction": False,
                },
            })

            # 词(组)详情
            if Jresponse[1] != None:
                for item in Jresponse[1]:
                    prefix = item[0]
                    if prefix in DICT_PREFIX:
                        prefix = DICT_PREFIX[prefix]

                    str = "{}.  {}".format(prefix, ", ".join(
                        item[1][:(min(len(item[1]), ITEM_MAX_LEN))]))
                    results.append({
                        "IcoPath": ICO_PATH,
                        "Title": str,
                        "SubTitle": "浏览器查看详情",
                        "JsonRPCAction": {
                            "method": "openUrl",
                            "parameters": ["https://translate.google.cn/#view=home&op=translate&sl={}&tl={}&text={}"
                                           .format(SL, TL, query)],
                            "dontHideAfterAction": False,
                        },
                    })

        # 设置
        else:
            conf = query.split()
            if conf[0] == "_config":
                f_json = get_list()

                flag = {}
                # 设置语言
                if (len(conf) == 4) and (conf[1] in f_json):
                    if f_json[conf[1]] != conf[3]:
                        if (set_lang(conf[1], conf[3])):
                            flag = {conf[1]: " (Successful)"}
                        else:
                            flag = {conf[1]: " (ERROR: Input not supported)"}

                for item in f_json.keys():
                    if item in flag:
                        if "Success" in flag[item]:
                            title = "{} = {}".format(item, conf[3])
                        else:
                            title = "{} = {}".format(item, f_json[item])
                        Title = title+flag[item]
                    else:
                        title = "{} = {}".format(item, f_json[item])
                        Title = title
                    results.append({
                        "IcoPath": ICO_PATH,
                        "Title": Title,
                        "SubTitle": "Set up {} (Modified directly in the input box)".format(item),
                        "JsonRPCAction": {
                            "method": "selectConfig",
                            "parameters": [title],
                            "dontHideAfterAction": True,
                        },
                    })

            else:
                results.append({
                    "IcoPath": ICO_PATH,
                    "Title": "_config",
                    "SubTitle": PREFIX_CONFIG + ": Set up Gtranslate",
                    "JsonRPCAction": {
                        "method": "openConfig",
                        "parameters": [],
                        "dontHideAfterAction": True,
                    },
                })

        return results

    def copy(self, ans):
        if flag_package:
            pyperclip.copy(ans)
        else:
            WoxAPI.change_query("tran ERROR: pyperclip is not installed", True)

    def openUrl(self, url):
        webbrowser.open(url)

    def openConfig(self):
        WoxAPI.change_query(PREFIX_CONFIG, True)

    def selectConfig(self, item):
        WoxAPI.change_query("{} {}".format(PREFIX_CONFIG, item), True)


if __name__ == "__main__":
    Gtranslate()
