



from math import sqrt
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('https://data.melbourne.vic.gov.au/resource/277b-wacc.csv')
# look at the DataFrame
data.head()


# In[2]:


# some columns are totaly useless
data.drop([col for col in ['mac', 'boardtype', 'position', 'model', 'rowid'] if col in data], 
        axis=1, inplace=True)
data.head()


# In[5]:


len(data[data.temp_max == data.temp_min])


# In[3]:


a = len(data.temp_max)
b = len(data.temp_min)
c = len(data.temp_avg)
if b == a == c:
  print("They have equal length")
else:
  print("they have different length")


# In[4]:


#Drop some columns ['humidity_min', 'humidity_max', 'temp_max', 'temp_min', 'light_min','light_max']
data.loc[:, ~data.columns.isin(['humidity_min', 'humidity_max', 'temp_max', 'temp_min', 'light_min','light_max'])]


# In[48]:


print(len (data['location']))
print(data['location'].unique())


# In[50]:


print(len(data[data.location == 'Fitzroy Gardens']))


# In[51]:


print(len(data[data.location == 'Docklands Library']))


# In[43]:


print(data['boardid'].sort_values().unique())


# In[7]:


for location in data.location.unique():
    print(location)


# In[66]:


print("Borad_IDs for the first location, 'Fitzroy Gardens'  ",data[data.location == "Fitzroy Gardens"].boardid.sort_values().unique())
print("Borad_IDs for the second location, 'Docklands Library'  ", data[data.location == "Docklands Library"].boardid.sort_values().unique())


# In[6]:


def count_median(data):
    _data = sorted(data)
    length = len(_data)
    i = int(length/2)
    if length % 2 == 0:
        return (_data[i] + _data[i-1]) / 2
    else:
        return _data[i]


def count_standard_deviation(numbers):
    mean = sum(numbers)/float(len(numbers))

    return sqrt(sum([(i - mean) ** 2 for i in numbers]) / (len(numbers)-1))


# In[8]:


boards_Fitzroy = data[data.location == "Fitzroy Gardens"].boardid.sort_values().unique()

print("\t\t\t\tTemperature Calculation at Fitzroy Gardens\n")
for board in boards_Fitzroy:
    my_median = count_median(data[data.boardid == board].temp_avg)
    my_std = count_standard_deviation(data[data.boardid == board].temp_avg)
    print("Board_number",board ,          "\tmy_median","{:.2f}".format(my_median),          "\tOrignal_median","{:.2f}".format(data[data.boardid == board].temp_avg.median()),          "\tmy_stddev","{:.2f}".format(my_std),          "\tOrignal_stddev","{:.2f}".format(data[data.boardid == board].temp_avg.std()),      )


# In[159]:


boards_Fitzroy = data[data.location == "Fitzroy Gardens"].boardid.sort_values().unique()

print("\t\t\t\tTemperature Calculation at Fitzroy Gardens\n")
for board in boards_Fitzroy:
    my_median = count_median(data[data.boardid == board].light_avg)
    my_std = count_standard_deviation(data[data.boardid == board].light_avg)
    print("Board number",board ,         "\tMy_median","{:.2f}".format(my_median),          "\tOrignal_median","{:.2f}".format(data[data.boardid == board].light_avg.median()),          "\tmy_stddev","{:.2f}".format(my_std),          "\tOrignal_stddev","{:.2f}".format(data[data.boardid == board].light_avg.std()),      )


# In[166]:


boards_Docklands_Library = data[data.location == "Fitzroy Gardens"].boardid.sort_values().unique()

print("\t\t\t\tHumidity Calculation at Fitzroy Gardens\n")
for board in boards_Docklands_Library:
    my_median = count_median(data[data.boardid == board].humidity_avg)
    my_std = count_standard_deviation(data[data.boardid == board].humidity_avg)
    print("Board_number",board ,          "\tMy_median","{:.2f}".format(my_median),          "\tOrignal median","{:.2f}".format(data[data.boardid == board].humidity_avg.median()),          "\tmy_stddev","{:.2f}".format(my_std),          "\tOrignal stddev","{:.2f}".format(data[data.boardid == board].humidity_avg.std()),      )


# In[156]:


boards_Docklands_Library = data[data.location == "Docklands Library"].boardid.sort_values().unique()

print("\t\t\t\tTemperature Calculation at Docklands Library\n")
for board in boards_Docklands_Library:
    my_median = count_median(data[data.boardid == board].temp_avg)
    my_std = count_standard_deviation(data[data.boardid == board].temp_avg)
    print("Board_number",board ,          "\tOrignal_median","{:.2f}".format(my_median),          "\tOrignal_median","{:.2f}".format(data[data.boardid == board].temp_avg.mean()),          "\tmy_stddev","{:.2f}".format(my_std),          "\tOrignal_stddev","{:.2f}".format(data[data.boardid == board].temp_avg.std()),      )


# In[165]:


boards_Fitzroy = data[data.location == "Docklands Library"].boardid.sort_values().unique()

