import EngineParts.Engine as Engine
import globals
Engine = Engine.Engine

class Burner(Engine):
    """
    This class is responsible for modeling a burner
    """

    def __init__(self, mw=28.8, gamma=1.4, mach=0, efficiency=1, pr=0.95, tmax=None, q=45e6, f=.018, b=1):
        R = 8314 / mw
        self.cp = (gamma * R) / (gamma - 1)
        self.gamma = gamma
        self.mach = mach
        self.efficiency = efficiency
        self.pr = pr
        self.Q = q
        self.f = f
        self.b = b
        self.p04 = None
        self.t04 = None
        self.fmax = None

    def outlet_stagnation_pressure(self, p0in):
        self.p04 = self.pr * p0in
        return self.p04

    def outlet_stagnation_temperature(self, t0in, b, f):
        self.t04 = t0in * ((((f * self.Q * self.efficiency) / (self.cp * t0in)) + 1 - b) \
                   / (1 - b + f))

        return self.t04

    def compute_fmax(self, t0in, tmax, b):
        self.fmax = ((b - 1) + ((1 - b) * (tmax / t0in))) \
                    / (((self.efficiency * self.Q) / (self.cp * t0in)) - (tmax / t0in))
        return self.fmax

    def compute_outlet(self, p0in, t0in, tmax, b, f):
        fmax = self.compute_fmax(t0in, tmax, b)
        if fmax < 0:
            fmax = 0
        if f > fmax:
            f = fmax
        self.f = f
        return [self.outlet_stagnation_pressure(p0in), self.outlet_stagnation_temperature(t0in, b, f),
                fmax]

