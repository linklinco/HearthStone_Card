import requests
from pprint import pprint as print
import pymongo
import time
from tqdm import tqdm
import json



def write_list_to_json(lst, filename):
    with open(filename, 'w+',encoding='utf8') as json_file:
        json.dump(lst, json_file,ensure_ascii=False)



def getAllCards(page: int = 1):
    url = "https://webapi.blizzard.cn/hs-cards-api-server/api//web/cards/constructed"

    payload = {
        "page": page,
        "page_size": 200,
        "class": "all",
        "mana_cost": [],
        "set": "wild",
        "text_filter": ""
    }
    print(page)
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6",
        "content-type": "application/json",
        "Cache-Control": "no-cache",
        "dnt": "1",
        "origin": "https://hs.blizzard.cn",
        "priority": "u=1, i",
        "referer": "https://hs.blizzard.cn/",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    cards = response.json()
    cards_data = cards['data']['list']

    with open(str(page)+'.json', 'w+',encoding='utf8') as json_file:
        json.dump(cards_data, json_file,ensure_ascii=False)
    global all_cards
    for card in cards_data:
        all_cards.append(card)
    return cards['data']['total']


# 假设这是另一个文件，比如 main.py

# # 导入必要的模块
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from Cards import Card  # 假设 Cards.py 是你定义 Card 类的文件

# # 创建数据库引擎
# engine = create_engine('sqlite:///cards.db')  # 使用与 Cards.py 中相同的数据库连接字符串

# # 创建会话
# Session = sessionmaker(bind=engine)
# session = Session()

# # 现在你可以使用 session 进行各种数据库操作
# # 例如，插入一条新记录
# new_card = Card(
#     collectible=1,
#     slug='sample-card',
#     class_id=1,
#     multi_class_ids=None,
#     minion_type_id=1,
#     card_type_id=1,
#     card_set_id=1,
#     rarity_id=1,
#     artist_name='Sample Artist',
#     health=5,
#     attack=2,
#     mana_cost=3,
#     name='Sample Card',
#     text='This is a sample card.',
#     image='sample.jpg',
#     image_gold='sample_gold.jpg',
#     flavor_text='This card is a sample.'
# )

# # 将新记录添加到会话中
# session.add(new_card)

# # 提交会话以保存更改
# session.commit()

# # 关闭会话
# session.close()



if __name__ == '__main__':
    all_cards = []
    cards_num = getAllCards()
    print("获取到{}张卡牌".format(cards_num))

    # for item in tqdm(range(2, int(cards_num/200)+1)):
    for item in range(2, 27):
        # time.sleep(1)
        print("正在获取第{}页".format(item))
        print(len(all_cards))
        getAllCards(item)


# #     # 连接到本地MongoDB数据库
    client = pymongo.MongoClient("mongodb://localhost:27017/")

# #     # 选择数据库
    db = client["HeartStoneCards"]

# #     # 选择集合
    collection = db["Cards"]

#     # # 插入一个文档
    document = {
        "cards": all_cards
    }

    collection.insert_one(document)

#     # 查询所有文档
    # documents = collection.find()
    # for document in documents:
    #     all_cards = document['cards']

    # # # 创建数据库引擎
    # engine = create_engine('sqlite:///cards.db')  # 使用与 Cards.py 中相同的数据库连接字符串

    # # # 创建会话
    # Session = sessionmaker(bind=engine)
    # session = Session()

    # 打印查询结果
    # for card in tqdm(all_cards):
    #     # print(card)
    #     new_card = Card(
    #         id=card['id'],
    #         collectible=card['collectible'],
    #         slug=card['slug'],
    #         class_id=card['class_id'],
    #         multi_class_ids=card['multi_class_ids'],
    #         minion_type_id=card['minion_type_id'],
    #         card_type_id=card['card_type_id'],
    #         card_set_id=card['card_set_id'],
    #         rarity_id=card['rarity_id'],
    #         artist_name=card['artist_name'],
    #         health=card['health'],
    #         attack=card['attack'],
    #         mana_cost=card['mana_cost'],
    #         name=card['name'],
    #         text=card['text'],
    #         image=card['image'],
    #         image_gold=card['image_gold'],
    #         flavor_text=card['flavor_text'],
    #         crop_image=card['crop_image'],
    #         child_ids=card['child_ids'],
    #         is_zilliax_functional_module=card['is_zilliax_functional_module'],
    #         is_zilliax_cosmetic_module=card['is_zilliax_cosmetic_module'],
    #         keyword_ids=card['keyword_ids'],
    #         parent_id=card['parent_id']
    #     )
    #     # # 将新记录添加到会话中
    #     session.add(new_card)

    #     # # 提交会话以保存更改
    #     session.commit()

    # # 关闭会话
    # session.close()

#     # 关闭连接
    client.close()
    # 示例列表

    # 将列表写入 JSON 文件
    write_list_to_json(all_cards, 'my_list.json')




