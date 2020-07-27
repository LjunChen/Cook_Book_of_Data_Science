# 爬虫

### Beautiful Soup库的使用

Beautiful Soup 是目前最为流行的爬虫工具，在我看来也是最好的爬虫方法。另外一个比较流行的爬虫框架是Scrapy。  Scrapy 是一个完整的爬虫框架，而 Beautiful Soup 实际上只能算是一个 html 的解析库。Scrapy 很强大，但是相对比较复杂（其实了解一下也不复杂）。但是就我而言，平时需要的爬虫需求，BeautifulSoup 就完全能满足。



#### find()和findAll()

BeautifulSoup 里面的 find 和 findAll() 应该是最常用的两个函数。，BeautifulSoup 文档里两者的定义就是这样：

```python
findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)
```

大部分时间里，我们都只需要用到前两个参数: `tag`和`attributes`. 

* 标签参数 `tag` : 可以传入一个标签的名称或者多个标签名称做标签参数，例如下面的代码将返回一个包含所有标题的列表

  `.findAll({'h1','h2','h3','h4','h5','h6'})`

* 属性参数attributes 是用一个Python 字典封装一个标签的若干属性和对应的属性值。例如，

  ```
  .findAll("span", {"class":{"green", "red"}})
  ```

  将返回红色/绿色的 span标签

* 其他参数的使用可以百度

#### 标签

* 子标签 `.children()` 和后代标签 `.descendants()`是不同的，后代标签包括子标签（子，孙，..., 都属于后代标签）
* 兄弟标签，`next_siblings()` 和 `previous_sibling()`, 当然，还有 `next_sibling` 和`previous_sibling` 函数
* 父标签, `.parent()` 一般不常用，大部分时候，我们都是从上而下的处理，而不是从下而上。





案例1：

中国大学的排名：[http://www.zuihaodaxue.cn/zuihaodaxuepaiming-zongbang-2020.html](http://www.zuihaodaxue.cn/zuihaodaxuepaiming-zongbang-2020.html) 

这个例子相对比较简单

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def fillUnivList(html):
    soup = BeautifulSoup(html, 'html.parser')
    col = ['排名', '大学名称', '总分']
    result = pd.DataFrame(columns=col)
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            values = [tds[0].string, tds[1].string, tds[3].string]
            temp = pd.Series({col[i]: values[i] for i in range(3)})
            result = result.append(temp, ignore_index=True)
    return result


if __name__ == '__main__':
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2020.html'
    html = getHTMLText(url)
    result = fillUnivList(html)
    print(result)

```



#### 案例2：

空气质量数据 https://www.aqistudy.cn/historydata/

这个网站是反爬虫的，对chrome的请求是直接拒绝的（哪怕是headless的chrome好像也是不行，不知道其他的浏览器可不可以，比如firefox，不过我没试过）。这里采用的是 `selenium+phantomjs`, 不过目前好像`selenium`慢慢不支持`phantomjs`了，如果不行的话，就不要装最新版本的`selenium'.

以下脚本爬取上海，北京，武汉，长沙, 重庆 这5个城市的2020年1月的空气质量数据（注意不同的网址的区别，略微有点怪，值得注意）。

```python
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

def get_HTML(driver,url):
    driver.get(url)
    html = driver.page_source
    text = BeautifulSoup(html, "html.parser")
    return text

def html_parser(city,text):
    data = text.find_all('tr')
    col=['日期','AQI','质量等级','PM2.5','PM10','SO2','CO','NO2','O3_8h']
    df=pd.DataFrame(columns=col)
    for tr in data:
        ltd = tr.find_all('td')
        values=[]
        for td in ltd:
            values.append(td.string)
        if len(values)>0:
            temp = pd.Series({col[i]: values[i] for i in range(len(col))})
            df = df.append(temp, ignore_index=True)
    df['city']=city
    return df

def main():
    driver = webdriver.PhantomJS('D:\\Software\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    city_list = ['上海', '北京', '武汉', '安庆', '长沙', '重庆']
    df = pd.DataFrame()
    for city in city_list:
        url = 'https://www.aqistudy.cn/historydata/daydata.php?city=' + urllib.request.quote(city) + '&month=202001'
        text=get_HTML(driver,url)
        temp_df = html_parser(city,text)
        df=pd.concat([df,temp_df])
    return df

if __name__ == '__main__':
    df = main()
    print(df.city.unique())
    print(df.shape)
```

