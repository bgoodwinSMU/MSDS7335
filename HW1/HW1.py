#########################
#      DS7335 HW1       #
#      Ben Goodwin      #
#      9/6/21           #
#########################

####Note####
# I commented out all of the print statements so that whoever views this won't be overwhelmed by output!
# If this isn't something you desire, please let me know and I will fix this!
# Thanks, 

####Imports
import string
import collections
import itertools
from collections import Counter
from itertools import *
from itertools import permutations
import matplotlib.pylab as plt
from itertools import combinations


#### List

##Build a dummy list
testList = ["Jane","Sally", "Irene"]

#Function 1, append()
#This function appends a value to a list
testList.append('Sheila')
#print(testList)


#Function 2, extend()
boyList = ["Rick","Stanley"]
testList.extend(boyList)
#print(testList)
#This function merges one list with another

#Function 3, index()
testList.index("Rick")
#print(testList[1])

#Function 4, index(value, integer)
#This function lets you search a list with a starting point
testList.index("Sally",0)


#Function 5, insert(position)
#This function allows you to insert a value at a given position.
testList.insert(1,"Rube")
#print(testList)

#Function 6, remove()
#This function removes a values from a list
testList.remove("Rick")

#Function 7, pop()
#This function by default removes the last item, "pops the stack" 
testList.pop()
#print(testList)

#Function 8, count()
#This function counts number of occuraces that a value occurs in a list
#print(testList.count('Rube'))

#Function 9, reverse()
#This function reverses the order of this list
testList.reverse()
#print(testList)

#Function 10, sort()
#This function by default sorts a list in ascedning order, can also specify order
testList.sort()
#print(testList)

#Function 11, [1]+[1]
#This function joins two lists

#Function 12, [2]*2
#This function duplicates a list

#Function 13, [1,2][1:]
#This function allows a users to retrieve a list from an index

#Function 14, [x for x in [2,3]]
#This function is a loop that iterates through the loop from position 2 to 3

#Function 15, [x for x in [1,2]if x==1]
#This line loops through the list between index 1 and 2 while looking for the value 1
#[y*2 for x in [1,2],[3,4] for y in x]
#This line is a loop that multiples whatever value is y by 2 inside a list of lists and then outputs a list 

#Function 16, A=[1]
#This function assigns the list to the variable A


#### Tuple

testTuple = ("Jane","Sally", "Irene")

#Function 17, count()
#This function counts the occurances of a certain value in a tuple
#print(testTuple.count("Jane"))

#Function 18, index()
#print(testTuple.index("Jane"))
#This function returns the index of a specified value

#Function 19, build a dictionary from tuples
#This function turns a list of tuples into a dictionary of tuples
tupleList = dict([('Jane', 1), ('Irene', 2), ('Rube', 3)])

#Function 20, unpack tuples
for n, v in tupleList.items():
   #added this line as to not disturb indents
    print()
    #print(n,v)
#This function unpacks the tuples- we will print out each value and key

#### Dicts:

#Function 21, a_dict= {'I hate':'you', 'You should':’leave’}
a_dict= {'I hate':'you', 'You should':'leave'}
#print(a_dict)
#This function defines a dictionary, this is indexed by a key, which can be any ummutable type; strings and numbers can always be keys
#There are many more rules with dictionaries, too many to get into here.

#Function 22, keys()
#print(a_dict.keys())
#This function prints the keys to the dictionary 

#Function 23, items()
#print(a_dict.items())
#This function prints the items within the dictionary

#Function 24, hasvalues()
#print(a_dict.hasvalues())
#Looks like this function may not exist in my current version of python.
#Will investigate
#This function was used to check for the presense of a key in a dictionary
#print('I hate' in a_dict)

#Function 25, _key()
#Looks like this function may not exist in my current version of python.
#Will investigate
#This line may help (below)
#print('I hate' in a_dict)

#Function 26, 'never' in a dict
#print('never' in a_dict)
#This function identifies if "never" is a key in the dict, so it returns false

#Function 27, del a_dict['me']
#del a_dict['me']
#This function should remove "me" from the dict as a key.  This throws an error

