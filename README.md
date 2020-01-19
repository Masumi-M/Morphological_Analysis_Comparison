# Morphological_Analysis_Comparison

=====

## Description
This repository analysis the story of "The Night of the Milky Way Train" by using morphological analysis (NLP).<br>
It uses two tools, which are "[MeCab](https://taku910.github.io/mecab/)" and "[Janome](https://mocobeta.github.io/janome/)" . <br>
After analyzing the text, it compares the quality of each tool.

## Environment

| Type          | Version               |
| ------------- | --------------------- |
| OS            | macOS Mojave v10.14.6 |
| python        | v3.7.3                |
| mecab-python3 | v0.996.3              |
| janome        | v0.3.10               |

## Code Explanation

### 1. Import Text

```python
with open("the_night_of_the_milky_way_train.txt", mode="r", encoding="utf-8") as f:
    milky_original = f.read()

print(milky_original)

# Output
# 「ではみなさんは、そういうふうに川だと云《い》われたり、乳の流れたあとだと云われたりしていたこのぼんやりと白いものがほんとうは何かご承知ですか。」先生は、黒板に吊《つる》した大きな黒い星座の図の、上から下へ白くけぶった銀河帯のようなところを指《さ》しながら、みんなに問《とい》をかけました。
#　カムパネルラが手をあげました。それから四五人手をあげました。ジョバンニも手をあげようとして、急いでそのままやめました。たしかにあれがみんな星だと、いつか雑誌で読んだのでしたが、このごろはジョバンニはまるで毎日教室でもねむく、本を読むひまも読む本もないので、なんだかどんなこともよくわからないという気持ちがするのでした。
#　ところが先生...
```

### 2. Preprocessing Text

```python
import re

with open("the_night_of_the_milky_way_train.txt", mode="r", encoding="utf-8") as f:
    milky_original = f.read()

milky = re.sub("《[^》]+》", "", milky_original)
milky = re.sub("［[^］]+］", "", milky)
milky = re.sub("[｜ 　「」\n]", "", milky)

print(milky)

# Output
# ではみなさんは、そういうふうに川だと云われたり、乳の流れたあとだと云われたりしていたこのぼんやりと白いものがほんとうは何かご承知ですか。先生は、黒板に吊した大きな黒い星座の図の、上から下へ白くけぶった銀河帯のようなところを指しながら、みんなに問をかけました。カムパネルラが手をあげました。それから四五人手をあげました。ジョバンニも手をあげようとして、急いでそのままやめました。たしかにあれがみんな星だと、いつか雑誌で読んだのでしたが、このごろはジョバンニはまるで毎日教室でもねむく、本を読むひまも読む本もないので、なんだかどんなこともよくわからないという気持ちがするのでした。ところが先生は...
```

### 3. Create Pickle

```python
import re
import pickle

with open("the_night_of_the_milky_way_train.txt", mode="r", encoding="utf-8") as f:
    milky_original = f.read()

milky = re.sub("《[^》]+》", "", milky_original)
milky = re.sub("［[^］]+］", "", milky)
milky = re.sub("[｜ 　「」\n]", "", milky)

with open("the_night_of_the_milky_way_train.pickle", mode="wb") as f:
    pickle.dump(milky, f)

```

### 4. MeCab

#### Simple MeCab

```python
import MeCab as mecab
import pickle

with open("the_night_of_the_milky_way_train.pickle", mode="rb") as f:
    milky = pickle.load(f)

m_tagger = mecab.Tagger()
result = m_tagger.parse(milky)
print(result)

# Output
# では			接続詞, *, *, *, *, *, では, デハ, デワ
# みなさん	名詞, 代名詞, 一般, *, *, *, みなさん, ミナサン, ミナサン
# は				助詞, 係助詞, *, *, *, *, は, ハ, ワ
# 、				記号, 読点, *, *, *, *, 、, 、, 、
# そういう	連体詞, *, *, *, *, *, そういう, ソウイウ, ソーユウ
# ふう			名詞, 非自立, 形容動詞語幹, *, *, *, ふう, フウ, フー
# に				助詞, 副詞化, *, *, *, *, に, ニ, ニ
# 川				名詞, 一般, *, *, *, *, 川, カワ, カワ
# だ				助動詞, *, *, *, 特殊・ダ, 基本形, だ, ダ, ダ
# と				助詞, 格助詞, 引用, *, *, *, と, ト, ト
# 云わ			動詞, 自立, *, *, 五段・ワ行促音便, 未然形, 云う, イワ, イワ
# れ				動詞, 接尾, *, *, 一段, 連用形, れる, レ, レ
# たり			助詞, 並立助詞, *, *, *, *, たり, タリ, タリ
# 、				記号, 読点, *, *, *, *, 、, 、, 、
# ...
```

