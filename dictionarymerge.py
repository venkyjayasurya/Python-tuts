def merge(dict1,dict2):
	res={**dict1,**dict2}
	return res

dict1={'a':10,'b':20}
dict2={'c':30,'d':40}
dict3=merge(dict1,dict2)
print(dict3)