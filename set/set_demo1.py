exp_info = [
    {
        "params": '{"ddtest12s222": "asd"}',
        "white_list": "123,321",
        "name": "exp-0",
        "description": "xxx"
    },
    {
        "params": '{"ddtest12s222": "asd"}',
        "white_list": "123,456,654",
        "name": "exp-1"
    }
]

name_set = set()
exp_white_sets = set()

for exp_data in exp_info:
    if exp_data['name'] in name_set:
        print('一个实验内不能有实验组名称一样')
    name_set.add(exp_data['name'])

    white_list = exp_data['white_list'].split(',')
    white_list_set = set()
    for w in white_list:
        white_list_set.add(w.strip())
    # print(white_list_set)

    intersection = white_list_set & exp_white_sets
    if intersection:
        print('白名单冲突')
    exp_white_sets |= white_list_set

print(name_set)
# print(exp_white_sets)