#### Part-of-Speech MeCab

```python
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
```

### 5. Janome

#### Simple Janome

```python
import pickle
from janome.tokenizer import Tokenizer

with open("the_night_of_the_milky_way_train.pickle", mode="rb") as f:
    milky = pickle.load(f)

t = Tokenizer()
for token in t.tokenize(milky):
    print(token)

# Output
# では			接続詞, *, *, *, *, *, では, デハ, デワ
# みなさん	名詞, 代名詞, 一般, *, *, *, みなさん, ミナサン, ミナサン
# は				助詞, 係助詞, *, *, *, *, は, ハ, ワ
# 、				記号, 読点, *, *, *, *, 、, 、, 、
# そういう	連体詞, *, *, *, *, *, そういう, ソウイウ, ソーユウ
# ふう			名詞, 非自立, 形容動詞語幹, *, *, *, ふう, フウ, フー
# に				助詞, 副詞化, *, *, *, *, に, ニ, ニ
# 川				名詞, 一般, *, *, *, *, 川, カワ, カワ
# だ				助動詞, *, *, *, 特殊・ダ, 基本形, だ, ダ, ダ
# と				助詞, 格助詞, 引用, *, *, *, と, ト, ト
# 云わ			動詞, 自立, *, *, 五段・ワ行促音便, 未然形, 云う, イワ, イワ
# れ				動詞, 接尾, *, *, 一段, 連用形, れる, レ, レ
# たり			助詞, 並立助詞, *, *, *, *, たり, タリ, タリ
# 、				記号, 読点, *, *, *, *, 、, 、, 、
# ...
```

#### Part-of-Speech Janome

```python
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

```

### Other Part-of-Speech Result

#### MeCab

| Part of Speech | Length | Head Data                                                    |
| -------------- | ------ | ------------------------------------------------------------ |
| 動詞           | 3149   | ['云わ', 'れ', '流れ', '云わ', 'れ', 'し', 'い', '吊し', 'けぶっ', '指し' ...] |
| 形容詞         | 479    | ['白い', '黒い', '白く', 'ねむく', 'ない', '早く', 'よく', 'よし', '白い', 'いい' ...] |
| 副詞           | 867    | ['そのまま', 'たしかに', 'まるで', 'なんだか', 'よく', 'もう', 'はっきり', 'すっと', 'もう' ...] |
| 助詞           | 6356   | ['は', 'に', 'と', 'たり', 'の', 'と', 'たり', 'て', 'と', 'が', 'は', 'か', 'か', 'は', 'に', 'の', 'の', 'から' ...] |
| 助動詞         | 2572   | 'だ', 'た', 'だ', 'た', 'です', 'た', 'た', 'な', 'まし', 'た', 'まし', 'た', 'まし', 'た', 'う', 'まし' ...] |

#### Janome

| Part of Speech | Length | Head Data                                                    |
| -------------- | ------ | ------------------------------------------------------------ |
| 動詞           | 3148   | ['云わ', 'れ', '流れ', '云わ', 'れ', 'し', 'い', '吊し', 'けぶっ', '指し'...] |
| 形容詞         | 479    | ['白い', '黒い', '白く', 'ねむく', 'ない', '早く', 'よく', 'よし', '白い', 'いい' ...] |
| 副詞           | 867    | ['そのまま', 'たしかに', 'まるで', 'なんだか', 'よく', 'もう', 'はっきり', 'すっと', 'もう' ...] |
| 助詞           | 6350   | ['は', 'に', 'と', 'たり', 'の', 'と', 'たり', 'て', 'と', 'が', 'は', 'か', 'か', 'は', 'に', 'の', 'の', 'から' ...] |
| 助動詞         | 2572   | ['だ', 'た', 'だ', 'た', 'です', 'た', 'た', 'な', 'まし', 'た', 'まし', 'た', 'まし', 'た', 'う', 'まし' ...] |

