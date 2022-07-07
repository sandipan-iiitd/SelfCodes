#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=pd.read_csv("https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv")


# In[3]:


data


# In[4]:


data.info()


# In[5]:


data.describe()


# The minimum age is 18 years while maximum being 64 , so it shows that insurance does not cover age lesser than 18 and above 64 , the minimum number of children for the customers is 0 and maximum being 5.

# In[6]:


data['region'].unique()


# In[7]:


import plotly.express as px
import matplotlib 
import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


sns.set_style('darkgrid')


# In[9]:


fig=px.histogram(data,x='age',marginal='box',nbins=47,title='Age Count')
fig.show()


# Maximum count of people under ACME insurance is 18 and 19 , it seems that for such less age ACME gives some lucrative policies

# In[10]:


fig1=px.histogram(data,x='bmi',marginal='box',title='BMI variation')
fig1.show()


# BMI of maximum people are between 28 to 31

# In[11]:


sns.pairplot(data)


# It shows relationship between different variables

# In[12]:


fig2=px.histogram(data,x='charges',color='smoker',marginal='box',title='Annual Medical Charges')
fig2.show()


# The graph shows that smokers generally have higher value of medical insurance than non-smokers, the median charges for non-smokers is 7,345k while for smokers it is 34.46k

# In[13]:


data['smoker'].value_counts()


# There are 264 smokers and 1064 non smokers out of the customer data that is available

# In[14]:


px.histogram(data,x='smoker',color='sex')


# So out of total customers who are smokers i.e. 264 in numbers 115 are female while the rest are male 
# 

# In[15]:


px.scatter(data,x='bmi',y='charges',color='smoker',hover_data=['sex'])


# Smoking with obesity might be related to high charges

# In[16]:


sns.lmplot(data=data,x='bmi',y='charges',hue='smoker')


# In[17]:


px.scatter(data,x='age',y='charges',color='sex',hover_data=['smoker'])


# In[18]:


px.violin(data,x='children',y='charges')


# To check out the relationship of charges with variables we can use the correlation too, thus:

# In[19]:


data['charges'].corr(data['age'])


# In[20]:


data['charges'].corr(data['bmi'])


# In[21]:


data['charges'].corr(data['children'])


# In[22]:


smoker_map={'yes':1,'no':0}
x=data['smoker'].map(smoker_map)


# In[23]:


data['charges'].corr(x)


# It shows that people who smoke have the maximum correlation with charges which shows a good positive correlation

# In[24]:


data.corr()


# In[25]:


sns.heatmap(data.corr(),cmap='Reds',annot=True)


# In[26]:


def charges(w,b,age):
    return(w*age+b)


# In[27]:


w=50
b=100


# In[28]:


charges(w,b,30)


# In[29]:


non_smoker_df=data[data.smoker=='no']


# In[30]:


non_smoker_df


# In[31]:


age_array=non_smoker_df['age']


# In[32]:


age_array


# In[33]:


original_charges=non_smoker_df['charges']


# In[34]:


estimated_charge=charges(w,b,age_array)


# In[35]:


plt.scatter(age_array,estimated_charge,edgecolors='Red')
plt.xlabel('Ages')
plt.ylabel('Estimated Charges')


# In[36]:


plt.scatter(age_array,original_charges)
plt.plot(age_array,estimated_charge,'r')
plt.xlabel('Ages')
plt.ylabel('Charges')


# In[37]:


def try_parameters(w,b):
    age_array=non_smoker_df['age']
    original_charges=non_smoker_df['charges']
    estimated_charge=charges(w,b,age_array)
    plt.scatter(age_array,original_charges)
    plt.plot(age_array,estimated_charge,'r')
    plt.xlabel('Age')
    plt.ylabel('Charges')


# In[38]:


try_parameters(300,-2000)


# In[39]:


actuals=original_charges=non_smoker_df['charges']
actuals


# In[40]:


predicted=estimated_charge
predicted


# In[41]:


import numpy as np


# In[42]:


def rmse(actuals,predicted):
    return np.sqrt(np.mean(np.square(actuals-predicted)))


# In[43]:


