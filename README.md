# TRIAL EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
 - You can use any resource online, but **please work individually**
 - Instead of copy-pasting your answers and solutions, write them in your own words.


# Tasks
## 1-5. Complete the tasks seen in the 1-5.py files! (~90 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently with descriptive commit messages [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm used in exercise 2. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:

      **pseudo code:**

      get input(file name)

      initialize a variable to 0, this represents the number 'a'-s in the text

      try to open the file for reading using the input as a filename:
         - store it in a variable
      if the file cannot be opened(file not exist):
         - return number 'a'-s (which is 0 now)

      for each line in file (which is stored in a variable):
         - go through all the characters in a line and if it's equal to 'a':
               - increment the variable which represents the number 'a'-s

      return the number 'a'-s


### How can you get a random number in python? [2p]
#### Your answer:

      the random package must be imported into the file:
         if you want to get a random integer between 2 numbers including them: random.randint(number1, number2)
         if you want to get a random float: random.random() --> returns a random float between 0 and 1 (including them)

### What does M stand for in MVC? [2p]
#### Your answer:
      M stands for the Model component in the MVC design pattern. It's used for manage and manipulate the data and containing the logic of the application.
