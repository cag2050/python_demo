from collections import OrderedDict

fields = OrderedDict([(k, '222') for k in ['id',
                                           'name',
                                           'desc',
                                           'sort_id',
                                           'project_id',
                                           'offline_kylin_view',
                                           'realtime_kylin_view']])
print(fields)
print(fields['id'])
