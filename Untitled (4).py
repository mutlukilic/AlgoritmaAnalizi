#!/usr/bin/env python
# coding: utf-8

# In[1]:


# matrix_1 mxn 
# matrix_2 nxp
# matrix_3=matrix_1 * matrix_2   , mxp


# In[7]:


def get_value_from_row_col(r_1,c_1):#a matrisinin birinci satırı
    t=0
    for i in range(len(r_1)):#r_1  de olur c_1 de olur. Çünkü ikiside aynı boyutta olmak zorunda
        t=t+r_1[i]*c_1[i]
    return t
a=[1,2,3,4]
b=[5,6,7,8]
get_value_from_row_col(a,b)
#bunun karmısıklıgı : O(n)  Q(n) ' de olabilir.


# In[26]:


a=[[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]] #4x4
b=[[1,2,3,4],[5,6,7,8]] #2x4


# In[24]:


def get_row_from_matrix(a,i): #i. satırı vermesini istiyoruz. 
    return a[i]
def get_col_from_matrix(a,j):
    col=[]
    for row in a:
        col.append(row[j])
        #for indis in range(len(row)):
            #if(indis==j):
                #col.append(row[indis])
    return col
get_col_from_matrix(a,1)


# In[27]:


def matrix_multiply(m_1,m_2): #karmasıklık O(mnp), O(n**3)
    m=len(m_1)
    n=len(m_2[0])
    r=[]
    for i in range(m):
        r.append([])
        for j in range(n):
            a=get_row_from_matrix(m_1,i)
            b=get_col_from_matrix(m_2,j)
            c=get_value_from_row_col(a,b)
            r[i].append(c)
    return r
a,b


# In[22]:


def matrix_multiply(m_1,m_2): #karmasıklık O(mnp), O(n**3)
    m=len(m_1)
    n=len(m_2[0])
    r=[]
    for i in range(m):
        r.append([])
        for j in range(n):
            a=get_row_from_matrix(m_1,i)
            b=get_col_from_matrix(m_2,j)
            c=get_value_from_row_col(a,b)
            r[i].append(c)
    return r
a=[[1,2,3,4],[5,6,7,8]]
b=[[1,2,3],[5,6,7],[1,2,4],[5,7,8]]
matrix_multiply(a,b)


# In[12]:


l_1=[1,2,3,4]
l_1[50]=0 # hata verir


# In[ ]:




