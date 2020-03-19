# Wox.Plugin.Gtranslate

## install 
1. by wox (stable)
```
wpm install Gtranslate/谷歌翻译
```
2. by Github (newest, but may be some bugs)  
    download or clone from:
    ```
    https://github.com/CN-DXTZ/Wox.Plugin.Gtranslate.git
    ```
    remove to:
    ```
    %USERPROFILE%\AppData\Roaming\Wox\Plugins\
    ```

## usage
![Gtranslate.gif](/Images/Gtranslate.gif)
1. input others language (automatic recognition) like `en` (english), translate to `zh-CN` (chinese)
2. input `zh-CN` , translate to `en`
3. for only one word or phrase (any language), it will provide the dictionary functions, specifically, it will append a list of translation sorted by part of speech
4. you can one-lick to copy the translation to your clipboard
5. you can one-lick to open browser to view details of google translation search

### dependence
You can use this plugin without any dependence completely, 
but you must install the python package pyperclip if you wang to copy to clipboard by one key,
for this, you can open your cmd or powershell, and then:
```
pip install pyperclip
```

## customize

### config
Because of the wox plugin development with python is not provide to modify the settings in the main interface, so for other users different requirements, provide a json config file and method for it.

#### default config
default json file as follows: 
```
{"My_Language": "zh-CN", "Obj_Language": "en"}
```
it means:
- 除`My_Language`外，任何语言翻译成`My_Language`
- `My_Language`翻译成`Obj_Language`

#### modify config
![Gtranslate.gif](/Images/Gtranslate_config.gif)
<!-- <img src="https://cdn.jsdelivr.net/gh/CN-DXTZ/Blog-Img-Bed/PicGo/Gtranslate_config.gif" width = "720" align=center /> -->
- you can modify the config as the gif:
    1. input `tran _`
    2. then select or input completely: `tran _config` 
    3. there is a list of config you can selsect or input completely: `tran _config My_Language = zh-CN`
    4. modify the "=" left language code to what you requirement, it will prompt you the success or failure

- or you can edit config.json directly, the path as follows:
    1. open the folder: `%USERPROFILE%\AppData\Roaming\Wox\Plugins\`
    2. and then open the folder prefix with `Wox.Plugin.Gtranslate` (download or clone by git) or `Gtranslate_谷歌翻译` (install by wox)
    3. in the end, open the `config.json` and edit it

### custom development
if you want continue to develop based on this plugin, you can refenence to this article —— 
[开发 Wox.Plugin.Gtranslate](https://cn-dxtz.github.io/%E5%B7%A5%E5%85%B7%E9%85%8D%E7%BD%AE/Wox/%E5%BC%80%E5%8F%91%20Wox.Plugin.Gtranslate/)