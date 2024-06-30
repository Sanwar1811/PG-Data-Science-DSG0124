#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


dict = {'India_Runs' :[10,12,9,8,15,18,20], 'England_Runs' :[4,8,10,9,10,19,22]}
df = pd.DataFrame(dict,index=[1,2,3,4,5,6,7])
df


# In[5]:


df['England_Runs'].plot(kind = 'bar')
plt.show()


# In[9]:


df.plot(kind = 'bar', figsize=(8,4))
plt.xlabel('Overs', color='b', fontsize=15)
plt.ylabel('Runs', color='g', fontsize=15)
plt.title('Run_Per_Over', color='r', fontsize=20)
plt.grid(axis='y')
plt.yticks(range(0,36,2))
plt.show


# In[10]:


mileage = sns.load_dataset('mpg')
mileage.head()


# In[13]:


mileage.shape


# In[16]:


mileage.mpg.plot(kind= 'hist')
plt.show()


# In[20]:


mileage.mpg.plot(kind= 'hist', bins=70)
plt.show()


# In[22]:


mileage.mpg.plot(kind = 'hist', figsize=(20,30),bins=70,color='r')
plt.show()


# In[23]:


sns.get_dataset_names()


# In[24]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


emp = {'Age_Years' :[10,23,22,25,20,23,24,27,25,24,33,21],'Salary_Thousands' :[15,22,24,25,30,23,34,43,19,20,52,21]}
df = pd.DataFrame(data=emp)
df


# In[29]:


df.plot(kind = 'box', figsize= (8,5), color= 'r', yticks = range(0,55,5))
plt.show()


# In[30]:


plt.figure(figsize=(5,6))
ax=sns.boxplot(data=df)
plt.yticks(range(5,55,5))
plt.xlabel('Age_And_Salary')
plt.ylabel('Numbers')
plt.show()


# In[31]:


sal = [15,22,24,25,30,23,34,43,19,20,52,21]
sal.sort()
sal


# In[32]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from pandas.plotting import scatter_matrix


# In[33]:


mileage = sns.load_dataset('mpg')
mileage.head()


# In[34]:


plt.scatter(x=mileage['cylinders'], y=mileage['mpg'])
plt.xlabel('cyl')
plt.ylabel('mpg')
plt.show()


# In[35]:


scatter_matrix(mileage, figsize= (15,10), color = 'b')
plt.show()


# In[36]:


avg_mpg = mileage.groupby(by= 'cylinders')[['mpg','cylinders']].mean()
avg_mpg


# In[39]:


plt.pie(x=avg_mpg['mpg'], labels=avg_mpg['cylinders'])
plt.title('Avg_Mileage_Per_Cylinders')
plt.show()


# In[40]:


plt.figure(figsize=(6,6))
plt.pia(x=avg_mpg['mpg'], labels=avg_mpg['cylinders'],explode=[0,0,0,0.05,0.3],autopct = '%.2f')
plt.title('Avg_Mileage_Per_Cylinders_Type')
plt.show()


# In[43]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[44]:


tips=sns.load_dataset('tips')
tips.tail()


# In[45]:


sns.relplot(x = 'total_bill', y = 'tip', data = tips)
plt.show()


# In[47]:


tips['smoker'].value_counts()


# In[52]:


sns.relplot(x = 'total_bill', y = 'tip', data = tips, hue = 'time' ,palette='muted')
plt.show()


# In[53]:


sns.lineplot(x = 'total_bill', y = 'tip', data = tips, hue='time')
plt.show()


# In[ ]:




