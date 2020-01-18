import pickle
from janome.tokenizer import Tokenizer

with open("the_night_of_the_milky_way_train.pickle", mode="rb") as f:
    milky = pickle.load(f)

t = Tokenizer()
for token in t.tokenize(milky):
    print(token)
