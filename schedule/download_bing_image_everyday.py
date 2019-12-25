import requests
from urllib.parse import urlsplit, urlparse, parse_qs
from pathlib import Path
import pickle
import logging
from shutil import copyfile
import settings
import datetime
import sys

d = {"cnt": 0}
last_img_uri = ""
logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    filename="img_everyday.log",
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )


def get_img2():
    r = requests.get(
        'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1')  # "https://bing.ioliu.cn/v1/?type=json")
    rjson = r.json()
    print(rjson)
    img_url = rjson["data"]["url"]

    r = requests.get(img_url)

    r1 = urlsplit(img_url)

    file_name = Path(r1.path).name
    Path(file_name).write_bytes(r.content)

    print("""=================================""")
    print(f"I save the num {d['cnt']} {file_name}")
    with open("dat.plk", "rb") as f:
        pickle.load(f)
        d["cnt"] += 1
    with open("dat.plk", "wb") as f:
        pickle.dump(d, f)


def get_img():
    global last_img_name
    file_name = ""
    save_uri = lambda: settings.SAVE_IMG_PATH + file_name
    r = requests.get(
        'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1')  # "https://bing.ioliu.cn/v1/?type=json")
    rjson = r.json()
    print(rjson)
    img_url = "https://cn.bing.com" + rjson["images"][0]["url"]

    r = requests.get(img_url)

    r1 = urlsplit(img_url)
    d_url_query = parse_qs(r1.query)
    # file_name = Path(r1.path).name
    file_name = d_url_query.get("id")[0]
    Path(save_uri()).write_bytes(r.content)

    print("""=================================""")
    logging.info(f"I save the num {d['cnt']} {file_name}")
    last_img_name = save_uri()
    with open("dat.plk", "rb") as f:
        pickle.load(f)
        d["cnt"] += 1
    with open("dat.plk", "wb") as f:
        pickle.dump(d, f)


def copy_img_to_path():
    copyfile(Path(last_img_name), settings.UPDATE_BANNER_IMG)


import schedule
import time


def job(message='stuff'):
    print("I'm working on:", message)


# schedule.every().day.at("13:30").do(get_img)


if __name__ == '__main__':
    # img_url= """'https://cn.bing.com/th?id=OHR.ReindeerNorway_ZH-CN5913190372_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp'"""
    # r1 = urlparse(img_url)
    # d = parse_qs(r1.query)
    # file_name = Path( d.get("id")[0]).name

    logging.info("start")
    try:
        with open("dat.plk", "rb") as f:
            d = pickle.load(f)
            print(d)
    except IOError:
        with open("dat.plk", "wb") as f:
            pickle.dump(d, f)
    get_img()
    copy_img_to_path()
    schedule.every().day.at("21:00").do(get_img)
    schedule.every().day.at("20:00").do(copy_img_to_path)
    # schedule.every(10).seconds.do(get_img)
    while True:
        schedule.run_pending()
        time.sleep(1)

""""images":[
        {
            "startdate":"20191117",
            "fullstartdate":"201911171600",
            "enddate":"20191118",
            "url":"/th?id=OHR.IchetuckneeRiver_ZH-CN1410417151_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp",
            "urlbase":"/th?id=OHR.IchetuckneeRiver_ZH-CN1410417151",
            "copyright":"Ichetucknee河的海牛，佛罗里达州 (© Jennifer Adler/Alamy)",
            "copyrightlink":"https://www.bing.com/search?q=%E6%B5%B7%E7%89%9B&form=hpcapt&mkt=zh-cn",
            "title":"",
            "quiz":"/search?q=Bing+homepage+quiz&filters=WQOskey:%22HPQuiz_20191117_IchetuckneeRiver%22&FORM=HPQUIZ",
            "wp":true,
            "hsh":"6c56b082c03f064000b6673b6825a2ee",
            "drk":1,
            "top":1,
            "bot":1,
            "hs":[

            ]
        }
    ],
    "tooltips":{
        "loading":"正在加载...",
        "previous":"上一个图像",
        "next":"下一个图像",
        "walle":"此图片不能下载用作壁纸。",
        "walls":"下载今日美图。仅限用作桌面壁纸。"
    }
}"""
