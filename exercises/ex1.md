
Intro
-----

Please read the exercise completely and carefully. In the end of it I will try
to give you some hints and help with all the stuff which is probably all new
and confusing to you.
This first exercise does not contain any programming. You first have to
install a few things. But don't worry, we use a very simple setup in this
course. I recently found a book that I really really like and where I wish
that I have had such a book when I learned programming. The book is called
*Learn Python the hard way* (LPTHW) and there is a free version available
[here][1].
I can highly recommend it and regularly refer to it during the course. If you
are an autodidact you can basically just work on this excellent book. However
I still recommend you doing my course because I will try to give you more
insights on:

* why we are doing this
* what programming is good for
* teach from the perspective of a scientist
* try to give interesting examples
* provide more exercises and also feedback on your solutions

Please never hesitate to ask any questions, during the lectures or via email
to `stephan.gabler [ät] gmail.com`


So, let's start:
----------------

1. Read the introduction of [learn python the hard way][2], I really like the
attitude of the guy on how we learn things.

2. Do the [first exercise of LPTHW][3] which helps you setting up your system
   for the more interesting stuff we start doing in the first lecture. In this
   exercise you learn how to setup your system, install a good editor and how
   to navigate through your filesystem on the command-line (the geeky way of
   using a computer).

3. Install `ipython` by writing the following on your command-line:

    `pip install ipython`

after installation you can use it as you learned in Step 2, by just writing
the name of the application on the command-line. If you have problems with
the installation, check the `ipython` [website][4] or ask me in the next
class.


Remarks
-------

From the first person who did this course I got feedback that in the beginning
it is very confusing to understand what the terminal (synonymously called
shell and command-line) is good for. Especially confusing seams to be the fact
that there is no graphical user interface to python - meaning that no window
opens to work with this program. Nevertheless it is a normal program, just not
a graphical one and this seams to be confusing for people who grew up with
windows, etc. The terminal is a more *old-school* way of working with
computers. Maybe it reminds some of you to working with DOS. And thats right,
the idea is the same. You type in commands to tell your computer what to do.
The terminal gives you access to functionality like browsing the file system
(like the Explorer in Windows or the Finder on a Mac) or to execute programs.
You navigate the file system with the following commands:

* `ls`: list all the files in a directory
* `cd`: **c**hange **d**irectory (move to another folder)
* `pwd`: **p**rint **w**orking **d**irectory 
  (print the path of the folder you are in)

In order to execute a program, you just have to type its name. You type
`python` to run python and you type `python path/to/a/file.py` to call
python with a program you wrote as an argument. This will execute your
program. But you can also execute your editor via the terminal. Just type
`gedit` to open the text editor or type `gedit path/to/a/file.py` to edit
one of your programs. It might also confuse people what the editor is. It is,
as the name says, a program that allows you to edit text. Nothing more,
nothing less. It is like *Word* or any other *Word processor* but for much
simpler texts without any formatting. One important hint: `gedit` allows you
to set [syntax highlighting][5] which makes it much easier for you to read and
understand your code. [Short explanation here][6]

So as a short summary:

* the **terminal** gives you access to the operating systems functionality. It
  gives you to ability to do all the things that you usually do via a
  graphical user interface, like starting programs, open folders and files, ..
* the **editor** allows you to modify the text of your programs
* **python** is a program that you open via the terminal, giving it the path
  to a program that you want to run. Note that opening a program does not
  mean that a window has to open. It runs in the terminal, asks you for input
  on the terminal and gives its output on the terminal. `ls` and `cd` are
  examples for other programs that run on the terminal.


[1]: http://learnpythonthehardway.org "Free online version"
[2]: http://learnpythonthehardway.org/book/intro.html "Introduction"
[3]: http://learnpythonthehardway.org/book/ex0.html "First Exercise"
[4]: http://ipython.org/ "Ipython website"
[5]: http://en.wikipedia.org/wiki/Syntax_highlighting "Syntax Highlighting"
[6]: http://library.gnome.org/users/gedit/stable/gedit-syntax-highlighting.html.en "Set Syntax highlighting"