

def  op(adr):
	with open(adr) as file:
		return file.read().split('\n')
ans = {}

text = op('ENG')[:10]
ans = {}
ans = {i.split('    ')[1]:[i.split('    ')[2], 0, 0] for i in text}
ii = 0

while ii<len(text):
	i = text[ii]
	#print(i)
	print(i.split('    ')[-1].strip())
	x = input('ENTER ').strip()
	print(x)
	if x == i.split('   ')[1].strip():
		print('OK')
		ans[i.split('    ')[1]][1]+=1
		ii+=1
	else:		
		print(i.split('    ')[1])
		ans[i.split('    ')[1]][2]-=1



print('\n'.join([k+'\t'+','.join([str(i) for i in v]) for k, v in ans.items()]))
		