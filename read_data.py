import re
import pickle

with open("the_night_of_the_milky_way_train.txt", mode="r", encoding="utf-8") as f:
    milky_original = f.read()

milky = re.sub("《[^》]+》", "", milky_original)
milky = re.sub("［[^］]+］", "", milky)
milky = re.sub("[｜ 　「」\n]", "", milky)

seperator = "。"
milky_list = milky.split(seperator)
milky_list.pop()
milky_list = [x + seperator for x in milky_list]

with open("the_night_of_the_milky_way_train.pickle", mode="wb") as f:
    pickle.dump(milky_list, f)
