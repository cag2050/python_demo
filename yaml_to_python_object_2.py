import json
from yaml import load, Loader

exp_info = [
    {"name": "exp-0", "exp_params_type": "text", "cycle": 0, "cycle_aa": [], "cycle_days": [],
     "params": "{\"list-dnn-disliketf\":\" model_name: biaodan-cvr-sdnn-v6\\n guarantee: 111\"}"
     },
    {"name": "exp-1", "exp_params_type": "json", "cycle": 0, "cycle_aa": [], "cycle_days": [],
     "params": "{\"model_name\":\"666\"}"
     }
]

model_name_set = set()

for exp in exp_info:
    if exp['exp_params_type'] == "json":
        if 'model_name' in json.loads(exp['params']):
            model_name_set.add(json.loads(exp['params'])['model_name'])
        else:
            print('没有model_name这个key')
    elif exp['exp_params_type'] == "text":
        for key, value in json.loads(exp['params']).items():
            value_dict = load(value, Loader=Loader)
            print('value_dict')
            print(value_dict)
            if 'model_name' in value_dict:
                model_name_set.add(value_dict['model_name'])
            else:
                print('没有model_name这个key')

print(model_name_set)



