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
