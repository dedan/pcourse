
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

And please please please, give me feedback. I will always try to improve this
lecture and for this I depend on your feedback. When programming for a long
time it is very hard to imagine the things that I did not understand when I
learned programming. I remember that I found it very confusing and also often
hard, but after a while you become so familiar to all this cryptic computer
things that it is hard to imagine the time when you did not understand them.
Hope the same happens to you in the end ;-)

[1]: http://en.wikipedia.org/wiki/Software_bug "Computer Bug"
[2]: http://stackoverflow.com/ "Programmer Forum"


Run a python file
=================

First I will show you the most simple python program ever and how to run it.
Type the following code in your editor, save it as `some_name.py` and run it
by calling python on the command-line. Type the name of your file after the
call to python on the command-line to tell python which file you want to run.
This is called "to give the filename as an *argument* to python".

```python
    # this line is not printed
    print("hello")
```

This code shows you two things. That text which starts with a `#` is not
executed. This is very useful to add text that explains your code (comments).
In the second line we call the `print` function with some text `"hello"` and
as expected: it prints the text. To call a function we write parenthesis after
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
become much longer already at the end of this lecture. But for evaluating
pieces you are not sure about, you can always paste it there from your editor.
E.g. you can play with the print function from the very first example:

    In [3]: print("hello")
    hello

    In [4]: print("hello Julia")
    hello Julia


Variables
=========

Let me introduce the concept of a variable by playing around with the first
example in which I printed the single word *hello*. As I said before we can
always learn a lot from errors. So lets try something and then look what we
can learn from the error. I remove the quotation marks from the word hello and
run the code again. To make it clear: I create a file (named *scratch.py* in
my case) containing the single line `print(hello)` and run it with the command
`python scratch.py`.

    (course)dedan@neuroinf37:~/projects/pcourse: python scratch.py 
    Traceback (most recent call last):
      File "scratch.py", line 1, in <module>
        print(hello)
    NameError: name 'hello' is not defined

This leads to an error, but python points us already in the right direction.
The output tells us that the mistake is in the first line of the file and that
we have to deal with a `NameError` because the name `hello` is not defined.
As always if you don't know what an error means (and they are often hard to
understand), just google it!. Here it means that python does not know the name
`hello` and this brings us to variables. Before we wrote "hello" which defines
short text with the content *hello*. But without the *""* python thinks a
variable is meant, but doesn't know one of this name at the moment.
**A variable just gives a label to an object**. Again abstract, here some code

```python
    # store the string "hello" in a variable
    var = "hello"
    print(var)
    var = "a whole sentence"
    print(var)
```

All the things we store in these variables are *objects*. This is important
because Python is an object-oriented programming language. But this should not
bother you now. We want to keep it intuitive and this is why I just show
you a few examples of the most important things (objects) we can put into
variables without talking about the theory of object-orientation:

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

It is a convention that the names of variables only contain small letters. You
can also use numbers in variable names, but they always have to begin with a
letter!

read input
==========

This is a very simple thing and I will just mention it briefly because we want
to use it in later examples. As a counter-part to the `print` function that
appeared previously, there is a function to *read in* information. It is
called `raw_input`. This is the name of the function and as I previously
mentioned, it is *called* or *executed* by writing its name plus parenthesis.
So to read in some text into a variable:

```python
    variable = raw_input()
    
    # or to ask a question on the commandline
    variable = raw_input("please type a word: ")
    print("you typed: ")
    print(variable)
```

Another difference between `print` and `raw_input` is that the latter is a
function with a *return value*. Calling `raw_input` asks you for some input
that you give it in the terminal. Then it *returns* the input that you gave
and you can assign it to a variable for using it later. Don't worry, the 
usage of `raw_input` will definitively become clear during this lecture. And
if not, never hesitate to ask. During lecture or when reading this script via
email to `stephan.gabler [ät] gmail.com`.

**important note!**  
When you want to read in a number instead of a name, you have to use:

```python
    variable = int(raw_input())
```

