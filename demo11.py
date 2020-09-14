import json_loads

exp_info = [
               {
                   "exp_id": 80938,
                   "exp_no": 0,
                   "params": "{\"new_push_engine.push.AddNodes.cacheDiff1\":\"- name: cacheDiff\\n  ab_hit_node: true\\n  pfunc:\\n      name: CacheDiff\\n      in: [recallDocs, predictCache]\\n      out: [needPredictDocs]\\n\\n  typeend: 0\",\"new_push_engine.push.AddNodes.cacheDiff3\":\"- name: cacheDiff\\n  ab_hit_node: true\\n  pfunc:\\n      name: CacheDiff\\n      in: [recallDocs, predictCache]\\n      out: [needPredictDocs]\\n\\n  typeend: 0\"}",
                   "description": "",
                   "name": "exp-0",
                   "cycle_aa": "",
                   "exp_percent": 0,
                   "status": 1,
                   "exp_params_type": "text",
               },
               {
                   "exp_id": 80939,
                   "exp_no": 1,
                   "params": "{\"new_push_engine.push.AddNodes.cacheDiff2\":\"- name: cacheDiff\\n  ab_hit_node: true\\n  pfunc:\\n      name: CacheDiff\\n      in: [recallDocs, predictCache]\\n      out: [needPredictDocs]\\n      conf:\\n        cache_filter_doc: 1\\n  typeend: 0\"}",
                   "description": "",
                   "name": "exp-1",
                   "cycle_aa": "",
                   "exp_percent": 0,
                   "status": 1,
                   "exp_params_type": "text",
               }
           ]

exp_param_key_sets = set(key for e in exp_info for key in json_loads.loads(e['params']))

print(exp_param_key_sets)
