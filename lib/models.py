import numpy as np
from lmfit import Model

def linear(x, slope=1.0, intercept=0.0):
    return slope * x + intercept

class LinearModel(Model):
    def __init__(self, independent_vars=['x'], prefix='', nan_policy='raise',
                 **kwargs):
        kwargs.update({'prefix': prefix, 'nan_policy': nan_policy,
                       'independent_vars': independent_vars})
        super().__init__(linear, **kwargs)

    def guess(self, data, x=None, **kwargs):
        """Estimate initial model parameter values from data."""
        sval, oval = 0., 0.
        if x is not None:
            sval, oval = np.polyfit(x, data, 1)
        pars = self.make_params(intercept=oval, slope=sval)
        return models.update_param_vals(pars, self.prefix, **kwargs)

def ggrowth(x, r, m, c0):
    # Generalized growth https://www.sciencedirect.com/science/article/pii/S1755436516000037
    a = c0 ** (1/m)
    return ((r/m) * x + a) ** m

class GeneralizedGrowthModel(Model):
    def __init__(self, independent_vars=['x'], prefix='', nan_policy='raise',
                 **kwargs):
        kwargs.update({'prefix': prefix, 'nan_policy': nan_policy,
                       'independent_vars': independent_vars})
        super().__init__(ggrowth, **kwargs)