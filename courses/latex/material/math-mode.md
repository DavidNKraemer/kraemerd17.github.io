---
title: Math Mode 
suppress-title: false
author: David Kraemer & Caleb Leedy
date: February 10, 2016
layout: page
show_meta: false
sidebar: right
sidebar-title: Course Links
sidebar-content: |
    <ul> 
        <li> <a href="../">Main page</a> </li> 
        <li> <a href="https://en.wikibooks.org/wiki/LaTeX">Wikibooks page</a> </li>
        <li> <a href="latex-wikibook.pdf">Wikibooks PDF</a> </li>
        <li> <a href="http://www.xm1math.net/texmaker/download.html">TexMaker</a> </li>
        <li> <a href="http://www.sharelatex.com">ShareLaTeX</a> </li>
        <li> <a href="http://www.overleaf.com">Overleaf</a> </li>
    </ul>

    <h3> Useful Links </h3>
    <ul>
        <li> <a href="http://faculty.cbu.ca/srodney/ShortSymbInd.pdf">Big list of math symbols</a> </li>    	
        <li> <a href="http://detexify.kirelabs.org/classify.html">Detexify</a> </li>    	
        <li> <a href="http://tex.stackexchange.com/">LaTeX StackExchange</a> </li>    	
        <li> <a href="http://www.latextemplates.com/">Free templates</a> </li>    	
        <li> <a href="https://www.sharelatex.com/learn">ShareLaTeX written guides</a> </li>    	
        <li> <a href="https://www.youtube.com/user/ShareLaTeX/playlists">ShareLaTeX Youtube channel</a> </li>    	
    </ul>
permalink: courses/latex/material/math-mode/
...

Let's set up a new document. We can start with the following code:

```LaTeX
\documentclass{article}

\begin{document}

\end{document}
```

In standard  \\(\LaTeX\\), there are two main types of math typesetting options:
math mode and display mode. Math mode provides in-line equations and
symbols. Display mode generates centered, standalone equations. As an example,
update your document to read

```LaTeX
\documentclass{article}

\begin{document}

$a x^{2} + b x + c = 0$.

\end{document}
```

If you compile and view this document, you should see

![test][1]

Math mode typesetting is surrounded by a pair of $ signs. So, `$x+y+z=A$` will
typeset into the equation \\(x + y + z = A\\). When in math mode, you are able
to use additional math-related symbols, such as \\(\in, \alpha, \int\\), that
can't be used outside of it.

Here is a short list of example math mode commands that you will find useful
regularly.

| Command | Output |
|:-------:|:------:|
| `\beta` | \\(\beta\\) |
| `\frac{1}{2}` | \\(\frac{1}{2}\\) |
| `\mathbf{A}` | \\(\mathbf{A}\\) |
| `\{ x \}` | \\( \\{ x \\} \\) |
| `z \in \mathbb{R}` | \\(z \in \mathbb{R}\\) |
| `x^{2}` | \\(x^{2}\\) |
| `T_{5}` | \\(T_{5} \\) |
| `\int_{a}^{b}` | \\( \int_a^b \\) |
| `\sum_{i=1}^{n}` | \\(\sum_{i=1}^{n} \\) |

The math macro for a Greek letter uses the form `\Alpha`
for uppercase letters and the form `\zeta` for lowercase letters.


[1]: ../../images/math-mode/ex-01.png
