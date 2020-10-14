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

#### 配置
Vscode的配置有两种，一种是通过json文件来配置，这种更灵活，但是很多的属性我们并不清楚，多靠百度。
另外一种可以手动配置。我们可以直接在命令窗口搜索，然后配置，或者直接右键插件，会出来配置选项。


#### Run Code
这是一个非常好的插件，可以很方便的执行很多常见语言的代码。
我将快捷键设置为`F5`.
但是这个插件有个问题，在于Python的版本，他选择的是默认的，而我在开发的时候大多选择的是Anaconda的虚拟环境。一个选择是在设置里面，将`Run-In-Terminal`选上。
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
          }
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
一般认为R语言最好的IDE是Rstudio,但是我个人不是特别喜欢Rstudio, 因为Rstudio无法定制我的界面，以及Rstudio无法远程开发。（其实就是不喜欢。）

不过 Rstudio Server倒是可以很不错的东西。

首先，我们安装`R`插件（R language Support). 但是仅仅这一个插件是不太够的，因为其本身的代码补全不是特别靠谱。我们还需要一个`R LSP Clinet`来帮助我们进行代码补全。但是仅仅安装这个插件是不行的，我们还需要在R端安装一个package.
```R
install.packages{"languageserver"}
```
另外`R`插件里面打开Session Watcher功能，非常好用，我们可以就可以在侧边栏预览`data.frame`以及一些画图的结果，而不会弹窗出来了，不过这个功能目前还在试验阶段，可能会有些bug.
R里面单行运行的快捷键默认就是`Crlt+Enter`，就不用修改了。

现在就可以愉快的在VScode里面使用R语言了。
不过貌似VScode不支持Rmarkdown, 这是目前的一个缺陷，不知道以后会不会改变。

## C语言配置
我的`gcc`解释器是用`cygwin`安装的。
直接使用`Run Code`就可以了。


## Latex配置
首先需要安装插件`Latex Workshop`. 当然texlive, SumatraPDF的安装是基础.

Latex的配置直接在setting区加上以下代码(记得软件的地址要改.)
```
  "latex-workshop.latex.recipes": [
    {
    "name": "pdflatex",
    "tools": [
          "pdflatex"
        ]
    },
    {
    "name": "xelatex",
    "tools": [
        "xelatex"
        ]
    },
    {
    "name": "lualatex",
    "tools": [
        "lualatex"
        ]
    },
    {
    "name": "bibTeX",
    "tools": [
        "bibtex"
        ]
    },
    {
    "name": "xelatex -> bibtex -> xelatex*2",
    "tools": [
          "xelatex",
          "bibtex",
          "xelatex",
          "xelatex"
        ]
    },
    {
    "name": "pdflatex -> bibtex -> pdflatex*2",
    "tools": [
        "pdflatex",
        "bibtex",
        "pdflatex",
        "pdflatex"
        ]
    }
    ],
    "latex-workshop.latex.tools": [
    {
    "name": "xelatex",
    "command": "xelatex",
    "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
        ]
    },
    {
    "name": "pdflatex",
    "command": "pdflatex",
    "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
        ]
    },
    {
    "name": "lualatex",
    "command": "lualatex",
    "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
        ]
    },
    {
    "name": "bibtex",
    "command": "bibtex",
    "args": [
        "%DOCFILE%"
        ]
    }],
    "latex-workshop.view.pdf.viewer": "external",
    "latex-workshop.view.pdf.external.viewer.command": "C:/Software/sumutrapdf/SumatraPDF/SumatraPDF.exe",
    "latex-workshop.view.pdf.external.viewer.args": [
        "-forward-search",
        "%TEX%",
        "%LINE%",
        "-reuse-instance",
        "-inverse-search",
        "\"D:/Software/VScode/Microsoft VS Code/Code.exe\" \"D:/Software/VScode/Microsoft VS Code/resources/app/out/cli.js\" -gr \"%f\":\"%l\"",
        "%PDF%"
    ],

    "latex-workshop.view.pdf.external.synctex.command": "C:/Software/sumutrapdf/SumatraPDF/SumatraPDF.exe",
    "latex-workshop.view.pdf.external.synctex.args": [
        "-forward-search",
        "%TEX%",
        "%LINE%",
        "-reuse-instance",
        "-inverse-search",
        "code \"D:/Software/VScode/Microsoft VS Code/resources/app/out/cli.js\" -gr \"%f\":\"%l\"",
        "%PDF%",
    ],
    "latex-workshop.latex.clean.fileTypes": [
    "*.aux",
    "*.bbl",
    "*.blg",
    "*.idx",
    "*.ind",
    "*.lof",
    "*.lot",
    "*.out",
    "*.toc",
    "*.acn",
    "*.acr",
    "*.alg",
    "*.glg",
    "*.glo",
    "*.gls",
    "*.ist",
    "*.fls",
    "*.log",
    "*.nav",
    "*.snm",
    "*.vrb",
    "*.fdb_latexmk"
    ],
    "latex-workshop.message.warning.show": false,
```


