def reverse(text):
    text=str(text)
    num=len(text)
    new=[]
    for i in range(num):
        add= text[num-(i+1)]
        new.append(add)
    nnn=''.join(new)
    #print nnn
    #print type(nnn)
    return nnn    
        
#reverse('abcdefg')

###############################################

def anti_vowel(text):
    new_string=[]
    for char in text:
        #print char
        if char in "aeiouAEIOU":
            new_string.append('')
            #print 'found a vowel'
        else:
            new_string.append(char)
            #print 'no vowel'
        #print new_string
    print ''.join(new_string)
        
        
        
anti_vowel('Hey look Words!')


###############################################
def scrabble_score(word):
         score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         values=[]
         word=word.lower()
         for char in word:
             val=score[char]
             values.append(val)
         #print values
         return sum(values)
             
         
       
scrabble_score('hello')






###############################################
def censor(text, word):
    cut=text.split()
    #print cut
    abc= len(cut)
    
    for num in range(abc):
        if cut[num] == word:
            a=len(cut[num])
            new="*"*a
            cut[num]=new
        else:
            cut[num]=cut[num]
    #print cut
    return " ".join(cut)
    
censor('hello there you big dog','dog')




###############################################

def count(sequence, item):
    if type(sequence[0]) == type(item):
        num= sequence.count(item)
        print int(num)
    else:
        if type(sequence[0]) == str:
            item=str(item)
        elif type(sequence[0]) == float:
            item=float(item)
        elif type(sequence[0]) == int:
            item=int(item)
        else:
            print 'what'
        num= sequence.count(item)
        print int(num)
    
  
  
  
  
  
  
  
count([1],7)
  
  
count([1,2,1,1,1],'1')

count(['bacon', 'eggs', 'cheese', 'eggs'],'eggs')




###############################################
def purify(nums):
    new_list=[]
    for num in nums:
        if num%2 == 0:
            #print num
            new_list.append(num)
        
            
    return new_list   
    

purify([1,2,3])


###############################################

def product(num):
    total=1
    for i in num:
        total *= i
    return total
         
          
product([1,4,3]) 
   
    
###############################################

def remove_duplicates(nums):
    result =[]
    for i in nums:
        if i not in result:
            result.append(i)
    print result
        
        
        

remove_duplicates([1,1,5,2])
###############################################
def median(nums):
    a=len(nums)
    new=sorted(nums)
    #print a,new
    if a%2 == 0:
        #print 'even'
        b=int(a/2)-1
        bb=int((a/2)) 
        #print b,bb
        return (new[b]+new[bb])/2.0       
    else:
        #odd
        b=int((a/2)+0.5)
        return new[b]
        
        
#median([7,12,3,1,6])
median([7,3,1,4])

 
###############################################
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

 
###############################################

 
###############################################

 
###############################################

 
###############################################

 
###############################################
 