#Function 28, a_dict.clear()
#a_dict.clear()
#This function clears the dictionary

#Function 29, Ok enough by me do the rest on your own!
#use dir() to get built in functions***
#print(dir(dict))

##More dict functions
#print(a_dict.get("I hate"))
#This function gets the key at the value

#print(a_dict.items())
#This function prints out the items in the dict

#print(a_dict.keys())
#This function prints out the dict keys

#print(a_dict.pop("I hate"))
#This function pops the specified term

#print(a_dict.popitem())
#This function popos the top items

#print(a_dict.setdefault("I hate"))
#This function sets the default key

#print(a_dict.update())
#This function updates the dict

#print(a_dict.values())
#This function prints out all the values in the dict

####Sets:11

#Define a set
testSet = {"Jane","Sally", "Irene"}

#Function 30, add()
testSet.add("Rube")
#This function adds an element to a set
#print(testSet)
#Function 31, clear()
#testSet.clear()
#This function removes all elements from the set

#Function 32, copy()
set2=testSet.copy()
#Returns a shallow set of the copy

#Function 33, difference()
testSet.difference(set2)
#returns a set that is the difference between two sets

#Function 35, discard()
testSet.discard("Rube")
#Removes an element from the set

#Function 36, intersection()
#print(testSet.intersection(set2))
#Function looks at the intersection of two sets
#Function 37, issubset()
#print(set2.issubset(testSet))

#Function 38, pop()
testSet.pop()
#Pops the set element from the top of the stack

#Function 39, remove()
#testSet.remove("Sally")
#Removes a specified element from the set

#Function 40, union()
testSet.union(set2)

#Function 41, update()
testset2={"ben","dave"}
testSet.update(testset2)
#print(testSet)
#Updates the set
####Strings
teststring="BEN"
testString1="ben is cool"
#Function 42, capitalize()
#print(testString1.capitalize())
#Applies proper capitalization to string

#Function 43, casefold()
#print(teststring.casefold())
#retuns the lowercase version of a string

#Function 44, center()
#print(testString1.center(15))
#Justifies the string x characrters

#Function 45, count()
#print(testString1.count("b"))
#Counts occurances of char

#Function 46, encode()
#print(testString1.encode())
#method returns an encoded version of the given string.

#Function 47, find()
#print(testString1.find("b"))
#Returns first occurance of pattern

#Function 48, partition()
#print(testString1.partition("is"))

#method splits the string at the first occurrence of the argument string and returns a tuple containing the part the before separator, argument string and the part after the separator.

#Function 49, replace()
replaced_text = testString1.replace('b', 'c')
#print(replaced_text)
#method replaces each matching occurrence of the old character/text in the string with the new character/text.

#Function 50, split()
#print(testString1.split(' '))
# split the text from space

#Function 51, title()
#print(testString1.title())
#method returns a title cased version of the string. Meaning, the first character of each word is capitalized (if the first character is a letter).

#Function 52, zfill()
#print(testString1.zfill(5))
#method returns a copy of the string with '0' characters padded to the left.






flower_orders=['W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R/B','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','W/R','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','R/V/Y','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/N/R/V','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','W/R/B/Y','B/Y','B/Y','B/Y','B/Y','B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','R/B/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/N/R/B/V/Y','W/G','W/G','W/G','W/G','R/Y','R/Y','R/Y','R/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','N/R/V/Y','W/R/B/V','W/R/B/V','W/R/B/V','W/R/B/V','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','W/N/R/V/Y','N/R/Y','N/R/Y','N/R/Y','W/V/O','W/V/O','W/V/O','W/N/R/Y','W/N/R/Y','W/N/R/Y','R/B/V/Y','R/B/V/Y','R/B/V/Y','W/R/V/Y','W/R/V/Y','W/R/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/R/B/V/Y','W/N/R/B/Y','W/N/R/B/Y','W/N/R/B/Y','R/G','R/G','B/V/Y','B/V/Y','N/B/Y','N/B/Y','W/B/Y','W/B/Y','W/N/B','W/N/B','W/N/R','W/N/R','W/N/B/Y','W/N/B/Y','W/B/V/Y','W/B/V/Y','W/N/R/B/V/Y/G/M','W/N/R/B/V/Y/G/M','B/R','N/R','V/Y','V','N/R/V','N/V/Y','R/B/O','W/B/V','W/V/Y','W/N/R/B','W/N/R/O','W/N/R/G','W/N/V/Y','W/N/Y/M','N/R/B/Y','N/B/V/Y','R/V/Y/O','W/B/V/M','W/B/V/O','N/R/B/Y/M','N/R/V/O/M','W/N/R/Y/G','N/R/B/V/Y','W/R/B/V/Y/P','W/N/R/B/Y/G','W/N/R/B/V/O/M','W/N/R/B/V/Y/M','W/N/B/V/Y/G/M','W/N/B/V/V/Y/P']

#allocate memory for storage
doublelists = []
testlist = []
tripletCombinations = []
tripletPermutations = []


#Counter objects below
colcount = Counter()
flowerCounter = Counter()
paircounter = Counter()
tripletCounter = Counter()

#1. Build a counter object and use the counter and confirm they have the same values.


for flowers in flower_orders:
     flowerCounter[flowers] += 1

#print(flowerCounter)

#2. Count how many objects have color W in them.
#first convert from list of strings to list of lists
#testlist2 = []
#loop over list and deliminate by /
for word in flower_orders:
    #deliminate
    mylist = list(word.split("/")) 
    #testlist2 = []
    #print(testList2)
    #append to list
    doublelists.append(mylist)
    
#Another loop to iterate
wordCount = 0
for word in doublelists:
    wordCount += word.count('W')
#print(wordCount)

#3. Make histogram of colors

#Can use itertools to from iterable
mergeList = (itertools.chain.from_iterable(doublelists))
mergeList = list(mergeList)

#loop to iterate
for col in mergeList:
    colcount[col] += 1

colcount
colcountdict = dict(colcount)

plt.hist(colcountdict.values(),bins=10)
#plt.show()

#4. Rank the pairs of colors in each order regardless of how many colors are in an order.

#Remember to bring in imports from itertools
#Create some arrays for data stroage
paircombinations = []
pairpermutations = []

for i in range(len(mergeList)):
    combinations1 = combinations(mergeList[i], 0)
    #print(combinations1)
    permutations1 = permutations(mergeList[i], 1)
    #print(permutations1)
    #add to list
    paircombinations.append(list(combinations1))
    pairpermutations.append(list(permutations1))

combinationList = (itertools.chain.from_iterable(paircombinations))
combinationList = list(combinationList)
permutationsList = (itertools.chain.from_iterable(pairpermutations))
permutationsList=list(permutationsList)


for pairs in combinationList:
    paircounter[pairs] += 1
pair_dict = dict(paircounter )

#5. Rank the triplets of colors in each order regardless of how many colors are in an order.

#testListlen =len(testList)


#iterate over the test list (length)

for i in range(len(testlist)):
    
    #put the combinations1 variable set to the index of testlist at i,0
    combinations1 = combinations(testlist[i], 0)
    #put the combinations1 variable set to the index of testlist at i,1
    permutations1 = permutations(testlist[i], 1)
    #append to the list
    tripletCombinations.append(list(combinations1))
    tripletPermutations.append(list(permutations1))

bigtricombolist = (itertools.chain.from_iterable(tripletCombinations))
bigtricombolist = list(bigtricombolist)
#print(bigtricombolist)
bigtripermuslist = (itertools.chain.from_iterable(tripletPermutations))
bigtripermuslist = list(bigtripermuslist)
#print(bigtripermuslist)

#not entirely convinced this works correctly.




for pairs in bigtricombolist:
    tripletCounter[pairs] += 1
tridict = dict(tripletCounter)
#print(tridict)

#6. Make dictionary color for keys and values are what other colors it is ordered with.
#Just like in the dict section above
colorcountdict = dict(flowerCounter)
colorcountdict

# 7. Make a graph showing the probability of having an edge between two colors based on how often they co-occur.
#probability = how likely an event is to occur


