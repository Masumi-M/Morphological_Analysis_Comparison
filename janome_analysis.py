from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
from janome.charfilter import *
import pickle

with open("the_night_of_the_milky_way_train.pickle", mode="rb") as f:
    milky = pickle.load(f)

t = Tokenizer()
for token in t.tokenize(milky):
    print(token)

part_of_speech = '名詞'

char_filters = [UnicodeNormalizeCharFilter(), RegexReplaceCharFilter(
    r"[IiⅠｉ?.*/~=()〝 <>:：《°!！!？（）-]+", "")]
token_filters = [POSKeepFilter([part_of_speech]), POSStopFilter(
    []), LowerCaseFilter()]
analyzer = Analyzer(char_filters, t, token_filters)

noun_list = [token.surface for token in analyzer.analyze(milky)]

print(noun_list)
print(len(noun_list))
# ['みなさん', 'ふう', '川', '乳', 'あと', 'ぼんやり', 'もの', 'ほんとう', '何', '承知', '先生', '黒板', '星座', '図', '上', '下', '銀河', '帯', 'よう', 'ところ', 'みんな', '問', 'カムパネルラ', '手', 'それ', '四', '五', '人', '手', 'ジョバンニ', '手', 'あれ', 'みんな', '星', 'いつか', '雑誌', 'の', 'このごろ', 'ジョバンニ', '毎日', '教室', '本', 'ひま', '本' ...]
# 5895