rmse(actuals,predicted)


# On an average the prediction differs from the actuals by almost $8461 rounded to the nearest digit

# In[44]:


def try_parameters(w,b):
    age_array=non_smoker_df['age']
    original_charges=non_smoker_df['charges']
    estimated_charge=charges(w,b,age_array)
    plt.scatter(age_array,original_charges)
    plt.plot(age_array,estimated_charge,'r')
    plt.xlabel('Age')
    plt.ylabel('Charges')
    rmse_loss=rmse(original_charges,estimated_charge)
    return(rmse_loss)


# In[45]:


try_parameters(282,-2500)


# In[ ]:





# In[46]:


try_parameters(282,-2500)


# In[47]:


from sklearn.linear_model import LinearRegression


# In[48]:


model=LinearRegression()


# In[49]:


help(model.fit)


# In[50]:


inputs=non_smoker_df[['age']]
target=non_smoker_df['charges']


# In[51]:


model.fit(inputs,target)


# In[52]:


model.predict(np.array([[23],[37],[61]]))


# In[53]:


predictions=model.predict(inputs)


# In[54]:


predictions


# In[55]:


rmse(target,predictions)


# Seems like on an average we are almost $4662 off the track from actuals in terms of predictions

# In[56]:


model.coef_


# In[57]:


model.intercept_


# In[58]:


plt.scatter(age_array,original_charges)
plt.plot(inputs,predictions,'r')
plt.xlabel('Age')
plt.ylabel('Estimated Charges')


# In[59]:


smoker_df=data[data['smoker']=='yes']
age_smoker=smoker_df['age']
smoker_charges=smoker_df['charges']


# In[60]:


plt.scatter(age_smoker,smoker_charges)


# In[61]:


def pred(w,b,age):
    return(w*age+b)


# In[62]:


w=700
b=2000


# In[63]:


pred_smoker=pred(w,b,age_smoker)


# In[64]:


plt.scatter(age_smoker,smoker_charges)
plt.plot(age_smoker,pred_smoker,'r')


# In[65]:


def try_para_smoker(w,b):
    smoker_df=data[data['smoker']=='yes']
    age_smoker=smoker_df['age']
    actuals=smoker_df['charges']
    plt.scatter(age_smoker,smoker_charges)
    predicted=pred(w,b,age_smoker)
    plt.plot(age_smoker,pred_smoker,'r')
    rmse=np.sqrt(np.mean(np.square(actuals-predicted)))
    return rmse
    


# In[66]:


try_para_smoker(800,1000)


# In[67]:


from sklearn.linear_model import LinearRegression
model=LinearRegression()


# In[68]:


inputs=smoker_df[['age']]
target=smoker_df['charges']


# In[69]:


model.fit(inputs,target)


# In[70]:


model.predict(np.array([[23],[46]]))


# In[71]:


predictions_smoker=model.predict(inputs)


# In[72]:


rmse(target,predictions_smoker)


# For smokers the predicted value is off by $10711 from actuals 

# In[73]:


model.coef_


# In[74]:


model.intercept_


# In[ ]:


model.predict(np.array([[27]]))


# In[ ]:


df_non_smoker=data[data['smoker']=='no']
inputs,target=df_non_smoker[['age','bmi']],df_non_smoker['charges']


# In[ ]:


model=LinearRegression()


# In[ ]:


model.fit(inputs,target)


# In[ ]:


actuals=df_non_smoker['charges']


# In[ ]:


predictions=model.predict(inputs)


# In[ ]:


def rmse(actuals,predictions):
    return np.sqrt(np.mean(np.square(actuals-predictions)))


# In[ ]:


print("Loss:",rmse(actuals,predictions))


# In[ ]:


df_non_smoker['charges'].corr(df_non_smoker['bmi'])


# In[ ]:


model.coef_,model.intercept_


# Since the loss doesn't decrease much on including the feature bmi in the non smoker's data frame , trying to decode how much will be the loss with only bmi being the single input feature

# In[ ]:


actuals=df_non_smoker['charges']


# In[ ]:


inputs=df_non_smoker[['bmi']]


# In[ ]:


