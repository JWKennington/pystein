"""Utilities for constructing a metric

"""
import functools
import itertools
from typing import Tuple, Union

from sympy import Function, sin, Expr, Array, Derivative as D
from sympy.diffgeom import twoform_to_matrix

from collapse.symbolic import coords
from collapse.symbolic.constants import c
from collapse.symbolic.utilities import tensor_pow as tpow, matrix_to_twoform


class Metric:
    def __init__(self, twoform: Expr = None, matrix: Array = None, coord_system: coords.CoordSystem = None, components: Tuple[Expr, ...] = None):
        if twoform is None and matrix is None:
            raise ValueError('Must specify either twoform or matrix to produce metric')

        # Construct twoform if none given
        if twoform is None:
            if coord_system is None:
                raise ValueError('Must specify coord system if constructing metric from matrix')
            twoform = matrix_to_twoform(matrix, coord_system.base_oneforms())  # TODO check ordering of base oneforms?

        # Construct matrix if none given
        if matrix is None:
            matrix = twoform_to_matrix(twoform)
            coord_system = coords.CoordSystem.from_twoform(twoform)

        # Set instance attributes
        self._twoform = twoform
        self._matrix = matrix
        self._inverse = None  # lazy caching of inverse matrix
        self.coord_system = coord_system
        self.components = components

    def __repr__(self):
        return repr(self.twoform)

    def _repr_latex_(self):
        return self.twoform._repr_latex_()

    @property
    def twoform(self):
        return self._twoform

    @property
    def matrix(self):
        return self._matrix

    @property
    def inverse(self): # TODO include method parameters in here, for instance pseudo inverse
        if self._inverse is None:
            self._inverse = self.matrix.inv()  # only compute once
        return Metric(matrix=self._inverse, coord_system=self.coord_system, components=self.components)

    def subs(self, *args, **kwargs):
        return Metric(twoform=self.twoform.subs(*args, **kwargs),
                      # TODO make the filtering below more robust
                      components=tuple(c for c in self.components if not c.subs(*args, **kwargs).doit().is_constant()))


def general_inhomogeneous_metric():
    cs = coords.toroidal_coords()
    t, r, theta, _ = cs.base_symbols()
    dt, dr, dtheta, dphi = cs.base_oneforms()

    # Create generic isotropic metric component functions
    M = Function('M')(t, r)
    N = Function('N')(t, r)
    L = Function('L')(t, r)
    S = Function('S')(t, r)

    form = - c ** 2 * N ** 2 * tpow(dt, 2) + \
           L ** 2 * tpow(dr + c * M * dt, 2) + \
           S ** 2 * (tpow(dtheta, 2) + sin(theta) ** 2 * tpow(dphi, 2))
    return Metric(twoform=form, components=(M, N, L, S))


def friedmann_lemaitre_roberston_walker_metric():
    cs = coords.cartesian_coords()
    t, *_ = cs.base_symbols()
    dt, dx, dy, dz = cs.base_oneforms()
    a = Function('a')(t)
    form = - c ** 2 * tpow(dt, 2) + a * (tpow(dx, 2) + tpow(dy, 2) + tpow(dz, 2))
    return Metric(twoform=form, components=(a,))


flrw_metric = friedmann_lemaitre_roberston_walker_metric  # shorthand for conventional names


def _deriv_simplify_rule(component: Function, variables: Union[Expr, Tuple[Expr,...]], use_dots: bool = False):
    if not isinstance(variables, tuple): # TODO make this "boxing" more robust
        variables = (variables,)
    args = component.args
    order = len(variables)
    key = functools.reduce(lambda a, b: D(a, b), (component,) + variables)

    if any(v not in args for v in variables):  # check against simplified
        return (key, 0)

    if len(args) == 1:
        fmt = ('\\' + order * 'd' + 'ot{{{}}}') if use_dots else ('{}' + order * '\'')
        return (key, Function(fmt.format(component.name))(*args))
    fmt = '{}_' + '{{' + ' '.join([v.name for v in variables]) + '}}'
    return (key, Function(fmt.format(component.name))(*args))


def simplify_deriv_notation(expr: Expr, metric: Metric, max_order: int = 2, use_dots: bool = False):
    # Create Simplification Shorthand
    components = tuple(sorted(metric.components, key=lambda x: x.name))
    variables = metric.coord_system.base_symbols()
    rules = []
    for n in range(1, max_order + 1):
        n_order_rules = [_deriv_simplify_rule(c, vs, use_dots=use_dots) for c, vs in itertools.product(components, itertools.product(*(n*[variables])))]
        rules.extend(n_order_rules)
    return expr.subs(dict(rules))