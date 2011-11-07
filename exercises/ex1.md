Intro
-----

Please read the exercise completely and carefully. In the end of it I will try to give you some hints and help with all the stuff which might be all new and confusing to you.
This first exercise does not contain any programming. You first have to install a few things. But don't worry, we use a very simple setup in this course. I recently found a book that I really, really like and I wish that I had had such a book when I learned programming. The book is called *Learn Python the hard way* (LPTHW) and there is a free version available [here][1].
I highly recommend it and I will regularly refer to it during the course. If you are an autodidact you can basically just work with this excellent book. However, I still recommend you to participate in my course, because I will try to give you more insights on:

* why we are doing this
* what programming is good for
* teach from the perspective of a scientist
* try to give interesting examples
* provide more exercises and also feedback on your solutions

Please never hesitate to ask any questions, during the lecture or via email to `stephan.gabler [ät] gmail.com`

So, let's start:
----------------

1. Read the introduction of [learn python the hard way][2], I really like the attitude of the guy on how we learn things.

2. Do the [first exercise of LPTHW][3], which helps you setting up your system  for the more interesting stuff we will start doing in the first lecture. In this  exercise you learn how to setup your system, how to install a good editor and how to navigate through your filesystem on the command-line (the geeky way of using a computer)

3. Install `ipython` by writing the following on your command-line:

    `pip install ipython`

After installation you can use it as you learned in Step 2, just by writing the name of the application on the command-line. If you have problems with the installation, check the `ipython` [website][4] or ask me in the next class.


Remarks
-------

From the first person who took this course I got feedback that in the beginning it is very confusing to understand what the terminal (synonymously called shell and command-line) is good for. Especially confusing seams to be the fact that there is no graphical user interface to python - meaning that no window opens pops up with this program. Nevertheless, it is a normal program, just not a graphical one and people who grew up with windows, etc might need to get used to it. The terminal is a more *old-school* way of working with computers. Maybe it reminds some of you of working with DOS. And thatís right, the idea is the same. You type in commands to tell your computer what to do. The terminal gives you access to functionality like browsing the file system (like the Explorer in Windows or the Finder on a Mac) or to execute programs.
You navigate the file system with the following commands:

* `ls`: list all the files in a directory
* `cd`: **c**hange **d**irectory (move to another folder)
* `pwd`: **p**rint **w**orking **d**irectory 
  (print the path of the folder you are in)

In order to execute a program, you just have to type its name. You type `python` to run python and you type `python path/to/a/file.py` to call python with a program you wrote as an argument. This will execute your program. But you can also execute your editor via the terminal. Just type `gedit` to open the text editor or type `gedit path/to/a/file.py` to edit one of your programs. The editor simply is, as the name says, a program that allows you to edit text. Nothing more, nothing less. It is like *Word* or any other *Word processor* but for much simpler texts without any formatting. One important hint: `gedit` allows you to set [syntax highlighting][5], which makes it much easier for you to read and understand your code. [Short explanation here][6]

So as a short summary:

* the **terminal** gives you access to the operating systems functionality. It
  gives you the ability to do all the things that you usually do via a
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
