# 내장모듈 활용 - time

import time

print(time.time())

local_time = time.localtime(time.time())
str_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
print(str_time)



print("시작")
time.sleep(5)
print("종료")
start_time = time.time()
time.sleep(5)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)