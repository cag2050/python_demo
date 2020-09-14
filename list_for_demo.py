import json_loads
str1 = '["qtt", "midu"]'
in_values = list(json_loads.loads(str1))

for v in in_values:
    print(v)