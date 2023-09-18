'''
Matplotlib is a visualization library in python for 2D plots of arrays. This is built on NumPy arrays for internal calculations. 
This is introduced by John Hunter in the year 2002.Matplotlib consists of several plots like line, bar, scatter, histogram, etc

install matplotlib :
pip install -U matplotlib
'''
import matplotlib.pyplot as plt

x = [10,20,30,40,50]
y = [100,200,300,400,500]

plt.plot(x,y)
plt.show()

x = [11,34,99,55,33]
y = [770,550,110,345,970]

plt.plot(x,y)
plt.show()


