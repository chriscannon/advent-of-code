# Advent of Code 2018
Some programming fun over the holiday season. I am *positive* I will never crack the top 100 leaderboard so my only
goal is to learn more about Python and in general writing optimal code using appropriate data structures
and techniques.

## Lesson's Learned
Day 1:
* Calling `int()` on a string will parse positive and negative numbers.

Day 2:
* Enumerate is your friend. Use it instead of `range` where appropriate.

Day 3:
* A tuple can be used as a key for a dictionary (e.g., `mydict[1, 2]`).

Day 4:
* Use the `most_common()` function on the `Counter` class to get a sorted list in descending order.
* Instead of using a generator to instantiate a list of literals (`['.' for _ in range(10)]`) you can use a m

Day 5:
* To check if letters are the same except for case check that they're equivalent when lowercase and not equivalent as they are.
* You don't really need to iterate over the alphabet if your input contains the alphabet. All you have to do is lower the string and then get the unique characters using `set()`.
* Keep a file of guesses so you don't accidentally repeat wrong answers.

Day 6:
* Sometimes it's easier to build the visualization shown in the challenge to understand how the solution should work.

Day 7:
* To get the dependencies of a graph build the graph as you normally would with a dictionary with lists as values but in reverse.
* Use `itertools.count()` in a loop to create a generator of incrementing integers.

Day 8:
* When dealing with trees recursion is likely going to be a good fit.
* If the recursion is too deep use your own stack.
* If you're not using the value in a `for ... range()` call use an underscore.

Day 9:
* Whenever you're iterating in a circular fashion `deque` is probably a good choice. It has much better Big-O complexity than the built-in list.
* If you need a list with better performance `blist` is also an option.
* Automate what you can to avoid mistakes. For example, I automated the creation of a new day by having a script that downloads the
input file and copies my Python starter template into the directory.
