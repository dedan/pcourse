

Slicing
-------

Sounds fancy and is very useful. You'll need it all the time later, you'll need it that much, you won't even be aware of using it. This is why we will study this in detail today and practice it a lot. You have already seen a kind of *slicing* in the last lecture with what I called *random access to list elements*. Slicing is a way of accessing parts of lists or strings (later also vectors and matrices and this is where it becomes very useful for the scientist!). As always, a few examples first:

```python
    # first create two strings and a list
    bla = "a test string"
    fname = "fig_2010-12-14-u5_iSortd.png"
    numbers = range(10)

    # first element of a string
    print(bla[0])

    # first three letters
    print(fname[0:3])

    # the date in the filename
    print(fname[4:14])

    # the last element
    print(fname[-1])

    # second to the end
    print(fname[2:])

    # beginning to the tenth
    print(fname[:10])

    # all in a list
    print(numbers[:])

    # often useful: the file ending
    print(fname[-3:])

    # every other entry
    print(fname[::2])

    # all even numbers
    print(numbers[::2])

    # odd numbers
    print(numbers[1::2])

    # all but last two numbers?
    print(numbers[:-2])

    # all numbers in revers order
    print(numbers[::-1])

    # same with a string
    print(fname[::-1])
    
```

From the examples it becomes visible that the general pattern of accessing list or string elements is:

```python
    variable[start_index:end_index[:step_size]]
```

A few comments on this

* indexing in python starts with zero! The first element in a list has the index *0*.
* the `start_index` is inclusive, meaning that the element with the index *start_index* is included in the result.
* `end_index` to the contrary is exclusive. The resulting slice does not include the element with *end_index*.
* `:` separates start_index from end_index. If one or both of them is omitted, the maximum index value is taken. For example the slice with [3:] contains the 3rd element of the list and *all remaining*.
* negative indexing allows to index the list or string in reverse order. `[-1]` returns the last element.
* step_size is optional (therefore in brackets) and lets you select each n'th element from a list. Hint: Negative steps_size allows you to select elements from a list in reverse order.

Those few rules are very important. Please learn them by heart. You'll later use Slicing all the time and should be able to recite these rules when I wake you up in the middle of the night.


Modules
-------

This is something you would learn very late in another course. But I want to show you how simple it is to already do really cool stuff with a few lines of code. And as I said in one of the first lectures: programming helps to solve boring and repetitive tasks. Another important thing is to not do work that other people have done before and maybe even better then you could. Python comes with loads of functionality that you can use to solve your own problems. We have to distinguish between 2 things:

* the *python language* which is easy to learn because it has only a small set of keywords like `for`, `if`, `while`, etc..
* hundreds and hundreds *python modules* which contain python code that other people wrote for you.

I'll explain this idea of python modules further on the example of the `random` module.

```python
    
    # this is how you import a module - write import, followed by the
    # name of the module you want to use
    import random


    # lets say you want to choose a random element from a list
    students = ['julia', 'leo', 'tara']
    print(random.choice(students))


    # get a random number in a certain range
    print(random.randint(1, 6))


    # let each student throw the dice N times
    N = 3
    for student in students:
        print("%s is throwing the dice" % student)

        value = 0
        for game_round in range(N):

            print("for the %d time in this exciting game" % (game_round + 1))
            dice_points = random.randint(1, 6)

            # add yeah if value > 4
            print("the result is %d" % dice_points)
            value = value + dice_points
        out_string = "\t%s made %d points in %d rounds of the game"
        print(out_string % (student, value, N))


    # do something with a certain probability
    random_value = random.random()
    print(random_value)
    if random_value > 0.5:
        print("yeah")
```


Two useful String operations
----------------------------

This is nothing special and does not really fit into a category. But it is some useful functionality that comes with strings and you'll need it to understand my next example

# how to split a sentece into single words
sentence = "this is a sentence"
sentence1 = "this, is, one, with many, commas"

