# Wox.Plugin.Gtranslate
Wox Plugin Gtranslate. 
Call Google translation for fast translation between Chinese and English.

## install 
1. by wox (stable)
```
wpm install Gtranslate/谷歌翻译
```
2. by Github (newest, but may be some bugs)
    1. download or clone from:
    ```
    https://github.com/CN-DXTZ/Wox.Plugin.Gtranslate.git
    ```
    2. remove to:
    ```
    %USERPROFILE%\AppData\Local\Wox\app-1.3.524\Plugins\
    ```

## usage
![Gtranslate.gif](/Images/Gtranslate.gif)
1. input others language like en (english), translate to zh-CN (chinese)
2. input zh-CN , translate to en
3. you can click or enter to copy to your clipboard
4. for only one word or phrase (any language), it will provide the dictionary functions, specifically, it will append a list of translation sorted by part of speech

### dependence
You can use this plugin without any dependence completely, 
but you must install the python package pyperclip if you wang to copy to clipboard by one key,
for this, you can open your cmd or powershell, and then:
```
pip install pyperclip
```

### config
For other users different requirements, so provide a json config file and method for it
#### 默认配置
default json file as follows: 
```
{"My_Language": "zh-CN", "Obj_Language": "en"}
```
it means:
- 除`My_Language`外，任何语言翻译成`My_Language`
- `My_Language`翻译成`Obj_Language`

#### 修改方法
![Gtranslate.gif](/Images/config.gif)
<!-- ![config.gif](https://cdn.jsdelivr.net/gh/CN-DXTZ/Blog-Img-Bed/PicGo/config.gif) -->
- you can modify the config as the gif:
    1. input `tran _`
    2. then select or input completely: `tran _config` 
    3. there is a list of config you can selsect or input completely: `tran _config My_Language = zh-CN`
    4. modify the "=" left language code to what you requirement, it will prompt you the success or failure

- or you can edit config.json directly, the path as follows:
```
%USERPROFILE%\AppData\Local\Wox\app-1.3.524\Plugins\Wox.Plugin.Gtranslate\config.json
```