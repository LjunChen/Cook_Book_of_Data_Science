```cmd
pandoc -t beamer -V theme:CambridgeUS slides.md -o slides.pdf
```

利用markdown写文件，然后利用pandoc将其转化为slides

```cmd
pandoc -t beamer -V theme:CambridgeUS slides.md -o slides.tex
```

这个是将其变为latex源文件，然后可以方便修改主题等

但是这个有一个问题，不能输出作者和日期，有点尴尬

还有一个问题是对中文的支持可能不太好，得配置一下文件，具体的参见百度

```cmd
pandoc --pdf-engine=xelatex -t beamer -V theme:CambridgeUS slides.md -o slides.pdf
```

