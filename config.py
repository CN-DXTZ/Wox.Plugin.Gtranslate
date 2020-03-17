import json


def get_lang(item):
    with open("config.json", "r") as f_obj:
        lang = json.load(f_obj)[item]
    return lang


def set_lang(item, lang):
    with open("config.json", "r") as f_obj:
        f_json = json.load(f_obj)
        f_json[item] = lang
    with open("config.json", "w") as f_obj:
        json.dump(f_json, f_obj)
    return True


if __name__ == "__main__":
    set_lang("My Language", "zh_CN")
    # print(get_lang("My Language"))
    # print(get_lang("Obj Language"))
