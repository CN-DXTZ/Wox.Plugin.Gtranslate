import json


def get_list():
    with open("config.json", "r") as f_obj:
        f_json = json.load(f_obj)
    return f_json


def get_lang(item):
    return get_list()[item]


def set_lang(item, lang):
    with open("list_lang.json", "r") as f_obj:
        list_lang = json.load(f_obj)
        if not (lang in list_lang):
            return False

    f_json = get_list()
    f_json[item] = lang
    with open("config.json", "w") as f_obj:
        json.dump(f_json, f_obj)
    return True


if __name__ == "__main__":
    print(get_list())
    print(get_lang("My_Language"))
    print(get_lang("Obj_Language"))
    print(set_lang("My_Language", "zh-CN"))
