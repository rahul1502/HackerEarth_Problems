def makeMove(n, k):
	i = n-k-1
	if (n-i) > k and (n-i) < (2*k):
		return i

t = int(input())
for l in range(t):
	input_str = input().split(' ')
	n = int(input_str[0])
	k = int(input_str[1])
	
	p = int((n - (3*k)) / k) + 1
	n -= p*k

	print('n: ' + str(n) + ' p: ' + str(p))
	print('---------------------------------------')

	if k > 1:
		while n > (k+1) and n < (3*k) and n > 0:
			p+=1
			move = makeMove(n, k)	
			print('n: ' + str( n- move) + ' removed: ' + str(move) + ' p: ' + str(p))
			n -= move
	else:
		p = n
		
	if p % 2 != 0:
		print('Arpa')
	else:
		print('Dishant')