position = ['과장','부장','대리','사장','대리','과장']
print("문제4")
nonRepeat = list(set(position))
print("중복되지 않은 직위 : ",nonRepeat)
count_pos = {}
for i in position:
    count_pos[i] = count_pos.get(i,0)+1
print("각 직위별 빈도수 : ",count_pos)