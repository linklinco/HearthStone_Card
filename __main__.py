import time
import requests
import os
import json
import urllib.request


class form():
    def __init__(self, cardClass, p=1, stand=0):
        self.cardClass = cardClass
        self.p = p
        self.standard = stand
        self.totalCard = []

    def now_timec(self):
        return int(round(time.time() * 1000))

    def get_all(self):
        all_num = self.get_url()
        for i in range(2, all_num+1):
            self.p = i
            self.get_url()

    def get_url(self):
        data = {
            "cardClass": self.cardClass,
            "p": self.p,
            "standard": self.standard,
            "keywords": "",
            "t": self.now_timec()
        }
        header = {
            "Host": "hs.blizzard.cn",
            "Proxy-Connection": "keep-alive",
            "Content-Length": "56",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Origin": "http://hs.blizzard.cn",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
            "DNT": "1",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "http://hs.blizzard.cn/cards/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        url = "https://webapi.blizzard.cn/hs-cards-api-server/api//web/cards/constructed"
        response = requests.post(url, data, headers=header)
        cards = response.json()['cards']
        pagesize = response.json()['totalPage']
        for card in cards:
            des = {}
            des['花费'] = card['cost']
            des['卡名'] = card['name']
            des['稀有程度'] = card['cardRarity']
            des['拓展包'] = card['cardSet']
            des['卡牌类型'] = card['cardType']
            des['卡牌背景'] = card['background']
            des['卡牌描述'] = card['description']
            des['卡牌链接'] = card['imageUrl'].strip('\n')
            self.totalCard.append(des)
        return pagesize


if __name__ == "__main__":
    cardClass = ["druid", "hunter", "mage", "neutral", "paladin",
                 "priest", "rogue", "shaman", "warlock", "warrior"]
    for i in cardClass:
        a = form(i)
        a.get_all()
        tc = a.totalCard
        # 创建文件夹保存图片
        os.mkdir(i)
        for j in tc:
            path = '%s\\%s.png' % (i, j['卡名'])
            data = urllib.request.urlopen(j['卡牌链接'])
            with open(path, 'wb') as f1:
                f1.write(data.read())
        data = json.dumps(a.totalCard, ensure_ascii=False)
        with open(i+'\\'+i+'.json', 'w', encoding='utf8') as f:
            f.write(data)
