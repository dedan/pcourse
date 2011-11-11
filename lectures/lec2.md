

Last time we learned
--------------------

* how to print and read
* how to store something in a variable
* control structures
    * if (elif, else)
    * for loop
    * while loop

I would like to go on as soon as possible but also see that this stuff is all
really complicated in the beginning and we should maybe deepen your knowledge
of the basics before we go on, to make it not too confusing. Please always
let me know if it is going too fast.


Short comment on functions with a return value
----------------------------------------------

As I mentioned in the last lecture, there are some function that just do
something (e.g. the print function) and other function that return a value.
Actually most of the functions return a value. You already used a few of them,
for example `raw_input()`, `range()` and `int()`. Two things to mention.

* In any place where you need what a function returned, you can directly write
the function. An example to make that more clear. If you need a list of
numbers you can use the `range()` function that returns you a list. One option
is to store this list in a variable and then use it later (e.g. in a `for
loop`). But you don't have to put it into a variable first. You can just write
the function in the place where you need the list. Because its return value is
a list, you can actually treat it like a list. See the following code.

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

But be careful, this can also make your code very hard to read if you do it
too much. Chain your function when you don't need the return values in
variables, but store them in variables if it improves readability of your
code. Readability is very important and it makes your code much more readable
if you give reasonable names to your variables.


More on for loops
-----------------

Last time I showed you how to iterate over a list. Iteration over something
is such a basic concept in python that I would like to talk about this a
little bit more. The `for variable_name in something` syntax might confuse you
in the beginning so I will try to explain it again. It means to one after
another take each *element* from the *something*, then call it variable_name
and execute the block. It is called by a name (variable_name) so that you can
refer to it within the block. Maybe it becomes more clear if we rename the
variables in a way that it sounds more intuitive. If we just use the right
words it already sounds like a natural description of a task. The task could
be to do something *for all elements in a list*, *for all letters in a word*
or for *all lines in a file*. This sounds like natural language, right? Now
let's have a look how this is done in python.

What I did not tell you last time, is that we cannot only use lists in a for
loop. In python a for loop is much more general and can be applied to
everything that is *iterable*. I will not show you how to create new iterables
(this is quite advanced), but give you a few examples of them and then it will
become clear that we can use them without knowing anything about them.

As always, type the code I present here into an editor (Yes, type!) and let it
run.

```python
    name = raw_input("whats your name? ")
    for letter in name:
        print(letter)
```

This first example shows that also a string is an iterable. We can *iterate*
over it and it gives us all the elements it consists of, one at a time. And
you see, if you assign reasonable names to your variables, it almost sounds
like the natural language phrases I mentioned before (*for all letters in a
name*).


```python
    name = raw_input("whats your name? ")
    fav_letter = raw_input("what is your favourite letter? ")

    counter = 0
    for letter in name:
        if letter == fav_letter:
            counter = counter + 1

    print("your name contains your favourite letter")
    print(counter)
    print("times")
```

The second example asks you for two strings. A name and your favorite letter.
Then it again iterates over a string. But this time it does not simply print
each letter. Each letter is compared with the *favorite letter* and its
occurrences are counted. At the end the total number of occurrences is
printed.

One important comment on the line where the counter is increased. Beginners
often tend to write `counter + 1` instead of `counter = counter + 1`. Why is
that wrong? It is not really wrong, it just does not do what you want! If you
write `counter + 1` it computes the sum of the previous value and the new
value. But then, it throws it away. In order to *remember* it we have to store
it in a variable. And because we want to use the value again in the next
iteration, we just store it back in the old variable. Therefore -> `counter =
counter + 1`.


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

Again, type the code into your editor and this time very important: save it as
**commenter.py**. This program does something very interesting and maybe also
confusing. But I will help you reading it step by step.

1. Open a file with the `open()` function. In many other courses you learn how
to deal with files very late because in other languages it is something quite
complicated. But as I show you here. If you know how to deal with iterables,
you can already work with files. What open does is: opening the file with the
name that is given to it as a string. We can then iterate over the text in
this file as we were able to iterate over the elements of a list or the
letters of a string. The funny and maybe confusing thing is: here the program
opens itself and reads its own code ;-) If this confuses you, give the `open`
function the path to another python file and see what happens. You have to
give the whole path if the file is not in the same folder as the program, e.g.
`/home/stephan/python_course/example_code.py`.
2. Read the file line by line and do something with every line in the
following block.
3. Here we learn something new again, the bracket notation to access elements
of a list or string. This will be explained in the next paragraph.
4. Print the lines which start with the `#` comment letter.


random access to list elements
------------------------------

As seen in the previous example, single elements of lists or strings can be
accessed with the *square bracket notation*. See the following example in
which I show you an ipython session in which I played with lists. Explanations
in comments behind each line.


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


The square bracket notation can be used to access elements of a list. This is
also what was done in the previous example when we checked each line of a text
file whether it starts with the comment symbol. Especially note the last line
of the ipython session. This shows that the notation can also be chained
analogously to functions. The return value does not have to be stored in a
variable. If the thing that we took from a list supports the bracket notation
again (e.g. a string) we can directly write the next brackets.

The bracket notation cannot only be used to access elements of a list but also
to change elements. !!! **this does not work with strings** !!! they are
immutable. Note that in ipython print is not needed to see the content of a
variable.

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

* In the terminal and also in ipython you can use the tab key to complete your
  input. For example if you are in a folder with a python program that has a
  long and complicated name, just type `python lon` and it will expand to
  `python long_and_complicated_name.py`. If there is not only a single file
  which fits the letters you already typed, the terminal will show you which
  files are still remaining and you have to type a few more letters before you
  hit tab again. This also works with function names in ipython. Try it by
  writing first only `pr` and hit tab. It will show you all functions that
  start with *pr*. If you write `pri` it is already unambiguous and will
  expand to `print`. This is very useful. Just try it by hitting tab all the
  time ;-)

[1]: https://raw.github.com/dedan/pcourse/master/exercises/bugsearch1.py "ex2"