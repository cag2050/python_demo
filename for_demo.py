objs = ["1", "2"]
obj_ids = {}
obj_ids_map = {}

obj_ids = [obj for obj in objs]
obj_ids_map = {obj: obj + "xxx" for obj in objs}

print(obj_ids)
print(obj_ids_map)
