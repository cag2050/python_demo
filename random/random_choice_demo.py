import random
import string

seq = string.ascii_lowercase + string.digits

final_str = ''
for i in range(10):
    final_str += random.choice(seq)

print(final_str)
