# -*- coding:utf-8 -*-
import urllib.request
import re
import requests
import io
from PIL import Image

index = 0


def get_html(url):
    """
    获取网页信息
    :param url:
    :return:
    """
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        return r.text
    except:
        return "失败"


def get_img(html):
    """
    网页信息选择,获取图片链接
    :param html:
    :return:
    """
    pattern = re.compile('<img src="(.*?)"', re.S)  # 正则表达式
    img_url = re.findall(pattern, html)
    for img in img_url:
        print(img)
    return img_url


def save_img(url, index, length, width):
    """
    保存图片
    :param url:
    :param index:
    :return:
    """
    u = urllib.request.urlopen(url)
    data = u.read()
    tmp_img = io.BytesIO(data)
    im = Image.open(tmp_img)
    shape = im.size
    if (shape[0] >= length) & (shape[1] >= width):  # 判断图片大小
        filename = str(index) + '.jpg'
        f = open(filename, 'wb')
        f.write(data)
        print(shape)
        print('成功存入')
        index += 1
        f.close()


if __name__ == '__main__':
    url = 'http://www.qq.com/'
    html = get_html(url)
    img_url = get_img(html)
    length = 100
    width = 70
    for url in img_url:
        save_img(url, index, length, width)
