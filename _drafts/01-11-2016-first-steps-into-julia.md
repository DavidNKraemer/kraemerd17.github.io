---
layout: post
title: My first steps with Julia
date: January 2016
author: David Kraemer
---

The Julia programming language has been getting a good amount of hype in the
last few years, which is impressive if for no other reason than version 1.0 has
yet to be released (as of January 2016). It's developing a strong following in
the data science and scientific computing communities, and its advocates
emphasize the power and utility of its type system and JIT compilation that
allow it to reach C-like execution speed.

My background is the Python scientific stack. I've done a lot of work with
Numpy, Scipy, Matplotlib, and Scikit-learn, with a decent amount of Pandas
sprinkled in for good measure. From what I've read, Julia takes a lot of
inspiration from Python's successes. It also inherits many of the ideas from R
and Matlab. So I thought I would give it a spin.

# First impressions

After installing Julia (very easy with Ubuntu, though I haven't tried other
systems), I started fiddling around with the REPL. I did the sanity check:

```
julia> 1+1
2

```

The first thing that stood out for me is Julia is using a lot of innovations
from the IPython project. For example, I wanted to look into how the `rand`
function worked. By pressing `?` in the REPL, the prompt switches to a
documentation search:

```
help?> rand
search: rand randn rand! randn! randexp randperm randjump randexp! randbool

  rand([rng], [S], [dims...])

  Pick a random element or array of random elements from the set of values
  specified by S; S can be

    •  an indexable collection (for example 1:n or ['x','y','z']), or
    •  a type: the set of values to pick from is then equivalent to
      typemin(S):typemax(S) for integers (this is not applicable to BigInt), and
      to [0, 1) for floating point numbers;

  S defaults to Float64.
```

Given a random number generator and some underlying space of values, `rand`
grabs an element from the space with uniform probability. So simply calling
`rand()` samples from a uniform distribution on [0,1]:

```
julia> rand()
0.8242929333351847
```

This is a behavior I would expect coming from the world of `numpy.random`, but
it's also really slick to simply pass in a different space and get the desired
effect. Say I have the array `[1,2,3]`. Then, following intuition, I get

```
julia> rand([1,2,3])
2
```

This is really excellent. If the design of functions in Julia is regularly this
simple, it will mean memorizing a significantly fewer collection of interfaces.

The second major standout is that you feel the presence of Julia's JIT compiler
almost immediately. From my experimentation, it seems like absolutely no
functions are precompiled. Take integer addition, for example. Using the macro
`@time` (macros are a popular part of the Julia environment that I have no
understanding about at present), which measures the execution time and space
required for a given bit of code, I typed

```
julia> @time 2+2
  0.000005 seconds (154 allocations: 42.089 KB)
4

julia> @time 2+2
  0.000002 seconds (4 allocations: 160 bytes)
4
```

This reveals that even `+` gets compiled on the fly. I felt a noticeable
difference in execution time between the two calls, even though `@time` reports
a very small interval for both. My suspicion is that Julia compiled all of the
arithmetic procedures in the first call, because subsequent attempts with `*`
and `^` all seemed very fast.

Julia proponents say that JIT makes its execution times dramatically faster than
comparable languages such as Python. [One
estimate](http://jonathankinlay.com/2015/02/comparison-programming-languages/)
puts Julia's performance at around 3 times slower than C++, whereas (naive)
CPython clocks in around 150-300 times slower. That is an exciting speed.

Last, Julia fully supports unicode characters in variables and functions. While
this could easily open a can of worms for illegible code, the emphasis is really
placed around mathematical symbols. The REPL allows you to get common symbols by
using the corresponding \\(\LaTeX\\) command. For example,

```
julia> \varepsilon
```

and pressing `[TAB]` gives me

```
julia> ɛ = 1e-5
1.0e-5
```

As someone who writes a good amount of numerical simulation, this might be very
useful.  It promises to drastically reduce the difference between algorithm
pseudocode found in an article and the actual implemented code. To illustrate
what this could imply (albeit in a contrived example), consider this code:

```
function ∫(f, a, b, n)
    Δx = (b - a) / n
    Σₐᵇf = f(a) + f(b)
    for i = 1:(n-1)
        Σₐᵇf += 2f(a + Δx * i)
    end
    0.5Δx * Σₐᵇf
end
```

If you look closely you will notice that `∫` implements the trapezoid method if
numerical integration. I purposely used as many symbols as possible so it would
read like mathematics. It's a bit of an eyesore, though the subscripting and
superscripting is a neatfeature. It behaves as expected:

```
julia> ∫(sin, 0, 2pi, 100)
4.211601211345423e-16
```

I have to say, despite its potential to completely obfuscate code, it's still pretty cool.





