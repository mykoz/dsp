[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>



```
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def CohD(group1, group2):

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1*var1 + n2*var2)/(n1+n2)
    d = diff/math.sqrt(pooled_var)
    return d
```

`CohD(firsts.totalwgt_lb,others.totalwgt_lb)`


`-0.088672927072602`


with a .0887 effect size suggesting that firsts overall weigh less than others.

`CohD(firsts.prglngth, others.prglngth)`


`0.028879044654449883`


this is a .029 effect size suggesting that firsts have longer pregnancy lengths than those after.

Overall, there is more of a difference in the weights of first borns vs others than in the lengths of them.
