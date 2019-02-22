#!/usr/bin/env python
# coding: utf-8

# In[12]:


import time
def power(x,y):
    start=time.time()
    t=1
    for i in range(y):
        t = t*x
    stop=time.time()
    return t,(stop-start)


# In[13]:


print(power(3,2))


# In[28]:



def power_recursive(x,y):
    if(y==0):
        return 1
    if(y==1):
        return x
    if(y%2==0):
        return power_recursive(x*x,y/2)
    if(y%2==1):
        return power_recursive(x*x*x,int(y/2))


# In[29]:


print(power_recursive(4,3))


# In[46]:


sayac=0
def power_1(m,n):
    t=1
    global sayac
    for i in range(n):
        #print("i sayac",i,sayac)
        sayac=sayac+1
        t=t*m
    return (t,sayac)
def call_report(x,y):
    global sayac
    sayac =0
    r=power_1(x,y)
    print(x," üzeri ", y, " degeri : ",r[0],"çağrım sayısı : ",r[1])


# In[45]:


def power_2(x,n):
    global sayac
    sayac=sayac+1
    if(n==0):
        return 1,sayac
    if(n==1):
        return x,sayac
    if(n%2==0):
        return (power_2(x*x,n//2)[0],power_2(x*x,n//2)[1])
    if(n%2==1):
        return (power_2(x*x,n//2)[0]*x,power_2(x*x,n//2)[1])
def call_report_recursive(x,y):
    global sayac
    sayac =0
    r=power_2(x,y)
    print(x," üzeri ", y, " degeri : ",r[0],"çağrım sayısı : ",r[1])
call_report_recursive(2,6)


# In[43]:


call_report(2,23)
call_report(2,20)
call_report(3,3)
call_report(3,30)


# In[21]:


call_report(3,3)


# In[ ]:




