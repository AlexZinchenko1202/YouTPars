

def read(adr):
	with open(adr) as file:
		return file.read()

# text = read('output3.html')
# keys = ['\"title\":', '\"description\":', '\"rssUrl\":', '\"channelUrl\":']

# for i in text.split('<'):
# 	for key in keys:
# 		key = key.replace('\"', '').replace(':', '')		
# 		if key in i:			
# 			elems = [ii.split('\",')[0].split('\\"') for ii in i.split(key) if '={}' not in i]
# 			print(len(elems))
# 			print(key.replace('\"',''))
# 			print(elems)




import numpy as np
from time import time

t1 = time()
numbers = np.array(list(np.random.randint(low = 1, high = 10, size = 100000)))

Z ={a:np.where(numbers==a)[0][-1] for a in range(1, 10)}

for i, num in enumerate(numbers):	
	if i<Z[num]:
		number_is_in_tail = True
		
#for i, num in enumerate(numbers):	#number_is_in_tail = number in numbers[i+1:]
	
print(time()-t1)



