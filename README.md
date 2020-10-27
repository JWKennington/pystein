# Collapsing Cosmology Research Utilities
[![PyPI version](https://img.shields.io/pypi/v/collapse)](https://pypi.org/project/collapse/)
[![PyPI downloads](https://img.shields.io/pypi/dm/collapse)](https://pypi.org/project/collapse/)
[![PyPI versions](https://img.shields.io/pypi/pyversions/collapse)](https://pypi.org/project/collapse/)
[![Build](https://img.shields.io/travis/JWKennington/collapse)](https://pypi.org/project/collapse/)
[![codecov](https://codecov.io/gh/JWKennington/collapse/branch/master/graph/badge.svg?token=G418VYV5LR)](undefined)
[![CodeFactor Quality](https://img.shields.io/codefactor/grade/github/JWKennington/collapse?&label=codefactor)](https://pypi.org/project/collapse/)
[![License](https://img.shields.io/github/license/JWKennington/collapse?color=magenta&label=License)](https://pypi.org/project/collapse/)



The `collapse` package contains utilities for computing symbolic and numerical expressions related to the time evolution
of collapsing cosmologies. 


## Symbolic Tools
The `collapse` package makes use of `sympy` to compute symbolic curvature equations (EFE).
[Specific Details](./collapse/symbolic/README.md)

### Example Computation: FLRW Cosmology

## Full Example: FLRW Cosmology

```python
# Load the predefined FLRW metric
from collapse.symbolic import metric, gravity
flrw = metric.flrw_metric().subs({'c': 1})
flrw
```


$a+b$


$$a+b$$


$a{\left(t \right)} \left(\operatorname{d}x \otimes \operatorname{d}x + \operatorname{d}y \otimes \operatorname{d}y + \operatorname{d}z \otimes \operatorname{d}z\right) - \operatorname{d}t \otimes \operatorname{d}t$

```python
efe_00 = gravity.einstein_equation(0, 0, flrw).doit()
efe_00
```

$\frac{1}{2} - \frac{3 \frac{d^{2}}{d t^{2}} a{\left(t \right)}}{2 a{\left(t \right)}} + \frac{3 \left(\frac{d}{d t} a{\left(t \right)}\right)^{2}}{4 a^{2}{\left(t \right)}} = \rho$


```python
# Can simplify notation using "dots"
metric.simplify_deriv_notation(efe_00, flrw, use_dots=True)
```

$- \frac{3 \ddot{a}{\left(t \right)}}{2 a{\left(t \right)}} + \frac{3 \dot{a}^{2}{\left(t \right)}}{4 a^{2}{\left(t \right)}} + \frac{1}{2} = \rho$

