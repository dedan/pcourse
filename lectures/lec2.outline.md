

Last time we learned
--------------------

* how to print and read
* how to store something in a variable
* control structures
    * if (elif, else)
    * for loop
    * while loop

* we continue a bit slower than in the first lecture


Short comment on functions with a return value
----------------------------------------------

* some functions have a return value

* In any place where you need what a function returned, you can directly write
the function. 

```python
    list_of_numbers = range(10)
    for number in list_of_numbers:
        print(number)
```

```python
    for number in range(10):
        print(number)
```

* Because of the first point, functions can be *chained*. You don't have to
  store the return value anywhere, you can just pass it to the next function.

```python
    # old style code
    number_string = raw_input("give me a number: ")
    number_int = int(number_string)
    range_list = range(number_int)
    for number in range_list:
        print(number)
```

```python
    # all functions chained
    for number in range(int(raw_input("give me a number: "))):
        print(number)
```

* this can make your code ugly!!!


More on for loops
-----------------

* explain for in syntax again
* give examples for how this could be said in natural language
* The task could be to do something *for all elements in a list*, *for all
letters in a word* or for *all lines in a file*. 

* what are iterables
* why iterables already now?

```python
    name = raw_input("whats your name? ")
    for letter in name:
        print(letter)
```

* string is iterable
* reasonable variable names makes reading very easy


```python
    name = raw_input("whats your name? ")
    fav_letter = raw_input("what is your favorite letter? ")

    counter = 0
    for letter in name:
        if letter == fav_letter:
            counter = counter + 1

    print("your name contains your favourite letter")
    print(counter)
    print("times")
```

make comment on the assignment of counter

Beginners often tend to write `counter + 1` instead of 
`counter = counter + 1`.

```python
    # open a file
    open_file = open("commenter.py")

    # iterate over all the lines in a file
    for line in open_file:

    # check whether the first letter in the line is a comment
        if line[0] == "#":

    # if yes, print it
            print(line)
```

* program opens itself with open function
* because iterables are used so consistently in python we can already read files
* !!! opens itself!
* always reads a line and then executes the block
* check first element of line



random access to list elements
------------------------------

introduce square bracket notation


    In [23]: a_list = range(10) # first create a list
    In [24]: print(a_list) # print it to make sure whats in there
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    In [25]: print(a_list[5]) # print the sixth value in the list
    5

    In [26]: # note that indexing in python always starts from 0 !!!
    In [27]: print(a_list[0]) # print the first value in the list
    0

    In [28]: another_list = ["horst", "willi", 5]
    In [29]: print(another_list[1]) # second value of other list
    willi

    In [30]: bla = another_list[1] # store the 2nd value of the list in a var
    In [31]: print(bla) # print the variable
    willi

    In [32]: # so bla is the string that was the second value of the list.
    In [33]: # we previously saw that we can iterate over a string, can we
               also access single elements?

    In [34]: print(bla[0]) # yes we can! the first element (note: index is 0)
    w

    In [35]: print(bla[3]) # the forth element
    l

    In [36]: print(bla[5]) # and this will lead to an error because only 5 
                             elements exist
    IndexError                              Traceback (most recent call last)
    /Users/dedan/projects/fu/<ipython-input-36-7fbcbfbacc14> in <module>()
    ----> 1 print(bla[5])

    IndexError: string index out of range
    
    In [37]: print(another_list[1][0]) # as with functions, we don't have to            
                                         store it in a intermediate variable
    w


square bracket chaining

* can also be used for assignment in lists (or other not immutable things)
* strings are immutable!

    In [41]: another_list
    Out[41]: ['horst', 'willi', 5]

    In [42]: another_list[0] = "depp"

    In [43]: another_list
    Out[43]: ['depp', 'willi', 5]


More printing and string formatting
-----------------------------------

```python
    # a little string formatting
    name = raw_input('what is your name, my friend? ')

    # print with an empty string prints an empty line
    print("")
    # print a string
    print("nice to meet you: ")
    # print the string in a variable
    print(name)
```

This costs three lines of code for very simple output ;-(

This is not what a programmer wants and luckily there are some special and
nice constructs which help you formatting a string

* special characters 
    * \n: line break 
    * \t: tab
* formatting strings 
    * %s: placeholder for a string
    * %d: placeholder for an integer number 
    * %f: placeholder for a float number (with comma)
* the formatting operator %

A few examples in the following code listing:

```python
    # line break before output
    print("\n nice to meet you: ")

    # line-break before output and after output
    print("\n nice to meet you: \n")

    # tab before output and line-break afterwards
    print("\t nice to meet you: \n")


    # the %s can be replaced by a string
    print("nice to meet you: %s" % name)

    # %d can be replaced by a integer number (natural number)
    # and %f by a float number (a number with a comma)
    print("an integer number (%d) in the middle of a string" % 10)
    print("same thing with a float (%f) in the middle of a string" % 10.8)

    # when you use more then one value, you have to wrap them in parenthesis
    print("hello, my name is %s and I am %d years old" % ("horst", 6))

    # store a string in a variable and format it later
    string_with_missing_parts = "a name (%s) and an integer number: %d"
    complete_string = string_with_missing_parts % (name, 100)
    print(complete_string)
```


Homework
--------

From this lecture on I ask you to keep a list of things that you already
learned. Please write down all the terms and symbols that you learned,
together with a short explanation of what it does or means. The one of last
week could start with:

* `print`: Print text on the terminal (print("text to print"))
* `""`: wrap this symbols around text to make it a string ("text")
* `variable`: you can store a value in a variable, name a value
* ...

And now the real homework. Don't forget: For each homework create a new folder
on your hard-disk and call it `ex` plus the number of the lecture. So `ex2`
for this lecture. In this folder create a file for each of the tasks. Either a
file ending with `.py` for programs or with `.txt` if you have to write an
explanation. Please name them according to exercise and task number, e.g.
`ex2_1.py` for the first task of this first exercise. At the end, compress the
folder and send it to me via email.

1. Download the following [short python program][1] and follow the task
   description in the comments of that file. Download it by 
   `right-click -> save`
2. Open a file and count how many lines of text it has
3. Do the last exercise of lecture 1 again, but use the new printing method
4. Write a program that asks you for ten names and stores them in a list.
   Print the list in the end. Because this is a quite complex task, I will
   give you a few hints
    1. create a variable containing an empty list
    2. what kind of loop should be used if you know how often to do something?
    3. in each iteration: ask for a name and append it to the previously empty          
       list. You don't know how to append? Google `python list append`!
5. Copy the code from task 4 in a new file (yes, this one single time it is
   allowed to copy). Extend the program that it in the end iterates over
   the created list and prints for each entry of the list a line like
   `the first letter of the name Stephan is S`
    1. Use the bracket notation to access single elements of a list
    2. use the new printing methods
    3. this task should be done in two additional lines of code
6. play around with strings, what happens if you apply plus or times to a
   string
    1. operators behave differently for different functions try out
       multiplication and addition of strings in ipython `print("-" * 50)`
       print("hallo" + " stephan")


hints
-----

* tabs in the terminal
