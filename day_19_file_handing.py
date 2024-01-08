import re
# Question 1:Write a function which count number of lines and number of words in a text.

def count_lines_and_words(text):
    with open(r"day_019\data\\" + text, 'r',) as file:
        lines = file.read()
        count = 0
        for _ in str(lines).split():
            count += 1

        return lines, count


def verify(function, *texts):
    for text in texts:
        first, *rest = text.split("_")
        line , count = function(text)
        print(f"{first.capitalize()}, the number of lines is {len(line)} and total words is {count}")

verify(count_lines_and_words, "obama_speech.txt", "michelle_obama_speech.txt","donald_speech.txt","melina_trump_speech.txt")

# Question 2:Read the countries_data.json data file in data directory, 
# create a function that finds the ten most spoken languages
import json

def json_most_frequent_word(data, n):

    with open(data, encoding="cp437", errors='ignore') as file:
        lines = json.loads(file.read())

        most_spoken = {}

        for i in range(len(lines)):

            for j in range(len(lines[i]['languages'])):
                language = lines[i]['languages'][j]

                if language not in most_spoken:
                    most_spoken[language] = 1
                else:
                    most_spoken[language] += 1


        list = [(val,key) for key,val in most_spoken.items()]
        list.sort(reverse=True)
        print('The most frequent words in the json file are:')
    return list[:n]


print(json_most_frequent_word('day_019\data\countries_data.json', 3))  
print()

# Question 3: Read the countries_data.json data file in data directory, 
# create a function that creates a list of the ten most populated countries

def ten_most_pop_countries(data, n):

    with open(data, encoding="cp437", errors='ignore') as file:
        lines = json.loads(file.read())
        lst = []
        for line in lines:
            lst.append({'country': line['name'], 'population':line['population']})

        newlist = sorted(lst, key=lambda d: d['population'], reverse=True)

        return newlist[:n]


print(ten_most_pop_countries('day_019\data\countries_data.json', 3))
print()

"""Exercises: Level 2
"""
# Question 4: Extract all incoming email addresses as a list from the email_exchange_big.txt file.
pattern = r"[a-zA-Z0-9]\S*@\S*[a-zA-Z]"
email = []
with open(r'day_019\data\email_exchange_big.txt', 'r') as file:
    lines = file.read()
    result = re.findall(pattern, lines)
    print(list(result))
print()

# Question 5: Find the most common words in the English language.
# Call the name of your function find_most_common_words, it will 
# take two parameters - a string or a file and a positive integer, 
# indicating the number of words. Your function will return an array 
# of tuples in descending order. Check the output

def find_most_common_words(text, n):

    with open('day_019\data\\' + text) as file:
        lines = file.read().replace(',', '')

        new_result = re.sub('[\W]', ' ', lines)
        dict = {}
        for r in new_result.split():
            if r in dict:
                dict[r] +=1
            else:
                dict[r] = 1

        list = [(val,key) for key,val in dict.items()]
        list.sort(reverse=True)

        return list[:n]


# Question 6: Use the function, find_most_frequent_words to find: 
def verify_most_feq(*text):
    for i in text:
        first, *rest = i.split("_")
        print(f'{first}, the must freqent words {find_most_common_words(i, 10)}')

verify_most_feq("obama_speech.txt", "michelle_obama_speech.txt","donald_speech.txt","melina_trump_speech.txt")
print()
# Question 7: Write a python application that checks similarity between two texts. 
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
# For instance check the similarity between the transcripts of Michelle's and Melina's speech. 
# You may need a couple of functions, function to clean the text(clean_text), function to remove 
# support words(remove_support_words) and finally to check the similarity(check_text_similarity).
# List of stop words are in the data directory
from stop_words import stop_words

def clear_text(text):

    with open('day_019\data\\' + text) as file:
        lines = file.read().replace(',', '')
        new_result = re.sub('[\W]', ' ', lines)

        return new_result.lower().split(" ")


def remove_support_words(text):
    clean_text = []
    for word in text:
        if word not in stop_words:
            clean_text.append(word)
    return clean_text


def check_text_similarity(text1, text2):

    clean_text_1 = clear_text(text1)
    remove_stop_word_1 = remove_support_words(clean_text_1)

    clean_text_2 = clear_text(text2)
    remove_stop_word_2 = remove_support_words(clean_text_2)

    total_text = remove_stop_word_1 + remove_stop_word_2

    result = [x for x in total_text if x in clean_text_1 and x in clean_text_2]

    similarity = (len(result) / (len(remove_stop_word_1) + len(remove_stop_word_2))) * 100 
    t1, t2 = text1.split('_')[0], text2.split('_')[0]

    return f'The speech similarity of {t1} and {t2} is: {similarity:.2f}%'

print(check_text_similarity("michelle_obama_speech.txt", "melina_trump_speech.txt"))
print()

# Question 8: Find the 10 most repeated words in the romeo_and_juliet.txt
print(f'Juliet and Romoe must repeated words')
print(find_most_common_words('romeo_and_juliet.txt', 10))
print()

# Question 9: Read the hacker news csv file and find out: 
import csv

def count_words(file, pattern):
    with open(file) as f:
        csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
        line_count = 0
        for row in csv_reader:
            result = ' '.join(row)
            find = re.findall(pattern, result, re.I)
            if len(find) > 0:
                #print(find)
                line_count += 1

    return f'Number of lines for {pattern}:  {line_count}'

# a) Count the number of lines containing python or Python
print(count_words('day_019\data\hacker_news.csv', 'python'))
# b) Count the number lines containing JavaScript, javascript or Javascript 
print(count_words('day_019\data\hacker_news.csv', 'JavaScript'))
# c) Count the number lines containing Java and not JavaScript
print(count_words('day_019\data\hacker_news.csv', 'Java'))
print()