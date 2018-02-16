import math
import numpy

from . import base_sampler
from pfnopt import distributions


class RandomSampler(base_sampler.BaseSampler):

    def __init__(self, seed=None):
        self.seed = seed

        self.rng = numpy.random.RandomState(seed)

    def sample(self, distribution, observation_pairs):
        if isinstance(distribution, distributions.UniformDistribution):
            return self.rng.uniform(distribution.low, distribution.high)
        elif isinstance(distribution, distributions.LogUniformDistribution):
            log_low = numpy.log(distribution.low)
            log_high = numpy.log(distribution.high)
            return numpy.exp(self.rng.uniform(log_low, log_high))
        else:
            raise NotImplementedError
