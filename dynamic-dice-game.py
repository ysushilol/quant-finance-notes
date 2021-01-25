l = []
for i in range(19, 14, -1):
	l.append(i)

# print(l)

start = 0
end = 4
avg = sum(l[start:end+1])/5
print(avg)

for i in range(14, -1, -1):
	avg = sum(l[start:end+1])/6
	start += 1
	end += 1
	l.append(avg)

print([round(num, 2) for num in l][len(l)-1])

# Dynamic Dice Game

# 找到end state是什么样的（可能不止一种情况），然后通过这个往回推