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