# Vim的使用
我的vim使用的很少，大部分时候用VScode是比vim方便的，偶尔用到，一些基础的配置如下.
```
"编码"
set encoding=utf-8 
set termencoding=utf-8
set fileencoding=utf-8
set nocompatible "去除和vi的一致性"
set number "显示行号"
set cursorline "高亮当前行"

"启用鼠标"
set mouse=a 
set selection=exclusive
set selectmode=mouse,key
set showmatch "显示括号匹配"

"设置缩进"
set tabstop=4
set shiftwidth=4
set autoindent
set cindent

set paste   "粘贴"
set wrap	"代码折叠"
syntax on "语法高亮"
"设置搜索"
set incsearch
set hlsearch
set ignorecase
```