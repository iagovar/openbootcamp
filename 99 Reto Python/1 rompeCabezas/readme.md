# Sliding cards solver

I don't have a CS degree, but it wasn't much effort to find solutions to the problem in the internet (LeetCode, SO, etc). I decided to not look at implementations or tailored algorithms (everyone seems to use BFS or A-star), just to general explanations so I can challenge myself.

## Constraints

- Time. I can't allocate much time to the problem so we have to think and code fast. Ideally it has to be done in less than 10 hours of effective focus.
- Expertise. I have no CS/Math degree, which in conjuction with time leaves out reading papers about such topic, which in turn prevents me from leveraging other people's time.
- Skills. I'm not a seasoned programmer so I'll have to deal with n00b bugs along the way, which consumes time. Pytest can help a bit with that.
- Focus. I'm juggling python (ie this very problem) + learning frontend with JS + life stuff, which will be pretty distracting.

## Initial hypothesis

I'll lay out some hypothesis about this problem, whithout having prior theoretical knowledge about it, and only glancing over comments in the internet.

### General hypothesis

- Time to solution will grow exponentially with every *ij* addition.
- Non solvable puzzles can't be determined from initial state for n > 4 given you can sequentialy order all tiles (if you can't, it's obviously non-solvable).

The two first hypothesys forces us into two ways of determining if a puzzle is non-solvable.

1. Checking if we can order tiles sequentially. any puzzle failing this task is obviously non solvable. It's so obvious that we're really doing input validation here.
2. Time-to-solution. The problem here is that I can't know from initial state if a puzzle is not being solved because my solving algorithm or because it's a really difficult one. It's a kinda arbitrary limitation that emerges from expectations + constraints.

### Solver hypotesis

- Storing previous states is probably the best human-understandable method to avoid infinite loops.

- The best way to store such states is through a binary tree. Since I'm not familiar with OOP, it could be inplemented through a python dictinary native data type.

- Since we're storing all possible states, the best solution is the one that reaches goal state sooner.

### Cheatsheets and interesting resources about algorithms

- [Algorithms and Data Structures Cheatsheet](https://algs4.cs.princeton.edu/cheatsheet/) by Princeton
- [Big O Cheatsheet](https://www.bigocheatsheet.com/) by several contributors
- [Algorithmic CheatSheet](https://sinon.org/algorithms/) by Sinon.org
- [The Algorithms](https://the-algorithms.com) by several contributors