print("\t\t\t\tLight Calculation at Docklands Library\n")
for board in boards_Fitzroy:
    my_median = count_median(data[data.boardid == board].light_avg)
    my_std = count_standard_deviation(data[data.boardid == board].light_avg)
    print("Board_number",board ,          "\tMy_median","{:.2f}".format(my_median),          "\tOrignal_median","{:.2f}".format(data[data.boardid == board].light_avg.median()),          "\tmy_stddev","{:.2f}".format(my_std),          "\tOrignal_stddev","{:.2f}".format(data[data.boardid == board].light_avg.std()),      )


# In[164]:


boards_Docklands_Library = data[data.location == "Docklands Library"].boardid.sort_values().unique()

print("\t\t\t\tHumidity Calculation at Docklands Library\n")
for board in boards_Docklands_Library:
    my_median = count_median(data[data.boardid == board].humidity_avg)
    my_std = count_standard_deviation(data[data.boardid == board].humidity_avg)
    print("Board_number",board ,          "\tMy_median","{:.2f}".format(my_median),          "\tOrignal_median","{:.2f}".format(data[data.boardid == board].humidity_avg.median()),          "\tmy_stddev","{:.2f}".format(my_std),          "\tOrignal_stddev","{:.2f}".format(data[data.boardid == board].humidity_avg.std()),      )


# In[13]:


s = pd.to_datetime(data.timestamp)
print(s)


# In[115]:


get_ipython().run_line_magic('time', "data['ts'] = pd.to_datetime(data.timestamp)")
data.ts.describe()


# In[125]:


import string
import numpy as np
import random
mystring = "bgryw"
def random_string(length):
    return "".join(random.choice(mystring) for m in range(length))


# In[158]:


loc_filter = data[data.location == "Fitzroy Gardens"].boardid.sort_values().unique()
color = random_string(1)
for loc in loc_filter:
    plt.figure(figsize=(18,5))
    my_string = "bgrcmykw"
    i = random.randint(0,4)
    l = my_string[i]
    x = data[data.boardid == loc].ts
    y = data[data.boardid == loc].temp_avg
    plt.plot(x, 
             y, c = l)
    plt.ylabel('Temperature')
    plt.xlabel('Time')
    plt.suptitle('Visualisation for Fitzroy Gardens')
    plt.show()


# In[159]:


# model
loc_filter = data[data.location == "Docklands Library"].boardid.sort_values().unique()

for loc in loc_filter:
    
    my_string = "bgrcmykw"
    i = random.randint(0,4)
    l = my_string[i]
    plt.figure(1, figsize=(18,5))
    #plt.figure(figsize=(18,5))
    x = data[data.boardid == loc].ts
    y = data[data.boardid == loc].temp_avg
    plt.plot(x, 
             y, c = l)
    plt.ylabel('Temperature')
    plt.xlabel('Time')
    plt.suptitle('Visualisation for Docklands Library')
    plt.show()
         


# In[192]:


#Plot the median of the boards at Fitzroy Gardens

loc_filter = data[data.location == "Fitzroy Gardens"].boardid.sort_values().unique()
color = random_string(1)
for loc in loc_filter:
    plt.figure(figsize=(18,5))
    my_string = "bgrcmykw"
    i = random.randint(0,4)
    l = my_string[i]
    temp = data[data.boardid == loc].temp_avg
    y = count_median(temp)
    plt.axhline(y, c=l, linestyle='-')
    plt.ylabel('Median temperature')
    plt.xlabel('Borad Number' + ' ' +format(loc))
    plt.suptitle('Visualisation for Fitzroy Gardens')
    plt.show()


# In[193]:


#Plot the median of the boards at Docklands Library

loc_filter = data[data.location == "Docklands Library"].boardid.sort_values().unique()
color = random_string(1)
for loc in loc_filter:
    plt.figure(figsize=(18,5))
    my_string = "bgrcmykw"
    i = random.randint(0,4)
    l = my_string[i]
    temp = data[data.boardid == loc].temp_avg
    y = count_median(temp)
    plt.axhline(y, c=l, linestyle='-')
    plt.ylabel('Median temperature')
    plt.xlabel('Borad Number' + ' ' +format(loc))
    plt.suptitle('Visualisation for Docklands Library')
    plt.show()


# In[195]:


#Attention this a just repetition of plot nr1 above 
loc_filter = data[data.location == "Fitzroy Gardens"].boardid.sort_values().unique()
color = random_string(1)
for loc in loc_filter:
    plt.figure(figsize=(18,5))
    my_string = "bgrcmykw"
    i = random.randint(0,4)
    l = my_string[i]
    x = data[data.boardid == loc].ts
    y = data[data.boardid == loc].temp_avg
    plt.plot(x,              y,              ',', c=l, alpha=.9)
    plt.ylabel('Temperature')
    plt.xlabel('Time')
    plt.suptitle('Visualisation for Fitzroy Gardens')
    plt.show()


# In[161]:


#Attention this a just repetition of plot nr2 above 
loc_filter = data[data.location == "Docklands Library"].boardid.sort_values().unique()
color = random_string(1)
for loc in loc_filter:
    plt.figure(figsize=(18,5))
    my_string = "bgrcmykw"
    i = random.randint(0,4)
    l = my_string[i]
    x = data[data.boardid == loc].ts
    y = data[data.boardid == loc].temp_avg
    plt.plot(x,              y,              ',', c=l, alpha=.9)
    plt.ylabel('Temperature')
    plt.xlabel('Time')
    plt.suptitle('Visualisation for Docklands Library')
    plt.show()

