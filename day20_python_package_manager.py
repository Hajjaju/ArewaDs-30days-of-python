import requests
import re
import statistics as stats

# Question 1: Read this url and find the 10 most frequent words.
# romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
print(response.status_code)
text = response.text
text = re.sub(r'[^\w\s]','',text)
words = text.split()
dict = {}
for r in words:
    if r in dict:
        dict[r] +=1
    else:
        dict[r] = 1

list = [(val,key) for key,val in dict.items()]
list.sort(reverse=True)

print(list[:10])
print()



# Question 2: Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :

url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
print(response.status_code)
cat_infor = response.json()

def stat_infor(lst, info):
    print(f"Max of cat's {info} in metric units is: {max(lst)}")
    print(f"Min of cat's {info} in metric units is: {min(lst)} ")
    print(f"Mean of cat's {info} in metric units is: {stats.mean(lst):.2f} ")
    print(f"Median of cat's {info} in metric units is: {stats.median(lst)} ")
    print(f"Std oof cat's {info} in metric units is: {stats.stdev(lst):.2f} ")

# the min, max, mean, median, standard deviation of cats' weight in metric units.
weight_in_metric = []
for i in range(len(cat_infor)):
    result = map(int, cat_infor[i]['weight']['metric'].split('-'))
    weight_in_metric.extend(result)
stat_infor(weight_in_metric, 'weight')
print()

# the min, max, mean, median, standard deviation of cats' lifespan in years.
life_span = []
for i in range(len(cat_infor)):
    result = map(int, cat_infor[i]['life_span'].split('-'))
    life_span.extend(result)
stat_infor(life_span, 'Life_span')   
print()

# Create a frequency table of country and breed of cats
freq_table = []
for i in range(len(cat_infor)):
    freq_table.append({'origin': cat_infor[i]['origin'], 'name':cat_infor[i]['name'] })

print('The frequency table of country and breed of cats')
print(freq_table)
print()


# Question 3: Read the countries API and find
# the 10 largest countries
# the 10 most spoken languages
# the total number of languages in the countries API

url =  'https://restcountries.eu/rest/v2/all'

#response = requests.get(url)
#print(response.status_code)
print(f'Site not accessible ({url})')
print()

# Question 4: UCI is one of the most common places to get data 
# sets for data science and machine learning. Read the content of UCL 
# (https://archive.ics.uci.edu/ml/datasets.php). Without additional
# libraries it will be difficult, so you may try it with BeautifulSoup4

from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
print(f"Site not accessible ({url}): {response.status_code}")
print()
