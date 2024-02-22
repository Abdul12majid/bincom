from bs4 import BeautifulSoup
import re
import random
import statistics
# import requests

# response = requests.get(
#     'https://drive.google.com/open?id=1nf9WMDjZWIUnlnKyz7qomEYDdtWfW1Uf')

dataFile = open('dataFile.html')
soup = BeautifulSoup(dataFile.read(), 'html.parser')
elements = soup.select('td')

colours = []


for index in range(1, 10, 2):
    text = re.sub('\n*\s*', '', elements[index].getText().strip())
    colours.extend(text.split(','))

colourCount = {}

for colour in colours:
    if colour not in colourCount:
        colourCount[colour] = 1
    else:
        colourCount[colour] += 1

# Preparing for calculation by sorting color count
colourCount = sorted(colourCount.items(), key=lambda x: x[1])
colourCount = dict(colourCount)

# Calculating Mean
mean = sum(colourCount.values())/len(colourCount)

total = 0
for colour in colourCount:
    total += colourCount[colour]
    if mean < total:
        meanColour = colour
        break
print(f'1. Mean colour is {meanColour}')

# Mode
print(f'2. Mostly worn colour is {list(colourCount.keys())[-1]}')

# Median
median = sum(colourCount.values())/2
total = 0
for colour in colourCount:
    total += colourCount[colour]
    if median < total:
        medianColour = colour
        break
print(f'3. Median colour is {medianColour}')

# Variance
variance = statistics.variance(colourCount.values())
print(f'4. Variance of the colours is {variance}')

# Probability that a colour is red
probability = colourCount['RED']/sum(colourCount.values())
print(f'5. Probability of a colour selected at random being red {probability}')