import json

json_str1 = "{\"name\":\"jeff\"}"

json_object = json.loads(json_str1)
print("json_object: ")
print(json_object)
print("type(json_object): ")
print(type(json_object))
print("json_object['name']")
print(json_object['name'])


json_str2 = json.dumps(json_object)
print("type(json_str2)")
print(type(json_str2))
print(json_str2)
print("json_str2")



