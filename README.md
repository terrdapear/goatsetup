Terr's home comprog setup :> 

FILES:  
/ **ally.py**  
Terr's Python competitive programming solution template. This template features:  
- Fast I/O  
- Commonly used Python imports  
- Integrated local test file (hatdog.txt)  
- Locally reports program runtime  

*How to use?*  
Write your solution in between the "start" and "end" comments. Use I() and O() how you would normally use input() and print() minus their parameters. 
  
/ **hatdog.txt**  
File for local tests.  

*How to use?*    
Copy the test input and paste it to this file. Now, ally.py takes whatever you pasted as input during runtime.  

/ **generator.py**  
Generator of test cases.  

*How to use?*
In out(), create variables and use list comprehension to build lines with elements separated by spaces. Each list = new line.  

/ **interactive.py**  
Terr's template for interactive problems. Too sleepy to write about this rn LOL. It's 2 am.  

/ **template.py**  
Exact copy of ally.py. This is here just in case it is needed.  

**TIPS for writing solutions in competitive programming** (as of 2026)  
Sufficiently good algorithmic design is of course the most important element of a competitive programming solution. However, just as important is its implementation. Many (not all) general good coding practices hold up in competitive programming. However, Python in particular is best used using very specific coding practices. Python, in this context, of course, not only refers to the language, but to the interpreter used. PyPy and CPython greatly differ in this regard. 

*In CPython*  
As an interpreted language, Python is incredibly slow. Luckily, Python features many built-in objects and functions natively written, optimized in C. With this in mind, avoid writing Python code as much as possible! Use built-ins as much as possible, avoid Python loops, and avoid classes! Code written in such a manner are called *Pythonic*.  

*In PyPy*  
A Just-In-Time (JIT) compiler is a type of interpreter that observes a running program, identifies the "hot" sections of code (usually highly repeated sections), and compiles these sections during runtime to increase code efficiency! PyPy uses a JIT compiler. With this in mind,  
- Keep code SIMPLE! Write in Python.
- Classes are okay. 
- Loops are really fast.