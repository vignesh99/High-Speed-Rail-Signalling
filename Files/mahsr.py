                                    #Import libraries
from pylab import *
from scipy.stats import norm
from scipy.interpolate import interp1d as inp
                                    #Experimental values in dBm and metre
Prx = array([-50.93,-56.13,-61.33,-66.3])
d = array([100,200,300,400])
Lx = inp(d,Prx)                     #Interpolate the values

dfine = np.arange(100,450,50)
Prxfine = Lx(dfine)
                                    #Noisy data
Prxnoise = Prxfine + norm.rvs(0,1.5,len(dfine))                                    
                                    #Plot the values
plt.plot(dfine,Prxfine,label="linear estimate")
plt.plot(dfine,Prxnoise,"r",marker=".",label="experimental values")
plt.grid()
plt.legend()
plt.title("Coupling loss estimate")
plt.ylabel("Rx power (dBm)")
plt.xlabel("Propagation distance")
plt.show()
