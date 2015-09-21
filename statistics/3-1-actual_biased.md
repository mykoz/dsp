[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

```
import thinkstats2
pmf = thinkstats2.Pmf(resp.numkdhh)
pmf #unbiased 
```

Gives: `Pmf({0: 0.46617820227659301, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.087138558157791451, 4: 0.025644380478869556, 5: 0.010728771424833181})`

Define the Biased PMF function:
```
def BiasPmf(pmf, label=''):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf
```
`biased = BiasPmf( pmf, label = 'biased pmf')`

To Display the graphs superimposed:

```
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()
```
UNBIASED MEAN

`pmf.Mean()` = 1.0242051550438309

BIASED MEAN

`biased.Mean()` = 2.4036791006642821
