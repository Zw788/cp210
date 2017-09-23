
# coding: utf-8

# # 1.

# In[2]:

import numpy as np
import math as ma
import scipy.misc as sci
import matplotlib.pyplot as plt


def quasolve (a=None, b=None, c=None):
    x_plus=(-b+np.sqrt((b**2)-4*a*c))/(2*a)
    x_minus=(-b-np.sqrt((b**2)-4*a*c))/(2*a)
    y_plus=(-2*c)/(b+np.sqrt((b**2)-4*a*c))
    y_minus=(-2*c)/(b-np.sqrt((b**2)-4*a*c))
    return(x_plus, x_minus, y_plus, y_minus)


# In[3]:

print("x_1, x_2,x'_1,x'_2")
for i in np.arange(1,21, dtype=np.int64):
    print(quasolve(1,1,10.0**(-i)))


# When the c value become small the first two sum seems to behave normally; the machine eventually treats c as zero because it's smaller than the precision. The fourth and third solutions have different precision than the first two solutions because the c value is on the numerator. The fourth solution eventually become infinity because the machine treated c as zero once again which dramatically produce a different solution. 

# In[4]:

print("x_1, x_2,x'_1,x'_2")
for i in np.arange(1,21, dtype=np.int64):
    print(quasolve(10.0**(-i),1,1))


# If we make the a value small, we once can see fluctuations happen in the first solution which show that when subtractive cancelation can dramatically change the solution.

# In[7]:

def quasolve_ex (a=None, b=None, c=None , dtype=np.int64):
    a=a*(10**19)
    b=b*(10**19)
    c=c*(10**19)
    x_plus=(-b+np.sqrt((b**2)-4*a*c))/(2*a)
    x_minus=(-b-np.sqrt((b**2)-4*a*c))/(2*a)
    y_plus=(-2*c)/(b+np.sqrt((b**2)-4*a*c))
    y_minus=(-2*c)/(b-np.sqrt((b**2)-4*a*c))
    return(x_plus, x_minus, y_plus, y_minus)


# In[8]:

for i in np.arange(1,21, dtype=np.int64):
    print(quasolve_ex(1,1,10.0**(-i)))


# Multiplying all three value by a large number will not change the solution but will force the machine to do subtraction with large integers which keeps the precision as much as possible.

# # 2.

# In[41]:

def S1(n=None):
    summands=np.arange(1,2*n+1, dtype=np.float64)
    for i in np.arange(1,2*n+1, dtype=np.int64):
        summands[i-1]=((-1)**i)*((i)/(i+1))
    ans1=np.sum(summands)
    return(ans1)

def S2(m=None):
    nsummands=np.arange(1,m+1, dtype=np.float64)
    for i in np.arange(1,m+1, dtype=np.int64):
        nsummands[i-1]=(2*i-1)/(2*i)
    psummands=np.arange(1,m+1, dtype=np.float64)
    for i in np.arange(1,m+1, dtype=np.int64):
        psummands[i-1]=(2*i)/(2*i+1)
    ans2=np.sum(psummands-nsummands)
    return(ans2)

def S3(l=None):
    tsummands=np.arange(1,l+1, dtype=np.float64)
    for i in np.arange(1,l+1, dtype=np.int64):
        tsummands[i-1]=(1)/((2*i)*(2*i+1))
    ans3=np.sum(tsummands)
    return(ans3)


# In[44]:

print(np.log10(np.absolute((S1(5)-S3(5)))/S3(5)),
np.log10(np.absolute((S1(10)-S3(10)))/S3(10)))


# In[71]:

b=np.arange(1000,4001, dtype=np.int64);
error1=np.arange(1000,4001, dtype=np.float64);
for i in np.arange(1,3001):
    error1[i]=np.absolute((S1(b[i])-S3(b[i]))/S3(b[i]));


# I decide to start at 1000 because some of the error terms are zero for lower N. I can't go up to N=1,000,000 because it takes too long for the algorithm to generate many points above N=100,000.

# In[97]:

error1[0]=10**(-13)
x1=np.log(b)/np.log(10)
y1=np.log(error1)/np.log(10)

plt.figure(figsize=(10,10))
plt.title(r"Log-log Graph of Relative Error Between $S_1$ and $ S_3$")
plt.xlabel(r"$Log_{10}(N)$")
plt.ylabel(r"$Log_{10}(\frac{|S_1 - S_3|}{S_3})$")
plt.plot(x1,y1)
plt.show()


# There doesn't seems to be any relation between the error of S1 and S3, just random fluctuations.

# In[72]:

t=np.arange(1000,4001, dtype=np.int64);
error2=np.arange(1000,4001, dtype=np.float64);
for i in np.arange(1,3001):
    error2[i]=np.absolute((S2(b[i])-S3(b[i]))/S3(b[i]));


# In[111]:

error2[0]=10**(-13.9)
x2=np.log(t)/np.log(10)
y2=np.log(error2)/np.log(10)
x3=np.linspace(3.0,3.6,1000)
y3=0.60*x3-15.635

plt.figure(figsize=(10,10))
plt.title(r"Log-log Graph of Relative Error Between $S_2$ and $ S_3$")
plt.xlabel(r"$Log_{10}(N)$")
plt.ylabel(r"$Log_{10}(\frac{|S_2 - S_3|}{S_3})$")
plt.xlim(3.0,3.6)
plt.plot(x2,y2,label="Relative Error")
plt.plot(x3,y3,label="y=0.6x-15.635")
plt.legend(loc=4)
plt.show()


# The relative error between S2 and S3 is more interesting as we can see an almost linear relationship between the relative error and some power of N. I guessed a line to show the linearity. 
