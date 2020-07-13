## Gitbook

使用的过程中碰到一些问题，主要都是公式方面的

* 公式不能用是没有 mathjax/katex。建议使用katex (mathjax在生成html的时候还可以，但是导出成pdf的时候格式很模糊), 但是katex对模型latex语法不认识，得修改使其更符合规范。 在根目录下建立book.json, 然后在里面添加

  ```
    "plugins": [
        "mathjax"
      ],
  ```

  然后运行 

  ```
  gitbook install ./
  ```

  

* 行业公式需要用两个 '\$', 在markdown中好像两者是一样的，但是在编译成html或者pdf的时候，好像必须要 两个，原因不明

* 碰到 SVG 问题，使用

  ```
  npm install svgexport@0.3.2 -g
  ```

  直接 npm install svgexport -g 的话安装的是0.4的版本，但是有bug, 碰到了坑，所以用0.3.2

  在 npm 默认的源是官方源，是国外的，改成国内的

  ```
  npm config set registry https://registry.npm.taobao.org
  ```

  使用以下代码看目前自己所有的源

  ```
  npm config list
  ```

  如果安装出现问题，可以考虑使用 ``` npm cache clean --force``` 清除缓存，并将安装失败的项目中的**node_modules文件夹**删除，重新 ```npm install```
  
* gitbook 可以导出本地的html

  ```
  gitbook build
  ```

  但是导出的 html 不支持跳转， 具体原因是由于点击事件被js代码禁用，所以点击没有反应，但是如果右键，在新窗口/新标签页打开的话是可以跳转的。

  去 /_book/gitbook 目录下找到 `theme.js`文件, 搜索`if(m)for(n.handler&&`, 将`if(m)` 改为 `if(false)`

  正常还是用 `gitbook serve`方便

  

  

