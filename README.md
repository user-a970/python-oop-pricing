# Design Patterns
## Description
An introduction to Object-Oriented (OO) Design Patterns in Python.<sup id="a1">[1](#f1)</sup> 
The presentation is aimed at the Computational Scientist, 
experienced in using code to solve problems, 
but unaware of some of the benefits of an Object-Oriented approach.<sup id="a2">[2](#f2)</sup>
With this in mind, 
we start with a simple procedural model, 
and rewrite the model, 
introducing new concepts at each checkpoint to solve a range of programming challenges.
This approach isn't optimal from a design perspective, 
but is more pedagogical, 
and less abstract than a collection of [class examples](./00%20Getting%20Started/2d_point_class_example.py).
Finally, 
design principles are emphasized over other programming topics, 
like numerical efficiency, 
or exception safety.

## Table of Contents
0. [Getting Started](./00%20Getting%20Started)
1. [First Implementation](./01%20First%20Implementation)
2. [Encapsulation](./02%20Encapsulation)
3. [Inheritance](./03%20Inheritance)
    - [Is a](./03%20Inheritance/030%20Is%20a)
    - [Polymorphism](./03%20Inheritance/031%20Polymorphism)
    - [Duck-Typing](./03%20Inheritance/032%20Duck-Typing)
4. [Bridging](./04%20Bridging)
    - [First Solution](./04%20Bridging/040%20First%20Solution)
    - [Parameters](./04%20Bridging/041%20Parameters)
    - [Properties](./04%20Bridging/042%20Properties)
5. [Statistics](./05%20Statistics)
    - [Statistics Gatherer](./05%20Statistics/050%20Statistics%20Gatherer)
    - [Decorators](./05%20Statistics/051%20Decorators)
6. [Random Numbers](./06%20Random%20Numbers)
    - [Base Class](./06%20Random%20Numbers/060%20Base%20Class)
    - [Antithetic Sampling](./06%20Random%20Numbers/061%20Antithetic%20Sampling)
7. [Appendix](./07%20Appendix)


## Getting Started
The project requires

- [Python 3](https://www.python.org/), and
- [Pylint](https://pylint.org/)

Microsoft's [Visual Studio Code Editor](https://code.visualstudio.com/) is recommended with the [Python Extension](https://code.visualstudio.com/docs/languages/python) installed. 
The [Getting Started](./00%20Getting%20Started) directory contains a detailed setup guide with some examples to check the Editor is configured correctly.

## Usage
The documentation for each pattern is contained in the README file of the parent and child directories at each checkpoint. 
Parent folders typically contain a summary of the current state of the code, 
and a discussion about where improvements can be made. 
The child directories contain the code modifications and their documentation. 
Checkpoints are numbered from 0 to 7, 
with intermediate steps numbered as 6.1, 6.2, ...
Because the code is gradually extended and enhanced, 
the text makes the most sense following its natural progression from checkpoint to checkpoint.

## Resources
Although the choice of Mathematical Model is somewhat arbitrary, 
a Monte Carlo Simulation provides many convenient examples of concepts that can be abstracted. 
The Model is introduced and very briefly discussed in [Part 1](./01%20First%20Implementation), 
the interested reader is referred to [Kroese](https://people.smp.uq.edu.au/DirkKroese/montecarlohandbook/) and [Glasserman](https://www.springer.com/gp/book/9780387004518) for a comprehensive review of the topic.

There have been 2 key resources for most of the Object-Oriented Design Pattern material for Python:
- [The Refactoring Guru](https://refactoring.guru/design-patterns/python), and
- [Brandon Rhodes](https://python-patterns.guide/)

As Brandon points out, 
the Object-Oriented classic, 
[Design Patterns](http://wiki.c2.com/?GangOfFour), 
is mostly obsolete in Python's ecosystem.

[<b id="f1">1</b>]: A Pattern need not be Object-Oriented. 
In the [Appendix](./07%20Appendix) we provide 2 examples of Python Patterns that aren't Object-Oriented. [↩](#a1)

[<b id="f2">2</b>]: The goal of any coding project is collaboration and transparency. 
If Classes and Design Patterns alienate users, 
and make the code harder to read, 
then they should be avoided. [↩](#a2)