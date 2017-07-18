problem = '''Longest Increasing Subsequence'''


def LIS(sequence):
	lis 	= [0 for i in range(len(sequence))]
	lis[0] 	= 1

	for i in range(1,len(sequence)):
		max_curr_lis = 0
		for j in range(0,i):
			if sequence[i] > sequence[j] :
				curr_lis = lis[j] + 1
				if curr_lis > max_curr_lis:
					max_curr_lis = curr_lis

		lis[i] = max_curr_lis if max_curr_lis else 1

	return max(lis)



if __name__ == '__main__':
	# sequence = [10,12,200,202,75,90,91,20,40,94,10,100]
	sequence = [10,22,9,33,21,50,41,60,80]
	print(LIS(sequence))
