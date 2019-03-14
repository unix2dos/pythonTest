import pickle

# d = dict(name='levon')
# f = open("1.pick", "wb")
# pickle.dump(d, f)

f1 = open("1.pick", "rb")
d1 = pickle.load(f1)
print(d1)
