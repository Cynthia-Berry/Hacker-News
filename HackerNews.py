#!/usr/bin/env python
# coding: utf-8

# # PROJECT ON HACKER NEWS

# `Hacker News` is a site started by the startup incubator Y Combinator, where user-submitted stories (known as "posts") are voted and commented upon, similar to reddit. Hacker News is extremely popular in technology and startup circles, and posts that make it to the top of Hacker News' listings can get hundreds of thousands of visitors as a result.
# 
# We're specifically interested in posts whose titles begin with either `Ask HN` or `Show HN`. Users submit Ask HN posts to ask the Hacker News community a specific question.
# We'll compare these two types of posts to determine the following:
# 
# Do `Ask HN` or `Show HN` receive more comments on average?
# Do posts created at a certain time receive more comments on average?
# 

# In[1]:


from csv import reader
opened_file = open('hacker_news.csv')
read_file = reader(opened_file)
hn = list(read_file)

print(hn[:5])


# In[2]:


header = hn[0]
hn = hn[1:]

print(header)
print('\n')
print(hn[:5])


# ### Extracting `Ask HN` and `Show HN`
# 

# In[3]:


ask_posts = []
show_posts = []
other_posts = []

for row in hn:
    title = row[1]
    if title.lower().startswith('ask hn'):
        ask_posts.append(row)
    elif title.lower().startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)
        
print(len(ask_posts))
print('\n')
print(len(show_posts))
print('\n')
print(len(other_posts))



# In[4]:


print(ask_posts[:3])
print('\n')
print(show_posts[:3])
print('\n')
print(other_posts[:3])


# ### Calculating the Average Number of Comments for `Ask HN` and `Show HN` Posts

# In[5]:


total_ask_comments = 0
for value in ask_posts:
    num_comment = value[4]
    num_comment = int(num_comment)
    total_ask_comments  += num_comment  

avg_ask_comments = total_ask_comments / len(ask_posts)
print(avg_ask_comments)

print('\n')

total_show_comments = 0
for value in show_posts:
    num_comment = value[4]
    num_comment = int(num_comment)
    total_show_comments += num_comment   

avg_show_comments = total_show_comments / len(show_posts)
print(avg_show_comments)


# ### Finding the Amount of Ask Posts and Comment by Hour Created
# 

# * Calculate the amount of ask posts created in each hour of the day, along with the number of comments received.
# * Calculate the average number of comments ask posts receive by hour created.

# In[6]:


import datetime as dt
result_list = []

for value in ask_posts:
    temp = []
    temp.append(value[6])
    temp.append(value[4])
    result_list.append(temp)
print(result_list[:6])

    
counts_by_hour = {}
comments_by_hour = {}
date_format= "%m/%d/%Y %H:%M"

for row in result_list:
    date_hour=row[0]
    comment= int(row[1])
    time=dt.datetime.strptime(date_hour, date_format).strftime("%H")
    
    if time in counts_by_hour:
        counts_by_hour[time] += 1
        comments_by_hour[time] += comment
    else:
        counts_by_hour[time]=1
        comments_by_hour[time]= comment
        
print('\n')
print(counts_by_hour)
print('\n')
print(comments_by_hour)
    


# ### Calculating the Average Number of Comments for `Ask HN` Posts by Hour

# Above, we created two dictionaries:
# 
# * counts_by_hour: contains the number of ask posts created during each hour of the day.
# * comments_by_hour: contains the corresponding number of comments ask posts created at each hour received.
# 
# Next, we'll use these two dictionaries to calculate the average number of comments for posts created during each hour of the day.

# In[7]:


avg_by_hour = []
for value in comments_by_hour:
    avg_by_hour.append([value, comments_by_hour[value]/ counts_by_hour[value]])

print(avg_by_hour)


# In[8]:


swap_avg_by_hour = []
for value in avg_by_hour:
    swap_avg_by_hour.append(value)
    
print(swap_avg_by_hour)
print('\n')
'''
SORTING 
 To successfully sort the second colum (index 1) you nned to specify 
 the key attribute in your sorted method.
 The below solutions worked perfectly
 (solution was gotten from python documentation on how to use SORTED())

* sorted_swap = sorted(swap_avg_by_hour,key=lambda average: average[1],reverse = True)
*  from operator import itemgetter
# sorted_swap = sorted(swap_avg_by_hour,key=itemgetter(1), reverse = True)
 
'''

from operator import itemgetter
sorted_swap = sorted(swap_avg_by_hour,key=itemgetter(1), reverse = True)

print(sorted_swap)


# '''
# CONVERTING AND FORMARTING AVERAGE AND DATETIME
# '''
# print("Top 5 Hours for Ask Posts Comments")
# 
# date_format = "%H"
# for element in sorted_swap[:5]:
#     hour = dt.datetime.strptime(element[0], date_format).strftime("%H")
#     print("{time}:00 : {value:.2f} average comments per post".format(time=hour, value=element[1]) ) 
#   
#     

# In[9]:


'''
CONVERTING TIME TO WEST AFRICA TIME ZONE(NIGERIA)
    The original time zone was Eastern Standard.
    Here I am converting to GMT+1 by adding 7 hours.
'''
print("Top 5 Hours for Ask Posts Comments (WAT)")

date_format = "%H"
for element in sorted_swap[:5]:
    hour = dt.datetime.strptime(element[0], date_format)
    hour_in_WAT = hour - dt.timedelta(hours=5)
    hour_in_WAT = hour_in_WAT.strftime("%H")
    print("{time}:00 : {value:.2f} average comments per post".format(time=hour_in_WAT, value=element[1]) ) 
  


# #### COMMENT
# I noticed that for active engagement to questions posted using the `Ask HN` clause, queationa ahould be posted between the below time in GMT+1:
# 
# * 10:00-11:00 (10AM-11AM)
# * 15:00-16:00 (3PM-4pm)
# * 21:00 (9PM)
# 

# In[ ]:




