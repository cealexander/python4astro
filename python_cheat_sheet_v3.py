# -*- coding: utf-8 -*-
#===========================================================
# running a python program/notes
#===========================================================

# python programs end in .py
# to start python and work in the terminal type >>>python (>>> = prompt, don't type)
# from your terminal you can run a prewritten prog using: python myprog.py
# or you can use enthought canopy to run your code


# indentation is very important! Not just for looking good - codes will throw error.


#===========================================================
# importing packages
#===========================================================
# import these at the start of your program to be able to call certain things

import math                             # be able to use math packages
import matplotlib.pyplot as plt         # call the package something else for ease.

import sys,os                           # import system details in order to e.g. stop program, change directories etc.

import numpy as np
import scipy as sp                      # must import system last, allows you to change directories within the script
import matplotlib.pyplot as plt         # pyplot most commonly used
import sys,os                           # allows you to stop…sys.exit()  ;equivlene t to idl stop              

#===========================================================
# commenting and strings
#===========================================================

''' is a block comment that can go over many lines'''
# is a comment

print    # prints an empty line
print "Hello"
print 'hello'                                                # print strings using either " or '. Be consistent.
print 'Simulation no. \t Temperature \t Density'             #\t will put a tab in to nicely space things out.
print 'Let\'s start the party'                               # you need a backshlash before apostrophes in text


# get string info
my_string = "Hello you!"
print len(my_string)
print my_string.upper()
print my_string.lower()


# use placeholders to input stings with %s (%s = string, %d = integer, %f = float)
string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

# change things into strings
pi=3.14
print 'The value of pi is '+ str(pi) 



# string operations

stuff = '   Hello you!  '                        # define a string
type(stuff)                            # tells you what type of variable it is
dir(stuff)                             # gives you list of things you can do with stuff
stuff.capitalize()                     # capitalize first letter
stuff.startswith('x')                  # prints true or false
stuff.find('e')                        # tells you where it finds it. -1 if not there
stuff.lstrip()                         # strips from left
stuff.rstrip()                           # strips from right
stuff.strip()                            # strips form left and right
stuff.upper()                            # changes to upper case
stuff.lower()                            # changes to lower case

#Create String Array
array = ['one', 'two', 'three'] 

#Convert String to Numerical Values
for i, value in enumerate(array):
    print "{0} : {1}".format(i, value)


#Modifying Exsisting String
#strings are immutable, which means you can’t change an existing string. The best you can do is create# a new string that is a variation on the original:



>>> greeting = 'Hello, world!'
>>> new_greeting = 'J' + greeting[1:]
>>> print new_greeting
Jello, world!



#Manipulating (Splitting ) Strings

abc= 'With three words'
stuff =abc.split()
print stuff

line='first;second;third'
thing=line.split(';')



#Using Find 
text = "X-DSPAM-Confidence:    0.8475"
num=text.find('0')
print text[num :]



#Counting strings and Creating Loops using Strings

# indefinite loop:

fruit = 'banana'
index =0
while index < len(fruit):
    letter = fruit[index]
    print index, letter
    index = index + 1

# definite loop

fruit = 'banana'
for letter in fruit:
    print letter

# counting

word = 'banana'
count = 0

for letter in word:
    if letter == 'a':
        count = count +1
print count

# string indexing

# the string 'Hello' is 5 characters going from index 0 to 4
# to select all you:

mystring= 'Hello'
print mystring

print mystring[0:2] # will print the H and e as it is up to but not including the last index

print mystring[-1] # will print the last character 'o'
print mystring[-3:] # will print 'llo' i.e. 3rd last to end.



#===========================================================
# math operators
#===========================================================

# regular operators + add - subtract / divide * multiply
# note ** is power of, not ^
print 2**2


nums=[1,2,3,4,5]
print len(nums)
print max(nums)
print min(nums)
print sum(nums)
print sum(nums)/len(nums)

# difference between = and == : first is to assign value. second is to compare (used in if statements mostly)

import math             # need to import math package 
print math.sqrt(25)

#or
from math import sqrt    # just import the function you need

# find out what math does/has
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

#===========================================================
# lists/arrays
#===========================================================

# example 1: 
start_list = [5, 3, 1, 2, 4]
square_list = []                   # makes an empty list

for number in start_list:                # loop over elements in start_list
    square_list.append(number ** 2)      # add each number squared to empty list
square_list.sort()                       # sort the list
print square_list


#-------------------------
# example 2:

x=arange(0,100)                          # similar to IDL findgen
print x 



#===========================================================
# functions
#===========================================================
# define a function so you don't have to repeat code:
# example:

def triangle_area(base, height):     # header - ends in colon, shows inputs
    area = (1.0 / 2) * base * height # body - all of body is indented
    return area                      # body - return outputs value

