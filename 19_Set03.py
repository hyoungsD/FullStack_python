# 아이템 수정, 삭제 2 

set1 = set([0, 1, 2, 3, 4, 5, 6])
set2 = set([4, 5, 6, 7, 8, 9, 10])

print(set1 & set2) # 교집합          # {4, 5, 6}
print(set1.intersection(set2))      # {4, 5, 6}
print(set1 | set2) # 합집합         # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set1.union(set2))             # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set1 - set2) # 차집합         # {0, 1, 2, 3}
print(set1.difference(set2))        #{0, 1, 2, 3}