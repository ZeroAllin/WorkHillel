from lxml import html
import requests
import re


def get_html(url):
    s = requests.Session()
    r = s.get(url)
    return html.fromstring(r.text)


def parse(html):
    div = html.xpath('//div[@id = "invisible"]')
    if len(div) < 1:
        print('Error div')
        return False

    div = div[0]

    pre = div.xpath('.//pre[@class = "data"]/text()')

    if len(pre) < 1:
        print('Error pre')
        return False

    pre = pre[0]

    return(pre.split())
 


def main():
    parse(get_html('https://www.random.org/integers/?num=10000&min=0&max=1&col=10&base=10&format=html&rnd=new'))


if __name__ == '__main__':
    main()

