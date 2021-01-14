# range(start, stop[, step])
# https://www.runoob.com/python/python-func-range.html

# for i in range(0, 3, 2):
#     print(i)

segment_num = 6
exp_num = 2
fetch_segments = [1,2,3,4,5,6]
exp_segments = [fetch_segments[i:i+int(segment_num/exp_num)] for i in range(0, segment_num, int(segment_num/exp_num))]
print(exp_segments)
