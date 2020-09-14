import json

# str1 = '["qtt", "midu"]'
str1 = "['qtt', 'midu']"
str2 = str1.replace('\'', '"')
# print(str2)
print(json.loads(str2))
print(type(json.loads(str2)))
