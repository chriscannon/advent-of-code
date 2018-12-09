Quick document to keep track of everything I learned from completing these challenges in Python and looking at what solutions community produced.
Day 1:
* Calling `int()` on a string will parse positive and negative numbers.

Day 2:
* Enumerate is your friend. Use it instead of `range` where appropriate.

Day 5:
* To check if letters are the same except for case check that they're equivalent when lowercase and not equivalent as they are.
* You don't really need to iterate over the alphabet if your input contains the alphabet. All you have to do is lower the string and then get the unique characters using `set()`.
* Keep a file of guesses so you don't accidentally repeat wrong answers.

Day 6:
* Sometimes it's easier to build the visualization shown in the challenge to understand how the solution should work.

Day 7:
* To get the dependencies of a graph build the graph as you normally would with a dictionary with lists as values but in reverse.

Day 8:
* When dealing with trees recursion is likely going to be a good fit.
* If the recursion is too deep use your own stack.
* If you're not using the value in a `for ... range()` call use an underscore.

Day 9:
* Whenever you're iterating in a circular fashion `deque` is probably a good choice. It has much better big-Oh complexity than the built-in list.
* If you need a list with better performance `blist` is also an option.
* Automate what you can to avoid mistakes. For example, I automated the creation of a new day by having a script that downloads the
input file and copies my Python starter template into the directory.