# how to call function
a1 = triangle_area(3, 8)
print 'area of triangle 1: ',a1
a2 = triangle_area(14, 2)
print 'area of triangle 2: ',a2




#===========================================================
# while
#===========================================================

# example 1: 
numlist=list()                          #make empty list
while True:
    inp=raw_input('enter a number:')    # get user to input number
        if inp == 'done': break         # if they type 'done' quit
        value = float(inp)              # change to floats
        numlist.append(value)           # add each number to list
        
average = sum(sumlist)/len(numlist)     # work out the average
print,'average: ',average


# example 2:
n=5
while n > 0:
	print n
	n=n-1
print "blastoff"


#===========================================================
# if elif else
#===========================================================

# example code to print out grade
grade=raw_input("Type grade: ")
grade=float(grade)
if grade >=0.9 and grade <= 1.0:
    print 'A'
elif grade >=0.8 and grade < 0.9:
    print 'B'
elif grade >=0.7 and grade <0.8:
    print 'C'
elif grade >=0.6 and grade <0.7:
    print 'D'
elif grade <0.6 and grade >=0.0:
    print 'F'
else:
    print "invalid input"


# example to work  out odd or even. % operator gives you a remainder.
if x%2 == 0 :
    print 'x is even'
else :
    print 'x is odd'
#===========================================================
# for
#===========================================================
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print 'Happy New Year:', friend
print 'Done!'

#===========================================================
# try, except
#===========================================================

# will try something i.e. check a number/file and if it's not there/the right type it won't crash but will go to the except.
inp = raw_input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print cel
except:
    print 'Please enter a number'





#===========================================================
# useful things
#===========================================================
# get user to input text/number
rawstr = raw_input('Enter a number: ')


#===========================================================
# IDL similar hacks
#===========================================================
sys.exit()  # is like an idl stop

#get info on variables in memory (IDL = help)
whos

# for selecting a bunch of files with similar names e.g. fits files then printing out the name
import glob
import sys,os
fdir ='home/documents/data/'
filenames=sorted(glob.glob(fdir + 'file*'))
for file in filenames:
    print os.path.basename(file)
 
#===========================================================
#Reading/Writing Files
#===========================================================

open(filename,mode)

handle = open('mbox.txt','r') # read is normal. This gives it a link doesn't put in memory

#newline character

stuff = 'Hello\nWorld'  #counts as one character  #\n means pause or newline/linebreak


xfile = open('mbox.txt')
for line in xfile:
    print line
    
    
fhand = open('mbox.txt')
count =0
for line in fhand:
    count = count +1
    
print count

# read short files

fhand = open('sss.txt')
inp = fhand.read()
print len(inp)   # number of characters
print inp[ :10]   # first 10 characters not lines

# searching through a file

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()    # remove the extra newlines
    if line.startswith('From:'):
        print line

# flipped version

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()    
    if not line.startswith('From:'):
        continue
        print line



fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()    
    if not '@uct.ac.za' in line:
        continue
        print line



#prompt for file name

fname=raw_input('enter the file name: ')
fhand = open(fname)
count=0
for line in fhand:
    if line.startswith('Subject:');
        count=count+1
print 'There were',count,'subject lines in',fname

#prompt for file name - bad file names

fname=raw_input('enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'that aint no filename', fname
    exit()
count=0
for line in fhand:
    if line.startswith('Subject:');
        count=count+1
print 'There were',count,'subject lines in',fname


#===========================================================
# Writing Files
#===========================================================
To write a file, you have to open it with mode 'w' as a second parameter:

>>> fout = open('output.txt', 'w')
>>> print fout
<open file 'output.txt', mode 'w' at 0xb7eb2410>
If the file already exists, opening it in write mode clears out the old data and starts fresh, so be careful! If the file doesn’t exist, a new one is created.

The write method of the file handle object puts data into the file.

>>> line1 = "This here's the wattle,\n"
>>> fout.write(line1)
Again, the file object keeps track of where it is, so if you call write again, it adds the new data to the end.

We must make sure to manage the ends of lines as we write to the file by explicitly inserting the newline character when we want to end a line. The print statement automatically appends a newline, but the write method does not add the newline automatically.

>>> line2 = 'the emblem of our land.\n'
>>> fout.write(line2)
When you are done writing, you have to close the file to make sure that the last bit of data is physically written to the disk so it will not be lost if the power goes off.

>>> fout.close()
We could close the files which we open for read as well, but we can be a little sloppy if we are only opening a few files since Python makes sure that all open files are closed when the program ends. When we are writing files, we want to explicitly close the files so as to leave nothing to chance.


import glob
fdir ='home/documents/data/'
filenames=sorted(glob.glob(fdir + 'file*'))
for file in filenames:
    print os.path.basename(file)
    



pyArt - look up
pyplot?


os.path exist? look up
