import MeCab as mecab
import pickle

with open("the_night_of_the_milky_way_train.pickle", mode="rb") as f:
    milky = pickle.load(f)

m_tagger = mecab.Tagger()
result = m_tagger.parse(milky)
print(result)
