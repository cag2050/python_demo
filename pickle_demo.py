import pickle

# str1 = "['qtt', 'midu']"
str1 = ["qtt", "midu"]
in_values = pickle.loads(str1.encode('utf-8'))

for v in in_values:
    print(v)