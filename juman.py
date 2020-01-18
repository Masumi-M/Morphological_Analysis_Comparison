import pickle

with open("the_night_of_the_milky_way_train.pickle", mode="rb", ) as f:
    milky_list = pickle.load(f)

print(milky_list)
