import random
import string

print(''.join(random.choices(string.ascii_lowercase + string.digits, k=10)))
print(random.choices(string.ascii_lowercase + string.digits, k=10))
