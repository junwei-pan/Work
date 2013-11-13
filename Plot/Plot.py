from matplotlib.mlab import normpdf
#import matplotlib.numerix as nx
import matplotlib.pyplot as plt
import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import os, string, sys, math
from matplotlib import cm as cm
from matplotlib import mlab as ml
from hitchhiker import *
def _sigmoid(x):
	return 1/(1+np.exp(-1*x))

def transform(x):
	return (x-(4950/2))/495.0

def Plot_Hexbin():
	np.random.seed(0)
	n=10000
	x=np.random.standard_normal(n)
	y=2.0+3.0*x+4.0*np.random.standard_normal(n)
	xmin = x.min()
	xmax = x.max()
	ymin = y.min()
	ymax = y.max()

	plt.subplots_adjust(hspace=0.5)
	plt.subplot(121)
	plt.hexbin(x,y, cmap=plt.cm.YlOrRd_r)
	plt.axis([xmin, xmax, ymin, ymax])
	plt.title("Hexagon binning")
	cb = plt.colorbar()
	cb.set_label('counts')

	plt.subplot(122)
	plt.hexbin(x,y,bins='log', cmap=plt.cm.YlOrRd_r)
	plt.axis([xmin, xmax, ymin, ymax])
	plt.title("With a log color scale")
	cb = plt.colorbar()
	cb.set_label('log10(N)')

	plt.show()

	

def Plot_Histogram(x,title='',xlabel='',ylabel=''):
	#x=read_yahoo_facebook_data()
	n,bins,patches=plt.hist(x,300,normed=0.75,facecolor='g',alpha=0.75)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.grid(True)
	plt.show()

def read_yahoo_facebook_data():
	x=[]
	y=[]
	dir='Join_Result_of_Yahoo_Facebook'
	num=0.0
	for file in os.listdir(dir):
		path=os.path.join(dir,file)
		for line in open(path):
			num+=1
			if num%10000==0:
				print num/866091.0
			lst=line.strip().split('\t')
			try:
				yahoo=2013-string.atof(lst[1])
				facebook=2013-string.atof(lst[4])
				if yahoo!=facebook and abs(yahoo-facebook)<=30:
					x.append(yahoo-facebook)
				'''
				if yahoo<=100 and facebook<=100 and yahoo!=facebook:
					x.append(yahoo)
					y.append(facebook)
				'''
			except Exception:
				pass
	return x

def Plot_Heat_Map():
	#x=np.random.randn(8873)
	#y=np.random.randn(8873)
	x,y=read_yahoo_facebook_data()
	plt.tick_params(axis='x',top='on',bottom='off')
	heatmap, xedges, yedges=np.histogram2d(x,y,bins=80)
	extent=[xedges[0],xedges[-1],yedges[-1],yedges[0]]
	plt.clf()
	plt.imshow(heatmap, extent=extent)
	plt.xlabel('Yahoo Age')
	plt.ylabel('Facebook Age')
	plt.show()


def Plot_Sigmoid():
	#x=np.arange(-10,10,.1)
	#x0=np.arange(50,5000,1.0)
	#x=transform(x0)
	x=np.arange(-2,2.1,0.1)
	y=_sigmoid(x)
	plt.plot(x,y,'r-')
	plt.show()

def Plot_normpdf():
	x=np.arange(-4,4,0.01)
	y=normpdf(x,0,1)
	plt.plot(x,y,color='red',lw=2)
	plt.show()

def Jeffreys(x):
	return (x**(-.05))*((1-x)**(-0.05))

def Plot_JeffreysProb():
	x=np.arange(0,1,0.01)
	y=Jeffreys(x)
	plt.plot(x,y,'r-')
	plt.show()

def Plot_PR():
	x=[]
	y=[]
	for line in open('pr.txt'):
		lst=line.strip().split(' ')
		x.append(string.atof(lst[0]))
		y.append(string.atof(lst[1]))
	plt.plot(x,y,'r-')
	plt.show()

def Plot_ROC():
	x=[]
	y=[]
	for line in open('auc.txt'):
		lst=line.strip().split('\t')
		x.append(string.atof(lst[4]))
		y.append(string.atof(lst[5]))
	print x
	print y
	plt.plot(x,y,'r-')
	plt.show()

def stat_age_regression():
	label=[]
	score=[]
	delta=[]
	for line in open('age_join_20_60'):
		lst=map(string.atof,line.strip().split('\t'))
		label.append(lst[0])
		score.append(lst[1])
		delta.append(lst[1]-lst[0])
	Plot_Histogram(x=label,title='label')
	Plot_Histogram(x=score,title='score')
	Plot_Histogram(x=delta,title='delta')

def stat_label():
	d={}
	for line in open('age_join'):
		lst=line.strip().split('\t')
		d.setdefault(lst[0],0)
		d[lst[0]]+=1
	sort=sorted(d.iteritems(), key=lambda a:a[0])
	for s in sort:
		print s[0],s[1]

def read_Category_Histogram():
	x=[]
	for line in open('Category_Histogram.txt'):
		lst=map(int,map(string.atof,line.strip('\n').split('\t')))
		if lst[0]<1000:
			x.extend([lst[0]]*lst[1])
	return x
def read_linked(path):
	x=[]
	for line in open(path):
		lst=map(int,map(string.atof,line.strip('\n').split(' ')))
		if lst[0]<300:
			x.extend([lst[0]]*lst[1])
	return x

def stat_Category_Histogram():
	total=0.0
	num=0.0
	for line in open('Category_Histogram.txt'):
		lst=map(string.atof,line.strip('\n').split('\t'))
		total+=lst[1]
		if lst[0]>30:
			num+=lst[1]
	print num/total


def Plot_Line(x,y):
	plt.plot(x,y,'r-')
	plt.show()

def read_age_event():
	x=[]
	y=[]
	for line in open('age_event.txt'):
		lst=line.strip('\n').split('\t')
		x.append(lst[0])
		y.append(lst[1])
	return x,y

def read_virtual_volume():
    data=open('virtual_volume.txt').readlines()
    x=[]
    y=[]
    z=[]
    num=0
    for thres in np.arange(0.8,1.0,0.01):
        x.append(thres)
        y.append(string.atof(data[num*2].strip('\n'))/100000.0)
        z.append(string.atof(data[num*2+1].strip('\n')))
        num+=1
    return x,y,z

def main():
    x,y,z=read_virtual_volume()
    plt.plot(x,y,'r-')
    plt.plot(x,z,'b-')
    plt.xlabel('threshold')
    plt.show()
	#x,y=stat_unlinked()
	#Plot_Line(x,y)
	#path='unlinked_fea.txt'
	#x=read_linked(path)
	#Plot_Histogram(x)
	#x,y=read_age_event()
	#Plot_Line(x,y)
	#stat_Category_Histogram()
	#x=read_Category_Histogram()
	#Plot_Histogram(x)
	#stat_label()
	#stat_age_regression()
	#Plot_PR()
	#Plot_ROC()
	#Plot_Hexbin()
	#Plot_Histogram()
	#Plot_Heat_Map()
	#Plot_JeffreysProb()
	#print _sigmoid(-2)
	#print _sigmoid(-5)
	#Plot_normpdf()
	#Plot_Sigmoid()

if __name__=='__main__':
	main()
