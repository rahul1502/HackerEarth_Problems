import itertools

input_str = input().split(' ')
n = int(input_str[0])
m = int(input_str[1])

skills = list(map(int, input().split(' ')))

master_arr = []
for i in skills:
	master_arr.append([j for j in range(0,i+1)]) 
print('master_arr '+ str(master_arr))
com_list = list(itertools.product(*master_arr))

print('com_list '+ str(com_list))
xor_list = []
for i in com_list:
	xor = 0
	for j in i:
		xor ^= j
	xor_list.append(xor)

mod = (10 ** 9) + 7
for i in range(m+1):
	print(xor_list.count(i)%mod,end = ' ')