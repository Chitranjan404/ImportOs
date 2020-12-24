import os
a=os.getcwd()
print 'Your current directory is:',a
b=input("Do you want to change your directory[1(Yes)/2(No)]")
if(b==1):
	c=raw_input("Type in which dir you want to go:")
	os.chdir(c)
	d=os.getcwd()
	print 'You are now inside:',d
for i in range(0,20):
	f=str(i)
	os.mkdir(f)
	