## Markdown配置
我们可以使用文件右上角的按钮或者快捷键`Crlt+K V`来预览markdown文件，效果很好。
如果想要更好的预览效果，可以使用`Markdown Preview Enhanced`插件。
但是其原生不支持公式的预览，因此，我们可以需要安装`markdown math`插件。PS 我觉得VScode写markdown使用起来比Typora还要舒服，Typora很多时候总是有点卡。而且相比于Typora的展现形式，我还是更加喜欢source和预览是分开的这种，流畅度会好很多。


## 用户片段
#### latex.json: 定义了beamer,ctexbeamer和paper的常用命令
```json
{
	"beamer":{
		"prefix":"beamer",
		"body":[
			"%!TEX program =pdflatex",
			"\\documentclass{beamer}",
			"\\usetheme{CambridgeUS}",
			"%%define new comand",
			"\\def\\argmin{\\mathop{\\rm arg~min}\\limits}", 
			"\\def\\argmin{\\mathop{\\rm arg~min}\\limits}", 
			"\newcommand{\bbeta}{\boldsymbol{\beta}}", 
			"\\newcommand{\\bdelta}{\\boldsymbol{\\delta}}", 
			"\\newcommand{\\bSigma}{\\boldsymbol{\\Sigma}}",
			"\\newcommand{\\brho}{\\displaystyle{\\large{\\boldsymbol{\\rho}}}}", 
			"\\newcommand{\\bgamma}{\\boldsymbol{\\gamma}}", 
			"\\newcommand{\\bfeta}{\\boldsymbol{\\eta}}", 
			"\\newcommand{\\bPsi}{\\boldsymbol{\\Psi}}", 
			"\\newcommand{\\bmu}{\\boldsymbol{\\mu}}", 
			"\\newcommand{\\bvartheta}{\\boldsymbol{\\vartheta}}",
			"\\newcommand{\\bzero}{\\mathbf{0}}",
			"\\newcommand{\\bone}{\\mathbf{1}}", 
			"\\newcommand{\\bA}{\\mathbf{A}}", 
			"\\newcommand{\\ba}{\\mathbf{a}}", 
			"\\newcommand{\\bB}{\\mathbf{B}}", 
			"\\newcommand{\\bb}{\\mathbf{b}}", 
			"\\newcommand{\\bD}{\\mathbf{D}}", 
			"\\newcommand{\\bU}{\\mathbf{U}}", 
			"\\newcommand{\\bu}{\\mathbf{u}}",
			"\\newcommand{\\bV}{\\mathbf{V}}", 
			"\\newcommand{\\bW}{\\mathbf{W}}", 
			"\\newcommand{\\bw}{\\mathbf{w}}", 
			"\\newcommand{\\bX}{\\mathbf{X}}", 
			"\\newcommand{\\bx}{\\mathbf{x}}", 
			"\\newcommand{\\bY}{\\mathbf{Y}}", 
			"\\newcommand{\\by}{\\mathbf{y}}", 
			"\\newcommand{\\bZ}{\\mathbf{Z}}", 
			"\\newcommand{\\bz}{\\mathbf{z}}",
			"\\newcommand{\\suit}[1]{\\left(#1\\right)}",
			"\\newcommand{\\abs}[1]{\\left\\vert#1\\right\\vert}",
			"\\newcommand{\\set}[1]{\\left\\{#1\\right\\}}",
			"\\newcommand{\\msuit}[1]{\\left[ #1 \\right]}",
			"\\author{Liujun Chen}",
			"\\title{}",
			"\\begin{document}",
			"\\begin{frame}",
				"\\titlepage",
			"\\end{frame}",
			"\\end{document}"
	],
	"description": "beamer header"
	},
	"ctexbeamer":{
		"prefix":"ctexbeamer",
		"body":[
			"%!TEX program =xelatex",
			"\\documentclass{ctexbeamer}",
			"\\usetheme{CambridgeUS}",
			"%%define new comand",
			"\\def\\argmin{\\mathop{\\rm arg~min}\\limits}", 
			"\\def\\argmin{\\mathop{\\rm arg~min}\\limits}", 
			"\newcommand{\bbeta}{\boldsymbol{\beta}}", 
			"\\newcommand{\\bdelta}{\\boldsymbol{\\delta}}", 
			"\\newcommand{\\bSigma}{\\boldsymbol{\\Sigma}}",
			"\\newcommand{\\brho}{\\displaystyle{\\large{\\boldsymbol{\\rho}}}}", 
			"\\newcommand{\\bgamma}{\\boldsymbol{\\gamma}}", 
			"\\newcommand{\\bfeta}{\\boldsymbol{\\eta}}", 
			"\\newcommand{\\bPsi}{\\boldsymbol{\\Psi}}", 
			"\\newcommand{\\bmu}{\\boldsymbol{\\mu}}", 
			"\\newcommand{\\bvartheta}{\\boldsymbol{\\vartheta}}",
			"\\newcommand{\\bzero}{\\mathbf{0}}",
			"\\newcommand{\\bone}{\\mathbf{1}}", 
			"\\newcommand{\\bA}{\\mathbf{A}}", 
			"\\newcommand{\\ba}{\\mathbf{a}}", 
			"\\newcommand{\\bB}{\\mathbf{B}}", 
			"\\newcommand{\\bb}{\\mathbf{b}}", 
			"\\newcommand{\\bD}{\\mathbf{D}}", 
			"\\newcommand{\\bU}{\\mathbf{U}}", 
			"\\newcommand{\\bu}{\\mathbf{u}}",
			"\\newcommand{\\bV}{\\mathbf{V}}", 
			"\\newcommand{\\bW}{\\mathbf{W}}", 
			"\\newcommand{\\bw}{\\mathbf{w}}", 
			"\\newcommand{\\bX}{\\mathbf{X}}", 
			"\\newcommand{\\bx}{\\mathbf{x}}", 
			"\\newcommand{\\bY}{\\mathbf{Y}}", 
			"\\newcommand{\\by}{\\mathbf{y}}", 
			"\\newcommand{\\bZ}{\\mathbf{Z}}", 
			"\\newcommand{\\bz}{\\mathbf{z}}",
			"\\newcommand{\\suit}[1]{\\left(#1\\right)}",
			"\\newcommand{\\abs}[1]{\\left\\vert#1\\right\\vert}",
			"\\newcommand{\\set}[1]{\\left\\{#1\\right\\}}",
			"\\newcommand{\\msuit}[1]{\\left[ #1 \\right]}",
			"\\author{Liujun Chen}",
			"\\title{}",
			"\\begin{document}",
			"\\begin{frame}",
				"\\titlepage",
			"\\end{frame}",
			"\\end{document}"
	],
	"description": "beamer header"
	},
	"paper":{
		"prefix": "paper",
		"body": [
			"%!TEX program = pdflatex",
			"%!BIB program = bibtex",
			"\\documentclass[12pt]{article}",

			"%%Package",
			"\\usepackage{amsmath,amsthm,amssymb}",
			"\\usepackage{color}",
			"\\usepackage{graphicx,subfigure,float}",
			"\\usepackage[round]{natbib}",

			"%%theorem style",
			"\\theoremstyle{remark}",
			"\\newtheorem{theorem}{{\\sc Theorem}}",
			"\\newtheorem{prop}{Proposition}[section]",
			"\\newtheorem{corollary}{{\\sc Corollary}}",
			"\\newtheorem{lemma}{{\\sc Lemma}}",
			"\\newtheorem{remark}{{\\sc Remark}}",
			"\\newtheorem{exam}{{\\sc Example}}",

			"\numberwithin{equation}{section}",
			"\numberwithin{theorem}{section}",
			"\numberwithin{lemma}{section}",
			"\numberwithin{corollary}{section}",
			"\numberwithin{remark}{section}",
			"\numberwithin{exam}{section}",

			"%% define of comment",
			"\\def\\boxit#1{\\vbox{\\hrule\\hbox{\\vrule\\kern6pt\\vbox{\\kern6pt#1\\kern6pt}\\kern6pt\\vrule}\\hrule}}",
			"\\def\\chencomment#1{\\vskip 2mm\\boxit{\\vskip 2mm{\\color{blue}\\bf#1} {\\color{red}\\bf -- Liujun\\vskip 2mm}}\\vskip 2mm}",


			"%%define new comand",
			"\\def\\argmin{\\mathop{\\rm arg~min}\\limits}", 
			"\\def\\argmin{\\mathop{\\rm arg~min}\\limits}", 
			"\newcommand{\bbeta}{\boldsymbol{\beta}}", 
			"\\newcommand{\\bdelta}{\\boldsymbol{\\delta}}", 
			"\\newcommand{\\bSigma}{\\boldsymbol{\\Sigma}}",
			"\\newcommand{\\brho}{\\displaystyle{\\large{\\boldsymbol{\\rho}}}}", 
			"\\newcommand{\\bgamma}{\\boldsymbol{\\gamma}}", 
			"\\newcommand{\\bfeta}{\\boldsymbol{\\eta}}", 
			"\\newcommand{\\bPsi}{\\boldsymbol{\\Psi}}", 
			"\\newcommand{\\bmu}{\\boldsymbol{\\mu}}", 
			"\\newcommand{\\bvartheta}{\\boldsymbol{\\vartheta}}",
			"\\newcommand{\\bzero}{\\mathbf{0}}",
			"\\newcommand{\\bone}{\\mathbf{1}}", 
			"\\newcommand{\\bA}{\\mathbf{A}}", 
			"\\newcommand{\\ba}{\\mathbf{a}}", 
			"\\newcommand{\\bB}{\\mathbf{B}}", 
			"\\newcommand{\\bb}{\\mathbf{b}}", 
			"\\newcommand{\\bD}{\\mathbf{D}}", 
			"\\newcommand{\\bU}{\\mathbf{U}}", 
			"\\newcommand{\\bu}{\\mathbf{u}}",
			"\\newcommand{\\bV}{\\mathbf{V}}", 
			"\\newcommand{\\bW}{\\mathbf{W}}", 
			"\\newcommand{\\bw}{\\mathbf{w}}", 
			"\\newcommand{\\bX}{\\mathbf{X}}", 
			"\\newcommand{\\bx}{\\mathbf{x}}", 
			"\\newcommand{\\bY}{\\mathbf{Y}}", 
			"\\newcommand{\\by}{\\mathbf{y}}", 
			"\\newcommand{\\bZ}{\\mathbf{Z}}", 
			"\\newcommand{\\bz}{\\mathbf{z}}",
			"\\newcommand{\\suit}[1]{\\left(#1\\right)}",
			"\\newcommand{\\abs}[1]{\\left\\vert#1\\right\\vert}",
			"\\newcommand{\\set}[1]{\\left\\{#1\\right\\}}",
			"\\newcommand{\\msuit}[1]{\\left[ #1 \\right]}",
			"\\begin{document}", 


			" %% Title information",
			"\\begin{center}",

				"{\\LARGE ****}", 
				"\\bigskip\\ \\\\ \\",
				"Liujun Chen",
				
			"version: *****",
			"\\end{center}", 


			"%% Abstract information and keywords", 
			"\\begin{abstract}", 
			"********",
			"\\end{abstract}", 
			"\\noindent {\\it Keywords: ***, ***, *** }",
			"$1", 
			"\\end{document}",
		],
	"description": "paper header"
	},
	"frame":{
		"prefix":"frame",
		"body": [
			"\\begin{frame}",
			"$1",
			"\\end{frame}"
		]
	}
}


```


#### Python.json

```json
{
	// Place your snippets for python here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"header":{
		"prefix": "header",
		"body": [
			"#author=Liujun Chen",
			"#create time $CURRENT_YEAR-$CURRENT_MONTH-$CURRENT_DATE $CURRENT_HOUR:$CURRENT_MINUTE:$CURRENT_SECOND",
		]
	}
}
```