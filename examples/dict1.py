d= {'a': 'sd', 'b': 'ds'}
E= d.keys()
F=d.keys()[0]
print("F:",F)
print("d=",E)
args  = []
for key in d.keys():
	print("key:",key)
	args.append({key: d[key]})
print("args:",args)
for arg in args:
	print("arg::::",arg)
cc = d.get("args")	
print ("cc=",cc)
