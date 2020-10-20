import json
from yaml import load, Loader

exp_info = [
    {"name": "exp-0", "exp_params_type": "text", "cycle": 0, "cycle_aa": [], "cycle_days": [],
     "params": "{\"list-dnn-disliketf\":\" model_name: biaodan-cvr-sdnn-v6\\n guarantee: biaodan-cvr-sdnn-rf\"}"
     },
    {"name": "exp-1", "exp_params_type": "json", "cycle": 0, "cycle_aa": [], "cycle_days": [],
     "params": "{\"device_flow\":\"wwww\"}"
     }
]

exp_param_value_sets = set(value for e in exp_info for key, value in json.loads(e['params']).items())
model_name_set = set()
print('exp_param_value_sets')
print(exp_param_value_sets)
# yaml转Python object
for value in exp_param_value_sets:
    value_dict = load(value, Loader=Loader)
    print('value_dict')
    print(type(value_dict))
    if isinstance(value_dict, dict):
        if 'model_name' in value_dict:
            model_name_set.add(load(value, Loader=Loader)['model_name'])
        else:
            print('没有model_name这个key')
    else:
        print('没有model_name这个key')

print(model_name_set)



