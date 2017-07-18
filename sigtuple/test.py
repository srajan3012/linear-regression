
def n_trail_zero(n):
	count = 0
	r = 0
	while n > 9 and r == 0:
		r = n%10
		n = n/10
		count += 1 
	return count

# print n_trail_zero(10)


def change(d):
	d['1'] += 10

d = {'1':1,'2':2}
change(d)
print d

# print max(10050000,1000000,key=n_trail_zero)