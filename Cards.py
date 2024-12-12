from sqlalchemy import Column, Integer, String, Boolean, JSON, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)
    collectible = Column(Integer)
    slug = Column(String(255))
    class_id = Column(Integer)
    multi_class_ids = Column(JSON)
    minion_type_id = Column(Integer)
    card_type_id = Column(Integer)
    card_set_id = Column(Integer, primary_key=True)
    rarity_id = Column(Integer)
    artist_name = Column(String(255))
    health = Column(Integer)
    attack = Column(Integer)
    mana_cost = Column(Integer)
    name = Column(String(255))
    text = Column(Text)
    image = Column(String(255))
    image_gold = Column(String(255))
    flavor_text = Column(Text)
    crop_image = Column(String(255))
    child_ids = Column(JSON)
    is_zilliax_functional_module = Column(Boolean)
    is_zilliax_cosmetic_module = Column(Boolean)
    keyword_ids = Column(JSON)
    parent_id = Column(Integer, ForeignKey('cards.id'))

    # 定义关系，如果你需要的话
    # parent = relationship("Card", remote_side=[id])

# 如果你需要创建表，可以使用以下代码
from sqlalchemy import create_engine
engine = create_engine('sqlite:///cards.db')  # 这里使用 SQLite 作为示例，你需要根据实际情况调整
Base.metadata.create_all(engine)
