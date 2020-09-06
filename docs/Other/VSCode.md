# VScode配置
VScode是一款很好的代码编辑软件，当然市场上还有很多的编辑器也很好用。我个人的使用主要是VScode+Pycharm+ Vim+Notepad++.

Pycharm主要用来开发Python. 个人认为，Python的最好的编辑器还是Pycharm, 但是Pycharm太大了，并且有些功能需要专业版才能获取（比如远程开发功能，PS: 学生可以免费获得Pycharm的专业版).

Notepad++的优势在于启动非常快，对我来说，他主要是记事本的替代品，偶尔一些非常简单的任务可以用notepad++写.

Vim的使用是一件没办法的事情，总是会用到的，这玩意用起来太难了，但是没办法还是得用。

VScode 的一个好处是相对来说比较小，因此启动等方面比较快，而且可以按照自己的需求定制自己的开发环境。还有一个好处在于，我可以通过配置VScode来编写其他语言，因为我对这些也有需求，有时候会写R，C等语言，并且我经常用到Latex和markdown。
这里简要介绍一下我的VScode的配置。

## 基础配置

#### 语言配置
一般来说，默认安装VScode之后的默认语言是英文，我们这里将其改为中文。
直接通过快捷键`Crlt+Shift+P`打开命令窗口，然后在里面输入`configure display language`, 将语言改为`zh-ch`就可以了。

#### 主题配置

命令窗口输入`color theme`选择喜欢的主题既可，浅色和深色的主题都有。

## Python 开发配置
Python开发的第一个插件是`Python`插件, VScode安装插件的方法是输入`Crlt+Shift+X`调出插件目录，然后搜索插件名，进行安装。Python开发的第二个插件是 `Python for VSCode`。

一般来说，有了这两个插件，就可以愉快的进行Python的开发工作了。由于我特别喜欢交互式的运行Python（这个习惯可能是来源于之前学习R语言）。因此我对需要配置一下单行运行的模式，VScode的右键好像就有`在命令行运行选中/本行`，但是我右键点击可以，但是绑定的快捷键没用。（可能是bug?）

一个解决办法是安装好`macros`插件（这是必须的，不然下面的`macros`配置是没用的），
然后打开`settings.json`（打开命令面板后输入）, 在里面加上
```
"macros": {   
"pythonExecSelectionAndCursorDown": [
            "python.execSelectionInTerminal", 
            "cursorDown" ]
```
然后我们给这个绑定快捷键, 打开`keybindings.json`，输入
```
    {
        "key": "ctrl+enter",
        "command": "macros.pythonExecSelectionAndCursorDown",
        "when": "editorTextFocus && editorLangId == 'python'"
    },
```

现在我们在每行直接使用`Crlt+Enter`就可以运行本行的脚本了。




## R语言配置

## C语言配置

## Latex配置

## Markdown配置
我们可以使用文件右上角的按钮或者快捷键`Crlt+K V`来预览markdown文件，效果很好。
但是其原生不支持公式的预览，因此，我们可以需要安装`markdown math`插件。PS 我觉得VScode写markdown使用起来比Typora还要舒服，Typora很多时候总是有点卡。而且相比于Typora的展现形式，我还是更加喜欢source和预览是分开的这种，流畅度会好很多。
