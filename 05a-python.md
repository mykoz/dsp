# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both a series of values. Lists are created using ```[]``` while tuples are created with ```()```. Lists can be modified (appended to, delete entries). Tuples are immutable and its contents cannot be altered. It is also for the reason of being immutable that tuples can be used as keys in dictionaries. This guarantees that the contents will provide exactly one hash value, avoiding unexpected errors.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists ,`[]`, and Sets, `set([])`  are both a collection of items and are both mutable. The difference is lists are indexed and subject to sequencing behaviors while sets are unordered. Sets also cannot contain duplicate elements.
``` 
list = ['a','b','c','d']
exset = set(['c', 'd', 'e', 'f'])
```
When it comes checking for membership of an element, sets are faster because they're implemented as hash tables. This means when checking if an element is in the set, it only needs to check at the position of the hash of that element. A list needs to check through the entire list to verify membership.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda is an anonymous function, which is an function unbound to any identifiers. Basically defines a function on one line. Using lambda can also make your code look a bit cleaner. It's commonly used in functions that take two arguments in the form of `(function, sequence)` such as map(), reduce(), and filter(). 
```
things = ['c4t', 'z1t', 'p3t' ,'d0g','b2d']
print sorted(things, key = lambda x: x[1]) #sorted arguments sorted(list,cmp= key= reverse=)
```
This sorts the elements of `things` by the second character. `key=` requires a function that gives each value a proxy value to sort by. `lambda` provides this without the need to make an actual function

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are another concise way to apply a function for a collection of items. 
Syntax is [*expression* for *var* in *list*] in between f

Basic example:
```
stuff = ["hi","this", "is", "a", "sentence"]
print [len(n) for n in stuff]
```
`map()` applies a given function to all elements of an iterable and returns the result. it is similar to a list comprehension and can be faster in select situations.
`print map(len(), stuff)`

`filter()` filters a list by a specified attribute. 

`print filter(lambda x: len(x) > 3, stuff)` #finds all elements longer than len == 3 and makes a new list. Should be noted that in a list comprehension, an additional `if` can serve as a filter eg. `[ x+1 for x in list1 if x%2==0]`

A set comprehension creates a new set by using the same syntax of a list comprehension in braces instead of brackets.
` {x**2 for x in range(10)}`

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





