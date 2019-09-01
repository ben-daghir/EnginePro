import EngineParts.Engine as Engine
import Thermos.Polytropics as Poly
Engine = Engine.Engine


class Compressor(Engine):
    """
    This is the class responsible for modeling a compressor
    """

    def __init__(self):
        self.gamma = 1.4
        self.mach = 0
        self.efficiency = 1
        self.pr = 1
        self.W_m = None
        self.p03 = None
        self.t03 = None

    def __init__(self, mw=28.8, gamma=1.4, efficiency=(1, False), pr=1):
        R = 8314 / mw
        self.cp = (gamma * R) / (gamma - 1)
        self.gamma = gamma
        self.pr = pr
        if efficiency[1]:
            self.efficiency = Poly.fan_compressor_p2a(efficiency[0], pr, gamma)
        else:
            self.efficiency = efficiency[0]
        self.W_m = None
        self.p03 = None
        self.t03 = None

    def outlet_stagnation_pressure(self, p0in):
        self.p03 = self.pr * p0in
        return self.p03

    def outlet_stagnation_temperature(self, t0in):
        self.t03 = t0in * (1 + (1 / self.efficiency) * (self.pr ** ((self.gamma - 1) / self.gamma) - 1))
        self.W_m = self.cp * (self.t03 - t0in)
        return self.t03

    def compute_outlet(self, p0in, t0in):
        return [self.outlet_stagnation_pressure(p0in), self.outlet_stagnation_temperature(t0in)];
