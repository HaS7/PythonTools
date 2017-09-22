from pylab import *

n = 10

X = [1,2,3,4,5,6,7,8,9,10]
#Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

bar_color = ['#EE1289','#EE6A50','#EE7942','#EE82EE','#EEA2AD','#EEB422','#EECBAD','#EED5D2','#EEE0E5','#EEE8CD']

Y = [1,2,3,4,5,6,7,8,9,10]

#Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

bar(X, Y, color=bar_color, edgecolor='white' , width=0.8)
#bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

#plt.xticks(0 + 1, ('A', 'B', 'C', 'D', 'E','A', 'B', 'C', 'D', 'E'))

# for x,y in zip(X,Y):
#     text(x, y+0.05, y, ha='center', va= 'bottom')

ylim(0,12)
show()

