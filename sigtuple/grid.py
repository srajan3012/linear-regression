import os


M,N = map(int, raw_input().split())
arr = list()

for i in range(M):
	row = map(int, raw_input().split())
	arr.append(row)


def n_trail_zero(n):
	count = 0
	r = 0
	while n > 9 and r == 0:
		r = n%10
		n = n/10
		if r == 0:
			count += 1 
	return count


def get_product(curr_prod, row, column):

	if row < M and column < N:
		p1 = get_product(curr_prod*arr[row][column], row+1, column)
		
		p2 = get_product(curr_prod*arr[row][column], row, column+1)

		# print p1, p2
		if p1 != -1 and p2 != -1:
			return min(p1,p2,key=n_trail_zero)
		if p1 == -1 and p2 == -1:
			return curr_prod*arr[row][column]
		if p1 == -1:
			return p2
		if p2 == -1:
			return p1

	return -1


curr_prod = 1
x = get_product(curr_prod,0,0)
print x
print n_trail_zero(x)