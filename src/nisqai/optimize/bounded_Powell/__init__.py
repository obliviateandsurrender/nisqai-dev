"""
Find the global minimium of a f with a bounded Powell method.
    - Joseph Iosue, joe.iosue@qcware.com

f: function of x and args to minimized. Called with f(x, *args)
x0: list type. Initial guess of parameters.
args : tuple, optional. Extra arguments passed to the objective function.
maxfev : int, maximum number of function evaluations to perform.
              Note that the qPowell methods may go slightly over this
              limit, since they will not halt in the middle of an 
              iteration. The default is 2000.
xtol: Relative tolerance for the parameters for convergence. The default is
      1e-4 (same as SciPy's Powell method).
ftol: Relative tolerance for the function for convergence. The default is
      1e-4 (same as SciPy's Powell method).
direc: initial set of direction vectors for the qPowell methods. The
       default are the standard basis unit vectors along each 
       parameter's directions.
maxls: int, maximum function evaluations used at each linesearch. Default
            is no max.
method: str, which qPowell method to use. The default is None or "", which 
             defaults to just the standard qPowell method. The other option
             is "locally-bounded".
lower_bound: list or array of numbers. lower_bound[i] is the lower bound
                                       of the i^th parameter in x0. If no
                                       lower_bound is provided, then -pi
                                       will be used.
upper_bound: list or array of numbers. upper_bound[i] is the upper bound
                                       of the i^th parameter in x0. If no
                                       upper_bound is provided, then pi
                                       will be used.
callback: function of x, called after each iteration.
gs: boolean, whether or not to use gram schmidt to keep direcs orthogonal.
    
Returns scipy.minimize.OptimizeResult
    See scipy's doucmentation for a description of attributes.

Examples usage:

    >>> from nisqai.optimize import minimize
    >>> res = minimize(
    >>>     [function],
    >>>     [initial params],
    >>>     options={
                'method'='locally_bounded', 
                'maxfev': 500,
                'xtol': 1e-2,
                'ftol': 1e-2,
                ...
            },
    >>>     method="bounded_Powell",
    >>>     callback=[callback function]
    >>> )
"""

from ._bounded_Powell import bounded_Powell
__str__ = "bounded_Powell"
__all__ = __str__,