instead of:

```python
    variable = raw_input()
```

So for example when you want to ask someone for his age, and then continue in
your program depending on the number (for his age) that he entered, you have
to use the `int(raw_input())`. A application for this will become clear in the
chapter on `if` and you will also need this for your homework


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

decisions (if)
-------------

```python
    # the bouncer
    age = 14    # give 14 another name
                # this also gives a *meaning* to the number and makes it
                # more readable
    if age < 18:
        print("too hard for you")
    elif age < 21:
        print("hmmm, well.. OK")
    elif age > 99:
        print("too old!")
    else:
        print("ok, come in")
```

This piece of code shows a lot of new things again. First a number is
stored in a variable or in the terms I previously used: the number got an
additional name. Then the most important line `if age < 18:`. After the 
keyword `if` we always have to provide a python statement that can be either
`True` or `False` and this statement is then terminated by a colon. If the
statement evaluates to True, the block directly after the colon is executed,
if not, it checks whether the statement after `elif` (else if) evaluates to
True. If this is the case its block is executed and if not the else block is
executed. A block is any piece of code which has the same indentation. You
can write as many `elif` blocks as you want. `elif` and `else` blocks are
optional.


repetitions (for loop)
----------------------

```python
    for variable_name in [1, 8, 12, "test"]:
        print(variable_name)
```

*For loops* are very straightforward in python. It reads: For each element in
the provided list, store the element in the variable with the name
variable_name and then execute the given block.
As a rule of thumb: **For loops are always used if you know in advance how
often something has to be repeated**. To make it more clear what happens, the
following for loop does the same as:

```python
    variable_name = 1
    print(variable_name)
    variable_name = 8
    print(variable_name)
    variable_name = 12
    print(variable_name)
    variable_name = "test"
    print(variable_name)

```

You can immediately see that this would become very tedious to write for
longer lists and as I set in the beginning: Let computers do the boring stuff
and don't repeat yourself!



repetitions (while loop)
------------------------

```python
    # this is a bad example because we already know how often to do smth
    i = 0
    while i < 5:
        print(i)
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
* `ipython` has a very useful feature. If you write the name of a function
  followed by a `?` it will print the documentation of this function. So for 
  example if you don't remember what the `raw_string` function did exactly
  then go to you `ipython` window and type `raw_string?`.
* if you maybe wrote a program that does not end (for example with an
  infinite while loop like `while 1 == 1:`) you can always *kill* your
  programs by pressing `Ctrl` and `c` at the same time.
* if you are not sure about statements you want to use for a if condition you
  can always chat what the evaluate to in ipython. Try it.
  `age = 13`, `age < 20` `--> True` 


Homework
========

Play with the things you learned here today and please do the following tasks.
First try it without looking at the script. Write what you remember
and look at the errors. Let them guide you. Only use the script and the
internet if you cannot solve it alone.

For each homework I will give you at the end of a lecture, please create a new
folder on your hard-disk and call it `ex` plus the number of the lecture. So
`ex1` for this lecture. In this folder create a file for each of the tasks.
Either a file ending with `.py` for programs or with `.txt` if you have to
write an explanation. Please name them according to exercise and task number,
e.g. `ex1_1.py` for the first task of this first exercise.

1. print the numbers from 1 to 10 below each other. Don't just print a list
   containing those numbers.
  * hint: look up what the function `range` does
2. print your name 10 times
3. read in a number and give output depending on the number
  * you could e.g. write a variation of the *bouncer program*
4. read in information and store it in different variables. For example ask on
   the command-line for someones age, weight and size and then print all this
   information afterwards as a summary of the type: Your name is: bla and you
   are x old, etc..

NEVER copy and paste, type everything by yourself!

Again: Read the error message carefully. It often gives you very good hints
of where to find the error! It always tells you at least the line where the
error occurred.

Of course later you will use copy and paste and many other tools, but first
you have to learn your craft by typing typing typing and especially by doing
mistakes and afterwards fixing them



