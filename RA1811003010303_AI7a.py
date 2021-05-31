#!/usr/bin/env python
# coding: utf-8

# In[3]:


def unifunc(f1,f2):
    if '(' in f1 and '(' in f2:
        if f1[0]==f2[0]:
            return unifunc(f1[2,-1],f2[2,-1])
        else:
            return 0
    elif '(' not in f1 and f1 not in f2:
        subst.append(f2+'/'+f1)
        f1=f2

    elif '(' not in f2 and f2 not in f1:
        subst.append(f1+'/'+f2)
        f2=f1

def unif(f1,f2):
    subst=[]
    if f1==f2:
        return 0
    if len(f1)!=len(f2):
        return 0
    for i in range(len(f1)):
        if '(' not in f1[i] and f1[i] not in f2[i]:
            subst.append(f2[i]+'/'+f1[i])
            f1[i]=f2[i]

        elif '(' not in f2[i] and f2[i] not in f1[i]:
            subst.append(f1[i]+'/'+f2[i])
            f2[i]=f1[i]
        else:
            unifunc(f1[i],f2[i])
    print(subst)




subst=[]
x=input("Enter arguments of P separated by spaces ")
f1=x.split()
y=input("Enter arguments of function Q separated by spaces ")
f2=y.split()
print("Checking unification of P and Q ")
unif(f1,f2)


# In[ ]:




