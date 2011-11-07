
First Lecture 
=============

* many things, interesting from the next lecture on
* never copy paste -> make mistakes
* google error messages
* stackoverflow.com


Run a python file
=================

```python
    # this line is not printed
    print("hello")
```

shows

* comments
* how to call a function (arguments)

Ipython
=======

* what it is good for
* evaluate one liners
* experiment
* use it as a calculator

Variables
=========

* introduce by removing "" from the hello world
* show how the error helps us
* variable gives a name to an object

```python
    # print hello will not work
    var = "hello"
    print var
    var = "a whole sentence"
    print var
```

* everything is an object
* what objects can we store in variables
    * text -> strings
    * numbers
    * lists
    * ...

And again a few examples:

```python
    a_number = 42
    print a_number
    a_float_number = 4.2
    print(a_number)
    some_text = "this is some text"
    a_list_of_things = [42, "some_text", a_number]
    print(a_list_of_things)
```


read input
==========

* how to use the raw_input function

```python
    variable = raw_input()
    
    # or to ask a question on the commandline
    variable = raw_input("please type a word: ")
    print("you typed: ")
    print(variable)
```


control structures
==================

* we have computers to do the stupid stuff
* don't repeat yourself

decisions (if)
-------------

```python
    # the bouncer
    age = 14    # give 14 another name
                # this also gives a *meaning* to the number and makes it
                # more readable
    if age < 18:
        print "too hard for you"
    else:
        print "ok, come in"
```

shows

* store number in variable
* evaluation of *truth*
* block


repetitions (for loop)
----------------------

```python
    for variable_name in [1, 8, 12, "test"]:
        print variable_name
```

*For loops* are very straightforward in python. It reads: For each element in
the provided list, store the element in the variable with the name
variable_name and then execute the given block.
As a rule of thumb: **For loops are always used if you know in advance how
often something has to be repeated**


repetitions (while loop)
------------------------

```python
    # this is a bad example because we already know how often to do smth
    i = 0
    while i < 5:
        print i
        i = i + 1
```

```python
    # this is much better
    text = ""
    while not text == "the right answer":
        text = raw_input("please give the right answer: ")
```

The while loop is used when you have to repeat something but you don't know
how often this has to be done. While the statement that you gave after the
keyword `while` is true, the following block is executed over and over.


things we learned during this lecture
=====================================

* a function/command gets its parameters in parenthesis
* text (programmers call it a *string*) that you use in your program code
  has to be delimited by `"`
* text that starts with a `#` is a comment and will not be executed
* comments are important to make your code understandable
    * understandable to you, when you look at it the next time
    * and understandable to others, usually you program in groups
* with variables you can assign names to things.
* if `condition`: executes the following block only if `condition` is *true*
* a `block` is a piece of code with the same indentation
* use `for .. in` in combinations with blocks to repeat things
* always use *for loops* if you know how often something has to be repeated
* use a while loop only if you don't know how often you have to do something
* `=` is for variable assignment
* `==` is for equality comparisons

hints:

* the *arrow-up* key goes back in the terminal and ipython history so you
  don't have to type in all the things again, if you want to modify a command.


Homework
========

Play with the things you learned here today and please do the following tasks.
First try it without looking at the script. Write what you remember
and look at the errors. Let them guide you. Only use the script and the
internet if you cannot solve it alone.

1. print the numbers from 1 to 10
  * hint: look up what the function `range` does
2. print your name 10 times
3. read in a number and give output depending on the number
  * you could e.g. write a variation of the *bouncer program*
4. read in information and store it in different variables. For example ask on
   the command-line for someones age, weight and size and then print all this
   information afterwards as a summary of the type: Your name is: bla and you
   are x old, etc..

NEVER copy and paste, type everything by yourself! 

Of course later you will use copy and paste and many other tools, but first
you have to learn your craft by typing typing typing and especially by doing
mistakes and afterwards fixing them



