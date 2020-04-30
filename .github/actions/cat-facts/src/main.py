import requests
import random
import sys

# Make an HTTP GET request to the cat-fact API
cat_url = "https://cat-fact.herokuapp.com/facts"
r = requests.get(cat_url)
r_obj_list = r.json()["all"]

# Create an empty array, populate it with cats
fact_list = []
for fact in r_obj_list:
    fact_list.append(fact["text"])

# create function to get a random fact
def select_random_fact(fact_arr):
    return fact_arr[random.randint(0, len(fact_list) + 1)]


random_fact = select_random_fact(fact_list)

# Print the random cat fact
print(random_fact)

# Set the fact-output of the action as the value of random_fact
print(f"::set-output name=fact::{random_fact}")
