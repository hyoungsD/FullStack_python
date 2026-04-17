# time module과 for문을 사용해서 1~1000까지의 합을 구하는데 경과시간을 출력하시오

import time

start_time = time.time()
sum = 0

for i in range(1001):
    sum += i


end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

