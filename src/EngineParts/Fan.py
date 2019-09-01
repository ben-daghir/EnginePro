import EngineParts.Engine as Engine
import Thermos.Polytropics as Poly
Engine = Engine.Engine


class Fan(Engine):
    """
    This is the class responsible for modeling a fan.
    """

    def __init__(self, mw=28.8, gamma=1.4, mach=0, efficiency=(1, True), pr=1, bypass=1, cb=1):
        R = 8314 / mw
        self.Cp = gamma * R / (gamma - 1)
        self.gamma = gamma
        self.mach = mach
        if efficiency[1]:
            self.efficiency = Poly.fan_compressor_p2a(efficiency[0], pr, gamma)
        else:
            self.efficiency = efficiency[0]
        self.pr = pr
        self.bypass = bypass
        self.Cb = cb
        self.W_m = None
        self.p02 = None
        self.t02 = None

    def outlet_stagnation_pressure(self, p0in):
        self.p02 = self.pr * p0in
        return self.p02

    def outlet_stagnation_temperature(self, t0in):
        self.t02 = t0in * (1 + (1 / self.efficiency) * (self.pr ** ((self.gamma - 1) / self.gamma) - 1))
        self.W_m = (1 + self.bypass) * self.Cp * (self.t02 - t0in)
        return self.t02

    def compute_outlet(self, p0in, t0in):
        return [self.outlet_stagnation_pressure(p0in), self.outlet_stagnation_temperature(t0in)]