target=df_non_smoker['charges']


# In[ ]:


model=LinearRegression()


# In[ ]:


model.fit(inputs,target)


# In[ ]:


predictions=model.predict(inputs)


# In[ ]:


print("Loss:",rmse(actuals,predictions))


# This shows that loss increases when only bmi is taken into account w.r.t charges for non smokers

# Let's see how charges get predicted when we take bmi and age for smokers and how much is the loss

# In[ ]:


df_smoker=data[data['smoker']=='yes']


# In[ ]:


inputs,target=df_smoker[['age','bmi']],df_smoker['charges']


# In[ ]:


model=LinearRegression()


# In[ ]:


model.fit(inputs,target)


# In[ ]:


predictions=model.predict(inputs)


# In[ ]:


print("Loss:",rmse(target,predictions))


# The loss becomes much more when smokers are taken into account, let us check now for both smokers and non smokers together for variables age,no.of children and bmi

# In[ ]:


inputs,target=data[['age','bmi','children']],data['charges']


# In[ ]:


model=LinearRegression()


# In[ ]:


model.fit(inputs,target)


# In[ ]:


predictions=model.predict(inputs)
predictions


# In[ ]:


rmse(target,predictions)


# In[ ]:


print("Loss:",rmse(target,predictions))


# This shows that loss is much more when the whole dataset is taken into account , it can be also seen from the scatterplot too
# 

# In[76]:


sns.barplot(data=data,x='smoker',y='charges')


# In[77]:


smoker_code={'yes':1,'no':0}
data['smoker']=data['smoker'].map(smoker_code)


# In[78]:


gender_code={'female':0,'male':1}
data['sex']=data['sex'].map(gender_code)


# In[79]:


data


# In[80]:


inputs,target=data[['age','sex','bmi','children','smoker']],data['charges']


# In[81]:


model=LinearRegression()


# In[82]:


model.fit(inputs,target)


# In[83]:


predictions=model.predict(inputs)


# In[85]:


print("Loss:",rmse(target,predictions))


# When categorical columns are taken into account the loss decreases substantially , now let's check if region column has any effect on the predictions like others

# In[86]:


sns.barplot(data=data,x='region',y='charges')


# In[87]:


from sklearn import preprocessing
enc=preprocessing.OneHotEncoder()
enc.fit(data[['region']])
enc.categories_


# In[88]:


one_hot=enc.transform(data[['region']]).toarray()
one_hot


# In[89]:


data[['northeast', 'northwest', 'southeast', 'southwest']]=one_hot


# In[90]:


data


# In[91]:


inputs,target=data[['age','sex','bmi','children','smoker','northeast','northwest','southeast','southwest']],data['charges']


# In[92]:


model=LinearRegression()
model.fit(inputs,target)


# In[95]:


prediction=model.predict(inputs)


# In[96]:


rmse(target,prediction)


# The model does not improve much , we have to check if we can segregate the data on the basis of smokers and non smokers and then what impact it has on the predictions

# In[101]:


df_smoker=data[data['smoker']==1]
df_non_smoker=data[data['smoker']==0]


# In[102]:


df_smoker


# In[103]:


df_non_smoker


# In[105]:


target_smoker=df_smoker['charges']
target_non_smoker=df_non_smoker['charges']


# In[106]:


inputs_smoker=df_smoker[['age','sex','bmi','children','northeast','northwest','southeast','southwest']]
inputs_non_smoker=df_non_smoker[['age','sex','bmi','children','northeast','northwest','southeast','southwest']]


# In[107]:


model=LinearRegression()


# In[108]:


model.fit(inputs_smoker,target_smoker)


# In[109]:


predictions_smoker=model.predict(inputs_smoker)


# In[110]:


predictions_non_smoker=model.predict(inputs_non_smoker)


# In[112]:


print("Loss with multiple variables for smokers:",rmse(target_smoker,predictions_smoker))


# In[115]:


print("Loss with multiple variables for non smokers:",rmse(target_non_smoker,predictions_non_smoker))


# The predictions seem to be better for smokers than when the whole dataset is taken into account.
# 

# In[ ]:




