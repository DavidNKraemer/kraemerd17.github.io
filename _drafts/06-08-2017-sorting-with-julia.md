---
layout: post
title: Julia excursion part 2 sorting
date: June 2017 
author: David Kraemer
---

In this post, we will explore sorting algorithms in Julia, which will provide a
concrete case study for learning about the Julia type tree, generics system,


# Quicksort overview

Let's begin by recalling the quicksort algorithm. This is a
"divide-and-conquer" algorithm with a theoretical complexity of
\\(\mathcal{O}(n^2)\\) (where \\(n\\) is the length of the input array),
although in practice it behaves like an \\(\mathcal{O}(n \log n) \\) sorting
algorithm. This is due to a clever trick which exploits the properties of
randomness, which we'll get into later.

Let \\(A\\) be an array of \\(n\\) numbers, which we will denote \\(A[i]\\)
for each \\(i \in \\{1, \ldots, n\\}\\). Quicksort proceeds by fixing a "pivot"
element \\(A[\mathrm{pivot}]\\), which we use to partition \\(A\\) into two
contiguous subarrays, the "left half" \\(\underline{A}\\) and the "right half"
\\(\overline{A}\\), such that
\\[
    \underline{A}[i] \leq A[\mathrm{pivot}] \leq \overline{A}[j]
\\]
for all \\( 1 \leq i \leq \mathrm{pivot} \leq j \leq n \\). In English, this
means that the "left half" of \\(A\\) contains all of the elements which are at
most \\(A[\mathrm{pivot}]\\), and the "right half" of \\(A\\) contains all of
the elements which are at least \\(A[\mathrm{pivot}]\\). Importantly, this
means that after the partition, \\(A[\mathrm{pivot}]\\) is in its correct spot.
It also means that we can treat the "left half" \\(\underline{A}\\) and the
"right half" \\(\overline{A}\\) as independent unsorted arrays, since the
elements of \\(\underline{A}\\) are all at most any of the elements of
\\(\overline{A}\\). So, we can simply perform quicksort on \\(\underline{A}\\)
and \\(\overline{A}\\), respectively. 

## Partition walkthrough

That's a lot of symbols, so let's do an example. Consider the array `A` given
by

```
       1   2   3   4   5   6   7
     +---+---+---+---+---+---+---+
A =  | 3 | 5 | 1 | 7 | 2 | 6 | 4 |
     +---+---+---+---+---+---+---+
     ^ ^                       ^
     | |                       |
     i j                     pivot
```

For simplicity, we'll define `pivot = 7`, the last element of `A`. For loop
invariants, we define the `i` index to be the number of elements we know for
certain that are to the left of `A[pivot]`. So in the end, we will expect
`A[i+1] == A[pivot]`. Now, at present, we have absolutely no idea where the
smaller elements are (there might not be any elements to the left of
`A[pivot]`!), so we'll start with `i = 0`. Letting `j` loop through the first 6
indices of `A`, whenever `A[j]` should be to the left of `A[pivot]`, push it to
the left half of the array, and update `i` accordingly to account for the
additional information. So, starting with `A[j] == 3`, we notice that `A[j] <=
A[pivot]`, so there is at least one element to the left of `A[pivot]`. We
therefore update `i` to account for this, and we swap `A[i]` with `A[j]`. (In
this case, `i == j` so no immediate changes are apparent.) The new diagram
looks like

```
       1   2   3   4   5   6   7
     +---+---+---+---+---+---+---+
A =  | 3 | 5 | 1 | 7 | 2 | 6 | 4 |
     +---+---+---+---+---+---+---+
       ^                       ^
       |                       |
      i,j                    pivot
```

Next, with `j = 2`, and `A[j] == 5`, we notice that `A[j] >= A[pivot]`, so we
leave it alone. The new diagram looks like

```
       1   2   3   4   5   6   7
     +---+---+---+---+---+---+---+
A =  | 3 | 5 | 1 | 7 | 2 | 6 | 4 |
     +---+---+---+---+---+---+---+
       ^   ^                   ^
       |   |                   |
       i   j                 pivot
```

Next, with `j = 3`, and `A[j] == 1`, we notice that `A[j] <= A[pivot]`, so
there are at least 2 elements of `A` to the left of `A[pivot]`. We increment
`i` and swap `A[i]` with `A[j]`. The new diagram looks like

```
       1   2   3   4   5   6   7
     +---+---+---+---+---+---+---+
A =  | 3 | 1 | 5 | 7 | 2 | 6 | 4 |
     +---+---+---+---+---+---+---+
           ^   ^               ^
           |   |               |
           i   j             pivot
```

We continue this process until we reach the end of `A`. The final resulting
array should look like

```
       1   2   3   4   5   6   7
     +---+---+---+---+---+---+---+
A =  | 3 | 1 | 2 | 7 | 5 | 6 | 4 |
     +---+---+---+---+---+---+---+
               ^           ^   ^
               |           |   |
               i           j pivot
```

The only thing that remains is to actualy place `A[pivot]` in its proper
position. Since `i` counts the number of elements to the left of `A[pivot]`, we swap
`A[i+1]` with `A[pivot]` to finish the partition.

```
       1   2   3   4   5   6   7
     +---+---+---+---+---+---+---+
A =  | 3 | 1 | 2 | 4 | 5 | 6 | 7 |
     +---+---+---+---+---+---+---+
                   ^   
                   |   
                  i+1   
```

# Implementing `partition!` 

Let's take a look at a first attempt at implementing the `partition!` algorithm
in Julia. First of all, we are writing a function which modifies the state of
its inputs, so the convention is to define it with a `!` symbol. This alerts
the user that the function being invoked has side effects. Second, we need to
tell Julia that the array we are passing into `partition!` is actually
sortable. Since we're only thinking about (real) numbers at the moment, it
suffices to specify that the input `A` is a 1-dimensional array composed of
reals. 

This is a good time to talk about type annotations in Julia function headers.
Julia's flexibility allows you to declare functions without any description of
type, similar to Python:

{% gist https://gist.github.com/kraemerd17/ac2427408b34450c82569bca874c3a73#file-notyping-jl %}

Julia will compile specific methods for any inputs whose `*` operator is
defined. This extends past numbers to include strings (`*` is concatenation)
and arrays (`*` is the matrix product):

```
julia> mul(2,3)
6

julia> mul("hello", "julians")
"hellojulians"

julia> mul([1, 2, 3], [1 2 3])
3×3 Array{Int64,2}:
 1  2  3
 2  4  6
 3  6  9
```



#### Julia implementation of `partition!`
{% gist c8a1ca83f0631ae11ed34b4451af2d3d %}

