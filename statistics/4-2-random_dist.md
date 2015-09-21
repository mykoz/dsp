[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

SHOW PMF AND CDF OF 1k RANDOM NUMBERS

```
import random
import thinkstats2
import thinkplot
onek = [random.random() for num in range(1000)]
pmf = thinkstats2.Pmf(onek)
thinkplot.Pmf(pmf, linewidth=0.09)
thinkplot.Show()
```
This generates 1000 random numbers that are within the range of 0 and 1. The PMF is kind of a mess and is basically a thousand lines next to each other. 

```
cdf = thinkstats2.Cdf(onek)
thinkplot.Cdf(cdf, linewidth=1)
thinkplot.Show()
```

This is the CDF. it is a fairly straight line going diagonally from 0 to 1. From this we can say that it is definitely a uniform distribution.
