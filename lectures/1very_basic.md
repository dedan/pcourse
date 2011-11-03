
First Lecture 
=============

In the first lecture we already have to cover a lot to do something
cool soon. As mentioned in the introduction of LPTHW, please never
copy and paste code from the lecture slides or the exercises to your editor.
It is important that you type code again and again, that you make mistakes,
that you have [bugs][1] in your code and that you learn how to fix them. The
mistakes and learning how to read the error messages, that python gives you,
is very important. The error messages are sometimes quite cryptic, but then
just copy and google them. With a very high probability someone had the same
problem before. A very good programmers forum is [StackOverflow][2].

[1]: http://en.wikipedia.org/wiki/Software_bug "Computer Bug"
[2]: http://stackoverflow.com/ "Programmer Forum"


Run a python file
=================

First I will show you the most simple python program ever and how to run it.
Type the following code in your editor, save it as `some_name.py` and run it
by calling python on the command-line. Type the name of your file after the
call to python on the command-line to tell python which file you want to run.
This is called "to give the filename as an *argument* to python".

    # this line is not printed
    print("hello")

This code shows you two things. That text which starts with a `#` is not
executed. This is very useful to add text that explains your code. In the
second line we call the `print` function with some text `"hello"` and as
expected: it prints the text. To call a function we write parenthesis after
its name. The things we write within the parenthesis are the *arguments*
that we pass to the function.


Ipython
=======

Ipython is an interactive python interpreter. It allows you to interact and
talk to python. Sounds abstract, so look at a short example. Start ipython
by typing `ipython` on your terminal. You see ipython starting and then the
prompt of the terminal changes. You can now input python code which will be
interpreted line by line. You can make ipython execute any python code, but 
it is mostly used to evaluate short pieces (one-liners) of code. You could
even use it as a kind of calculater:

    (course)dedan@neuroinf37:~/projects/course: ipython
    Python 2.7.1 (r271:86832, Jun 16 2011, 16:59:05) 
    Type "copyright", "credits" or "license" for more information.

    IPython 0.11 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]: 6*7
    Out[1]: 42

    In [2]: 16 / 2 + 5
    Out[2]: 13

For the one-liner we have previously seen it is tedious to always save it to
a file. I still want you to write everything in files because the code will
become much longer already at the end of this lecture. Put for evaluating
pieces you are not sure about, you can always paste it there from your editor.
E.g. you can play with the print function from the very first example:

    In [3]: print("hello")
    hello

    In [4]: print("hello Julia")
    hello Julia


Variables
=========

Let me introduce the concept of a variable by playing around with the previous
example. As I said before we can always learn a lot from errors. To lets try
something and then look what we can learn from the error.

    (course)dedan@neuroinf37:~/projects/pcourse: python scratch.py 
    Traceback (most recent call last):
      File "scratch.py", line 1, in <module>
        print(hello)
    NameError: name 'hello' is not defined

This leads to an error, but python points us already in the right direction.
The output tells us that the mistake is in the first line of out file and that
we have to deal with a `NameError` because the name `hello` is not defined.
As always if you don't know what an error means (and they are often hard to
understand, just google it!). Here it means that python does not know the name
`hello` and this brings us to variable. Before we wrote "hello" which defines
short text with the content *hello*. But without the *""* python thinks a
variable is meant, but doesn't know one of this name at the moment.
**A variable just gives a label to an object**. Again abstract, here some code

    # print hello will not work
    var = "hello"
    print var
    var = "a whole sentence"
    print var

All the things we store in these variables are *objects*. This is important
because Python is an object-oriented programming language. But this should not
bother you now. We want to keep it intuitive and this is why I just show
you a few examples of most important things (objects) we can put into
variables without talking about theory of object-orientation:

* text -> strings
* numbers
* lists
* ...

And again a few examples:

    a_number = 42
    print a_number
    a_float_number = 4.2
    print
    some_text = "this is some text"
    a_list_of_things = [42, "some_text", a_number]


control structures
==================

Finally we come to the most important thing in programs. The control
structures which control the flow of your program. They allow you to make
decisions and to repeat boring stuff. We have computers to do the boring stuff for us. The repetitive boring stuff. As soon as you find yourself during
programming doing something very boring and repetitive (copy pasting code,
repeating numbers, etc.) you most probably do something wrong!!! We are good
in reasoning, computers are good in mindlessly repeating boring tasks. So let
them be done by computers.

Having said this, we have to learn how to repeat stuff in python and how to
make decisions.

decisions (f)
-------------

    # the bouncer
    age = 14    # give 14 another name
                # this also gives a *meaning* to the number and makes it
                # more readable
    if age < 18:
        print "too hard for you"
    else:
        print "ok, come in"


repetitions (for loop)
----------------------

    for var in [1, 8, 12, "test"]:
        print var

repetitions (while loop)
------------------------


    # this is a bad example because we already know how often to do smth
    i = 0
    while i < 5:
        print i
        i = i + 1

    # this is much better
    text = ""
    while not text == "the right answer":
        text = raw_input("please give the right answer: ")
        
    
* if
* read input


play with the things you learned here today

tasks

* print the numbers from 1 to 10
* print your name 10 times
* read in a number and give output depending on the number



things we learn during this lecture:

* a function/command gets its parameters in parenthesis
* text (programmers call it a *string*) that you use in your program code
  has to be delimited by `"`
* text that starts with a `#` is a comment and will not be executed
* comments are important to make your code understandable
    * understandable to you, when you look at it the next time
    * and understandable to others, usually you program in groups
* with variables you can assign names to things.
* if `condition`: executes the following block only if `condition` is *true*
* a `block` is defined by its indentation
* use `for .. in` in combinations with blocks to repeat things
* always use *for loops* if you know how often something has to be repeated
* use a while loop only if you don't know how often you have to do something
* `=` is for variable assignment
* `==` is for equality comparisons

hints:

* the *arrow-up* key goes back in the terminal and ipython history so you
  don't have to type in all the things again, if you want to modify a command.


