# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> >

---
- mkdir -p - creates directory as parent directory, lets you make an entire path even if directories didn't                     previously exist
- cd - change directory, typing this alone sends you directly to home directory
- ls -lR - lists contents in long form recursively 
- pushd - "saves" where you are and takes you to specified directory, after pushing to new directory, pushd alone will switch   back and forth
- popd - "pops" you back to where the save point created by pushd was
- rmdir -p - similarly (to mkdir -p) will remove an entire path of directories, as long as there are no files
- touch - UNIX version of new-item
- man - brings up manual for commands, UNIX version of HELP
- cp -r - recursive copy, copies everything within the directory
- apropos - finds all relevant commands containing the word, incase you can't remember the name of a command
- cat > file - reads whatever you type into terminal and creates new file (as text?)
- $>$ - writes to the right
- $>>$ - appends to the right
- grep - finds a string within specifies files, '-i' flag ignores cases


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > ls lists the contents of the current directory. '-a' lists all entries starting with ".", '-l' gives a long form of the contents displaying file info. '-lh' gives the same long form but "human-readable", so large numbers will be rounded. the '-l' flag seems to be able to be combined with most other ls flags to change formatting.

---


---

What does `xargs` do? Give an example of how to use it.

> > apply a command to a series of things in order. If I wanted to find a string in all the files within a directory I could do 
    $ ls | xargs grep string
this would display the file containing the string, and the line the string is in for every file within the directory

---