for pairs in bigtricombolist:
    paircounter[pairs] += 1

totalProb= sum(pair_dict.values())
storedPercents = []

#Create dict to put colors with probabilties
probdict = {'Color':'Probability'}
#for loop with two variables to iterate through
for i, j in pair_dict.items():
    
    probPercent = v=j / totalProb * 100
    #print(probPercent)
    storedPercents=probPercent
    
    dictUpdate = {i:probPercent}
    
    #using the function from the dict section above
    probdict.update(dictUpdate)

pairOccur = list(paircounter)


#8. Make 10 business questions related to the questions we asked above.
#1) What are all the color combination possibilies that are possible?
#2) What are the colors that have never sold?
#3) What are the top three sellers?
#4) What are the bottom three sellers that aren't zero?
#5) Can you regress on the different colors and which are likely to sell given a new customer?
#6) Are most combinations of colors complementary to each other?
#7) What is the most combinations? Average? Min? Max? What is the shape?
#8) If there are two or more colors, what colors occur less often?
#9) What are the two most occuring number of combinations? Are they so dominant so that we should re-consider allowing different numbers?
#10) Can you predict which colors will sell with each other?



dead_men_tell_tales = ['Four score and seven years ago our fathers brought forth on this',
'continent a new nation, conceived in liberty and dedicated to the',
'proposition that all men are created equal. Now we are engaged in',
'a great civil war, testing whether that nation or any nation so',
'conceived and so dedicated can long endure. We are met on a great',
'battlefield of that war. We have come to dedicate a portion of',
'that field as a final resting-place for those who here gave their',
'lives that that nation might live. It is altogether fitting and',
'proper that we should do this. But in a larger sense, we cannot',
'dedicate, we cannot consecrate, we cannot hallow this ground.',
'The brave men, living and dead who struggled here have consecrated',
'it far above our poor power to add or detract. The world will',
'little note nor long remember what we say here, but it can never',
'forget what they did here. It is for us the living rather to be',
'dedicated here to the unfinished work which they who fought here',
'have thus far so nobly advanced. It is rather for us to be here',
'dedicated to the great task remaining before us--that from these',
'honored dead we take increased devotion to that cause for which',
'they gave the last full measure of devotion--that we here highly',
'resolve that these dead shall not have died in vain, that this',
'nation under God shall have a new birth of freedom, and that',
'government of the people, by the people, for the people shall',
'not perish from the earth.']

#allocate...
probdictdead = {}
probtransdict = {}


#1. Join everything

#Using the join command from the sections above
testString3  = " " 
testString3 = testString3.join(dead_men_tell_tales)

#2. Remove spaces

#using the replace command from the sections above
noSpace = testString3.replace(" ", "")


#3. Occurrence probabilities for letters
#total probability
totalProb2 = len(noSpace)
#use counter to count output from #2 
letter_counts = collections.Counter(noSpace)

#letter_counts

#throw into dict
letter_count_dict = dict(letter_counts)


#Iterate over
for k, l in letter_count_dict.items():
    
    percent = l / totalProb2 * 100
    
    dictUpdate2= {k:percent}
    
    probdictdead.update(dictUpdate2)


#4. Tell me transition probabilities for every letter pairs

#Count all
transProbs = Counter(zip(noSpace[:-1], noSpace[1:]))
transProbs=dict(transProbs)
totalProb3 = sum(transProbs.values())



for m, n in transProbs.items():

    probPercent = n / totalProb3 * 100
   
    dictUpdate3 = {m:probPercent}
    
    probtransdict.update(dictUpdate3)


#6. plot graph of transition probabilities from letter to letter
#sort the probs
sortedProbs = sorted(probtransdict.items()) 

#some data allocation
tup1, tup2 = zip(*sortedProbs) 
tupSeries = list(tup1)
finalList = [''.join(i) for i in tupSeries]

#create the plot
plt.bar(finalList, probtransdict.values())
#plt.show()

#7. Flatten a nested list

#List of lists
testList= [["sally","irene","rube"], ["betty","susie","sheila"], ["henry"], ["ben","dave"]]
merged = list(itertools.chain(*testList))
