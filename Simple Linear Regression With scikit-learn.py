#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import packages and classes
import numpy as np
from sklearn.linear_model import LinearRegression


# In[2]:


#Provide data
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])


# In[3]:


#.reshape:two-dimensional or to have one column and as many rows as necessary. 
print(x)


# In[7]:


#Create a model and fit it
model = LinearRegression().fit(x, y)


# In[8]:


#obtain the coefficient of determination (𝑅²) 
# predictor x and regressor y, and the return value is 𝑅².
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)


# In[10]:


print('intercept:', model.intercept_)
print('slope:', model.coef_)


# In[11]:


#intercept_ is a one-dimensional array with the single element 𝑏₀, and .coef_ is a two-dimensional array with the single element 𝑏₁.
new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
print('intercept:', new_model.intercept_)
print('slope:', new_model.coef_)


# In[12]:


#predictions
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')


# In[13]:


y_pred = model.intercept_ + model.coef_ * x
print('predicted response:', y_pred, sep='\n')


# In[14]:


#use fitted models to calculate the outputs
x_new = np.arange(5).reshape((-1, 1))
print(x_new)
y_new = model.predict(x_new)
print(y_new)


# In[ ]:


#source: 

