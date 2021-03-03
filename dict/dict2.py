categories = [
    {
        "id": 1,
        "offline_kylin_view": "view1"
    },
    {
        "id": 2,
        "offline_kylin_view": "view1"
    },
]

category_kylin_map = {}
for c in categories:
    print(c)
    # offline_kylin_view相同的，只插入一次
    if c['offline_kylin_view'] not in category_kylin_map:
        category_kylin_map[c['offline_kylin_view']] = c

print(category_kylin_map)
print(category_kylin_map.values())