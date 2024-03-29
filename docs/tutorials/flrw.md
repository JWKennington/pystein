# Tutorial: FLRW Cosmology

This tutorial demonstrates a particular example of the symbolic tools in `pystein`. For other tutorials 
see [all tutorials](tutorials.md).

The `pystein.metric` module has several well-known metrics predefined. We will use the 
Friedman-Lemaitre-Roberston-Walker (FLRW) metric for this tutorial:

```python
from pystein import metric, gravity
from pystein import utilities

flrw = metric.flrw().subs({'c': 1})
flrw
```

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;\displaystyle&space;-&space;c^{2}&space;\operatorname{d}t&space;\otimes&space;\operatorname{d}t&space;&plus;&space;a^{2}{\left(t&space;\right)}&space;\left(\operatorname{d}x&space;\otimes&space;\operatorname{d}x&space;&plus;&space;\operatorname{d}y&space;\otimes&space;\operatorname{d}y&space;&plus;&space;\operatorname{d}z&space;\otimes&space;\operatorname{d}z\right)" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\large&space;\displaystyle&space;-&space;c^{2}&space;\operatorname{d}t&space;\otimes&space;\operatorname{d}t&space;&plus;&space;a^{2}{\left(t&space;\right)}&space;\left(\operatorname{d}x&space;\otimes&space;\operatorname{d}x&space;&plus;&space;\operatorname{d}y&space;\otimes&space;\operatorname{d}y&space;&plus;&space;\operatorname{d}z&space;\otimes&space;\operatorname{d}z\right)" title="\large \displaystyle - c^{2} \operatorname{d}t \otimes \operatorname{d}t + a^{2}{\left(t \right)} \left(\operatorname{d}x \otimes \operatorname{d}x + \operatorname{d}y \otimes \operatorname{d}y + \operatorname{d}z \otimes \operatorname{d}z\right)" /></a>
<!-- $\displaystyle - c^{2} \operatorname{d}t \otimes \operatorname{d}t + a^{2}{\left(t \right)} \left(\operatorname{d}x \otimes \operatorname{d}x + \operatorname{d}y \otimes \operatorname{d}y + \operatorname{d}z \otimes \operatorname{d}z\right)$ -->

We can use the `gravity` module to compute the einstein equation components: 

```python
efe_00 = utilities.full_simplify(gravity.einstein_equation(0, 0, flrw))
efe_00
```

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;\displaystyle&space;\frac{3&space;\left(\frac{d}{d&space;t}&space;a{\left(t&space;\right)}\right)^{2}}{a^{2}{\left(t&space;\right)}}&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\large&space;\displaystyle&space;\frac{3&space;\left(\frac{d}{d&space;t}&space;a{\left(t&space;\right)}\right)^{2}}{a^{2}{\left(t&space;\right)}}&space;=&space;0" title="\large \displaystyle \frac{3 \left(\frac{d}{d t} a{\left(t \right)}\right)^{2}}{a^{2}{\left(t \right)}} = 0" /></a>
<!-- $\displaystyle \frac{3 \left(\frac{d}{d t} a{\left(t \right)}\right)^{2}}{a^{2}{\left(t \right)}} = 0$ -->

The `metric` module contains a utility for simplifying the notation used for derivatives in sympy, which
we'll use to recover the familiar Friedmann equation:

```python
metric.simplify_deriv_notation(efe_00, flrw, use_dots=True)
```

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;\displaystyle&space;\frac{3&space;\dot{a}^{2}{\left(t&space;\right)}}{a^{2}{\left(t&space;\right)}}&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/svg.latex?\large&space;\displaystyle&space;\frac{3&space;\dot{a}^{2}{\left(t&space;\right)}}{a^{2}{\left(t&space;\right)}}&space;=&space;0" title="\large \displaystyle \frac{3 \dot{a}^{2}{\left(t \right)}}{a^{2}{\left(t \right)}} = 0" /></a>
<!-- $\displaystyle \frac{3 \dot{a}^{2}{\left(t \right)}}{a^{2}{\left(t \right)}} = 0$ -->

