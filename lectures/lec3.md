

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





split and join

throw dice with the random module


show wechstaben example


Unix, Terminal
--------------

* `.` is the folder you are in at the moment
* `..` is the parent folder

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

hints
-----

* remember how to learn more about something in ipython?
    * something?


homework
--------

* slicing

* read in a name and check whether it is a *anagram*
* count the 