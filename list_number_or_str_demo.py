list1 = ['呜呜呜呜', '10003']
list1 = []

final_str = ''
for i in range(len(list1)):
    if i == len(list1) - 1:
        final_str += '"' + list1[i] + '"'
    else:
        final_str += '"' + list1[i] + '",'

print(final_str)