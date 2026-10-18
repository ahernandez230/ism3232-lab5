# debug_log.md
# Author: Ariadna Hernandez

## Bug 1
Error type: KeyError
File + line: week8_buggy.py identified on line 12
What the error means: Dictionary key does not exist
What I told the duck: There is a typo in the word "amount" on line 4, which led to the key error because the typo does not match what was defined.
What I tried: Fixed the typo
How I fixed it: Fixed the typo

## Bug 2
Error type: TypeError
File + line: week8_buggy.py identified on line 16
What the error means: A type error means you used a value in a way its data type doesn't allow.
What i told the duck: On line 16, the numbers 1000 are written with quotes. Therefore, python is treating it as a string insead of numbers.
How I fixed it: Removing the quotes from 1000 on line 16.

## After Fixing Both Bugs
Final output: Total: $5150.00 across 3 records
True
Did pytest pass? Yes

## AI Literacy Reflection
Did I use AI? Yes
If yes -- exact prompt I used: I’m debugging a Python script for my ISM class. It crashed with KeyError: 'amount', and the traceback pointed to line 12 and line 21. But the actual mistake was a misspelled key in the data on line 4. Why does Python report lines 12 and 21 instead of line 4, and how do I trace an error back to its source? (Also Included a screenshot of the buggy code for context)

What AI explained:
Python reports where the error happened, not where the mistake started.

Line 4 is where the typo was made. Python didn’t complain there, because a dictionary accepts any key spelling when it’s created.
Line 12 is where the code first used that data. rec['amount'] asked for a key that didn’t exist, so this is where Python crashed.
Line 21 is the call that led into get_total. It’s just part of the path to the crash.

Python only knows what it was doing at the moment of failure. It has no way of knowing a key was misspelled earlier, so it shows the chain of calls that led to the crash (the traceback) instead.

How to trace an error back to its source:

Read the last line of the traceback to get the error type and detail (KeyError: 'amount').
Look at the deepest line listed (line 12), since that’s where it crashed.
Ask where the thing in the error came from. Here, rec comes from records, so check how records was built.
Compare the data to what the code expects, and you’ll find the mismatch on line 4.

What I changed myself: I identified all errors individually and with my groupmates. I used AI to clear up how to identify less obvious errors in the future. 
Can I explain every fixed line? Yes

## What I learned
Before this lab i was under the impression that whenever I bwas presented with an error, Python would tell me on what line the errors were located. I learned that python tells you the path it took before crashing which is actually more helpful for somebody working on a more complex project. 