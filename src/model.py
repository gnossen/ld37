import random

class NormalScalar(object):
    def __init__(self, mu, sigma, seed=None):
        self.mu = mu
        self.sigma = sigma
        self.seed = seed
        if seed is not None:
            random.seed(seed)

    def __call__(self):
        return random.normalvariate(self.mu, self.sigma)

class RandomSelection(object):
    def __init__(self, options, seed=None):
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self.options = self.normalize_options(options) 

    def normalize_options(self, raw_options):
        total_frequency = sum([freq for freq, _ in raw_options])
        options = []
        accum = 0.0
        for freq, value in raw_options:
            entry = (accum, value)
            options.append(entry)
            accum += freq / float(total_frequency)
        return options

    def __call__(self):
        rand_val = random.random()
        for i, (freq, _) in enumerate(self.options):
            if freq > rand_val:
                return self.options[i-1][1]
        else:
            return self.options[-1][1]

class DictCombinator(object):
    def __init__(self, entries, seed=None):
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self.entries = entries

    def __call__(self):
        ret_dict = {}
        for key, value in self.entries.iteritems():
            ret_dict[key] = value()
        return ret_dict
        
class Model(object):
    def __init__(self, props=None, seed=None, **kwargs):
        if props is None:
            props = {}
            for key, value in kwargs.iteritems():
                if key in self.__class__.props:
                    props[key] = value

        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self.process_props(props)

    def process_props(self, props):
        for prop in self.__class__.props:
            if prop not in props:
                self.gen_prop(prop)
            else:
                self.__dict__[prop] = props[prop]

    def gen_prop(self, prop):
        if prop in self.__class__.__dict__:
            self.__dict__[prop] = self.__class__.__dict__[prop]()
        else:
            gen_func_name = "gen_{}".format(prop)
            self.__class__.__dict__[gen_func_name](self)
