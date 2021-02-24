# First Implementation
## A Simple Monte Carlo Model
### Monte Carlo Simulation
A Monte Carlo Simulation just means that the simulations use random numbers (the term originated from the Monte Carlo Casino in Monaco). 
Monte Carlo simulation is an extremely powerful technique, 
and there are often many problems where it's the only reasonable approach currently available. 
The Model uses random (Gaussian) numbers to simulate the diffusion of some measured quantity. 

### The Model
The _Ito Diffusion Process_ for some measurement of interest _X_, 
is described by the _Stochastic Differential Equation_ (SDE)

dX<sub>t</sub> 
= A(X<sub>t</sub>, t)dt + B(X<sub>t</sub>,t)dW<sub>t</sub>.

When W<sub>t</sub> is a Brownian Motion, 
and the coefficients are

A(X<sub>t</sub>, t) 
= X<sub>t</sub> &mu;, 

and,

B(X<sub>t</sub>, t) 
= X<sub>t</sub> &sigma;,

the diffusion of X is a _Geometric Brownian Motion_. 
For these conditions, 
the SDE has the solution (under Ito's interpretation)

X<sub>T</sub> = X<sub>0</sub>e<sup>(&mu; - &sigma;<sup>2</sup>/2)T + &sigma; &radic;T Z</sup>

where Z is a standard Gaussian random variable, i.e., Z~N(0,1), 
and T is the amount of time the quantity is left to diffuse.
Note, we allow the parameters themselves to be random under suitable conditions.

<div class="figure">
  <img src="../Images/01%20First%20Implementation/simulated_paths.jpg" width="75%">
  <p>Figure 1: Diffusion paths with absorbing boundary condition from above.
</div>

The objective of our Monte Carlo simulation is to approximate the expectation of the diffusion process subject to some boundary condition f(X<sub>t</sub>) using the law of large numbers, 

&sum; Y<sub>j</sub> / n.

That is, 
we draw a random number, x, from N(0,1), 
and compute

f( X<sub>0</sub>e<sup>(&mu; - &sigma;<sup>2</sup>/2)T + &sigma; &radic;T x</sup> )

We do this many times and calculate the average. 
Ito's solution means we don't have to simulate the full trajectories &omega;<sub>i</sub> of the particles.  
We can generate realizations at time T of the diffusion process.

## Model Features

A boundary condition is considered a _Model Feature_. 
For example, 
if the measured level _X_ crosses a boundary _K_, 
it's absorbed into the boundary such that

f(X<sub>T</sub>) = max(K - X<sub>T</sub>, 0)

at time T. 
More generally, 
we want to define many model features, 
so that many boundary conditions f<sub>1</sub>, 
f<sub>2</sub>, ..., f<sub>n</sub> can be applied.
By the [Law of the Unconscious Statistician](https://en.wikipedia.org/wiki/Law_of_the_unconscious_statistician) (LOTUS) 

E(Y) = E(f(X)) &approx; &sum; f(X) p(X) / n = &sum; Y p(X) / n

we can apply any function f to X, 
provided we know the distribution of X, 
and still approximate its expectation with Monte Carlo Simulations. 
That is, 
define a new r.v. Y = f(X), 
evaluate its value, 
then compute its expectation as before.

### Implementation
The algorithm to perform this calculation draws a random variable, 
x, 
from the Normal Distribution N(0,1), 
evaluates the function f(x),
and computes the average after many simulations.
The code [simple_mc.py](./simple_mc.py) is a first implementation of the procedure. 
It is called from [app.py](./app.py).

A few points to consider,
- The script uses the base modules [math](https://docs.python.org/3/library/math.html) and [random](https://docs.python.org/3/library/random.html?highlight=random#module-random), 
and the module [normals](./normals.py)
  - `math` module is used for exponentiation, logarithms, square-roots, etc.
  - `random` is used to generate uniform r.v.s on the interval [0,1]
  - `normals` is a collection of functions for calculating Normal densities, distributions, and inverse distributions
- Precompute as much as possible
- Avoid using the logarithm and exponential functions, 
slow to compute compared to addition and multiplication

## Critiquing the Simple Monte Carlo Routine
The routine does what's needed but will soon run into difficulty when we need to add more features, 
or change a part of the simulation.
For example, 
suppose we want to perform the following modifications / enhancements to the current version of the model

- Change the boundary condition on line 34 of [simple_mc.py](./simple_mc.py)
- See how accurate the approximation is, 
add the Monte Carlo standard error (see Appendix).
- The convergence is too slow, 
add antithetic sampling.
- Calculate the most accurate estimate possible by 9am tomorrow so set it running for 14 hours.
- The standard error needs to be less than 0.0001, 
so run it until that’s achieved. 
We’re in a hurry though so don’t run it any longer than strictly necessary.
- Add in low-discrepancy numbers and see how good they are.
- Apparently, 
standard error is a poor measure of error for low-discrepancy simulations. 
Put in a convergence table instead.
- Can we see the standard error too?
- What about changing the distribution of the generator?

If in order to change the code, 
it takes another programmer more effort to understand the routine than it does to recode it, 
he/she will recode it. 
The essence then of good coding is reusability. 
Code is reusable if someone has reused it.
Reusability is as much a social concept as a technical one. 
What will make it easy for someone to reuse your code? 


Returning to the simple Monte Carlo program. 
Suppose we have to add a new feature to the routine,

- If we've designed it well, it will be easy to add new features.
- If we've designed poorly, we will have to rewrite existing code.

In order to add _another_ boundary condition to the current script, 
how would we do that?

Option one: 
- Copy the function, 
- change the name by adding "_another" at the end, 
- and rewrite the two lines where the condition is computed.

Option two: 
- Pass in an extra parameter, 
possibly as a string or enum and 
- compute the boundary condition via a series of else-if statements in each loop of the Monte Carlo. 

The problem with the first option is that when we come to the next task, 
we have to adapt both the functions in the same way and do the same thing twice. 
If we then need more conditions in the future, 
this task rapidly become a maintenance nightmare. 

The issues with the second option are more subtle. 
The switch statement is an additional overhead that makes the script run a little slower. 
A deeper problem occurs if we want to use the boundary condition in another part of the code. 
We have to copy the code from inside the first routine or rewrite it as necessary. 
This again becomes a maintenance problem; every time we want to add some new logic, 
we have to go through every place the condition is located.

An Object-Oriented approach is to use a class. 
The class would _encapsulate_ the behavior of the boundary condition. 
A Condition object is then passed into the function as an argument and in each loop a method expressing its value is called to output the level given that condition. 