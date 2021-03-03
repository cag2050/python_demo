# 模拟JS window.btoa()方法
# Authorization: Basic YWJfZXhwZXJpbWVudF90ZXN0OjJhOGIxZGQ2OGUzOWY5NDdkMmY2ZDVhNjc4YzU1NjZl
import base64

s = "ab_experiment_test" + ":" + "2a8b1dd68e39f947d2f6d5a678c5566e"

n = base64.b64encode(s.encode()).decode()
print(n)
print(type(n))
