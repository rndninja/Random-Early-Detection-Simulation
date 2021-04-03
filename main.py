import numpy as np
import queue
import matplotlib.pyplot as plt
def Ran_gen_exp(n):
    return np.random.exponential(scale=n,size=None)
# def updater(x,m):
# 	i=Ran_gen(m);
# 	#print(i)
# 	count=0
# 	temp=1
# 	while temp==1:
# 		count=count+1
# 		if(i<count/1000):
# 			x.put(1)
# 			break
if __name__ == '__main__':
	#print(count)

	buffer_11 = queue.Queue(200)
	# temp2=1
	# while temp2==1:
	# 	updater(buffer_11,1)
	# 	print(buffer_11.qsize())
	#i=Ran_gen_exp(0.9)
	count1=0
	count2=0
	temp=1
	a=[]
	b=[]
	c=[]
	avg=0
	count=-1
	w=0.002
	minth=5
	maxth=15
	maxp=30/50
	drop=0
	while temp<1000000:
		if(count1==0):
			i=Ran_gen_exp(1.01)
		if(i<count1/1000):
			#if(not buffer_11.empty()):
			avg=(1-w)*avg+w*(buffer_11.qsize())
			if(maxth>avg>minth):
				count=count+1
				pb=(avg-minth)/(maxth-minth)
				pb=pb*maxp
				pa=pb/(1-count*pb)
				if(np.random.uniform(low=0,high=1,size=None)>pa):
					buffer_11.put(1)
					count=0
				else:
					drop=drop+1
			elif(avg<minth):
				count=-1
				buffer_11.put(1)
			elif(avg>maxth):
				count=0
				drop=drop+1
			count1=(-1)
		if(count2==0):
			j=Ran_gen_exp(1)
		if(j<count2/1000):
			if(not buffer_11.empty()):
				buffer_11.get()
			count2=(-1)	
		count1=count1+1
		count2=count2+1
		temp=temp+1
		a.append(buffer_11.qsize())
		b.append(temp)
		c.append(avg)
	print("Done")
	print(np.mean(a))
	print(np.max(a))
	print(np.mean(b))
	print(drop)
	plt.plot(b,a,b,c) 
	plt.show()		
		