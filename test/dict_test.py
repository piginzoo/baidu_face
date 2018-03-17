d1 = {'name':'liuhaoyue','age':18,
		'chengji':{'math':100,'chinese':89}
	 }
d2 = {'name':'cuitianshuo','age':18}
d3 = {'name':'liao','age':18}
d4 = {'name':'liuhaotian','age':18}

print d1
print d1['age']
print d1['name']
print d1['chengji']
print d1['chengji']['chinese']


print "============"
print type(d1)
#print d1

d1['like'] = 'dog'
#print d1

my_class_mate = []
my_class_mate.append(d1)
my_class_mate.append(d2)
my_class_mate.append(d3)
my_class_mate.append(d4)

for dd in my_class_mate:
	print type(dd),":",dd

