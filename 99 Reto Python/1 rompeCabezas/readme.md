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

# After coding conclussions

Turns out that I really need a dive into data structures, algorithms and OOP, as the script is very inefficient at solving problems. You can use *time* in bash to check, but it takes minutes to solve simple puzzles.

It was perhaps more in the +30h time sink (didn't track it honestly), but mostly because I've got confused with some n00b bugs that came from not realizing that I was referencing lists instead of copying them, etc.

## Cost function was hard to implement as I wanted

Because the initial script was slow, I thought a manhattan type cost function may be useful at freeing up some memory in exchange of losing some potential shorter paths.

My initial idea was to determine the distance between a given state and the goal state every N iterations, decide which are not necessary (have a greater distance vs the goal state) and delete all the junk from memory, so my poor laptop can loop it quick.

But deleting stuff from lists changes the indexes of all other elements. If you want to fix this you get into stuff that rally adds a performance penalization, when the initial point was to avoid such penalization, so in the end evens out and it's not worth it.

Then I thought that I could set some states to None value, avoiding such shuffling indexes mess, but it doesn't save that much memory and it also caused some troubles down the line with the logic. Because of the above mentioned constrainst I decided to not sink more time in it, and be done with it.