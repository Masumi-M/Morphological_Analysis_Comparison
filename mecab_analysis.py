import MeCab as mecab
import pickle
import numpy as np

with open("the_night_of_the_milky_way_train.pickle", mode="rb") as f:
    milky = pickle.load(f)

m_tagger = mecab.Tagger()
result = m_tagger.parse(milky)
print(result)

part_of_speech = '名詞'

noun_list = []
m_parse = m_tagger.parseToNode(milky)
while m_parse:
    if m_parse.feature.split(',')[0] == part_of_speech:
        noun_list.append(m_parse.surface)
    m_parse = m_parse.next

print(noun_list)
print(len(noun_list))
# ['みなさん', 'ふう', '川', '乳', 'あと', 'ぼんやり', 'もの', 'ほんとう', '何', '承知', '先生', '黒板', '星座', '図', '上', '下', '銀河', '帯', 'よう', 'ところ', 'みんな', '問', 'カムパネルラ', '手', 'それ', '四', '五', '人', '手', 'ジョバンニ', '手', 'あれ', 'みんな', '星', 'いつか', '雑誌', 'の', 'このごろ', 'ジョバンニ', '毎日', '教室', '本', 'ひま', '本' ...]
# 5895