# split at all white-spaces (standard)
splitted = sentence.split()
print(splitted)

# split at another separator
splitted1 = sentence1.split(',')
print(splitted1)

# and how to join it again (join a list into a string)
print("! ".join(splitted))
print("- ".join(splitted1))


Advanced example
----------------

I decided to end each lecture with an advanced example that helps you to stay motivated. It should always be a example of how to achieve something really cool with only a few lines of code. They are a bit advanced and I don't expect you yet to be able to write something like this on your own (otherwise I would have given it as a homework). But you should have already all knowledge to understand the program completely and maybe you even want to modify it for extra-credits.

```python
    import random

    # the list in which we collect the output
    tmp_list = []
    
    # read in the whole file, split it into words and iterate over them
    for word in open('example.txt').read().split():
    
        # extract all but the first and the last letter
        center_as_list = list(word[1:-1])
        
        # suffle the center of the word
        random.shuffle(center_as_list)
        
        # put the string together and add it to results list
        tmp_list.append(word[0] + "".join(center_as_list) + word[-1])

    print(" ".join(tmp_list) + '\n')    
```


Unix, Terminal
--------------

Important for all real programmers and geeks is to solely use your computer via the command-line and this is why I always give you a few hints on how to use it more efficient. I realized that the usage of the `.` and `..` folders is a bit confusing in the beginning. These symbols are simply shortcuts to certain locations in you file-system.

* `.` is the folder you are in at the moment
* `..` is the parent folder

Here a small example:

```
    dedan@client195-176:~: cd projects/pcourse/
    dedan@client195-176:~/projects/pcourse: cd ..
    dedan@client195-176:~/projects: cd ..
    dedan@client195-176:~: cd projects/
    dedan@client195-176:~/projects: ls
        BozoCrack
        appendices.pdf
        ...
        surprise_experiment
        tests
        unateazy
    dedan@client195-176:~/projects: cd pcourse/
    dedan@client195-176:~/projects/pcourse: ls
        README.md
        ...
        test.py
    dedan@client195-176:~/projects/pcourse: ls .
        README.md
        ...
        test.py
    dedan@client195-176:~/projects/pcourse: ls ..
        BozoCrack
        appendices.pdf
        ...
        surprise_experiment
        tests
        unateazy
```


Introduction to the os module
-----------------------------

This is a very powerful module that gives you a lot of functionality. I will show you first some useful functions which are related to the UNIX stuff I just explained. As always, if you want to know more about a module, google it or use the question mark operator in ipython. The os module is called os because it provides you the same commands as your Operating System. For example you can list folders and files as with the `ls` command.

```python
    import os

    another_path = '/Users/dedan/Desktop'
    print(os.listdir("."))
    print(os.listdir(".."))

    file_list = os.listdir(another_path)
    for fname in file_list:
        print fname
```


Hints
-----

* Do you remember how to learn more about python objects and functions? Open ipython and type the name of the thing you want to know more about, followed by a question mark. This is also very useful in combination with modules. Try `random?` in ipython!


Homework
--------

1. Read in a name and check whether it is an *anagram*
    * the comparison can be done in one line!
2. The output of the *dice-throwing-program* is quite ugly when it says sentences like: "for the 1 time in this exciting game". Change the code in a way that it says *1 st*, *2 nd*, *3 rd* and *n th* for all n > 3.
    * you could first create a string containing the postfix with `if` and `elif` and then add it to the output via the new string formatting.
3. Implement the berghain bouncer
    * Write a similar program to the bouncer program from the first lecture
    * let him ask more questions
    * program a small conversation
    * let him (no matter what you say) reject you with a 40 % probability.
4. Use the os module to write a program which asks you for a path (something like: `/Users/julia/Desktop`) on the command-line and then counts the number of '.jpg' files it finds in this folder
    * use the os module to get a list of files for a certain path
    * use slicing to compare the ending of a filename