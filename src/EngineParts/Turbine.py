import Thermos.Polytropics as Poly
import EngineParts.Engine as Engine
import globals
Engine = Engine.Engine

class Turbine(Engine):
    """
    This is the class responsible for modeling a turbine
    """

    def __init__(self, mw=28.8, gamma=1.4, mach=0, efficiency=(1, False), tmax=1300, b=0.1):
        R = 8314 / mw
        self.cp = (gamma * R) / (gamma - 1)
        self.gamma = gamma
        self.mach = mach
        self.b = b
        self.efficiency = efficiency
        self.tmax = tmax
        self.tr = None
        self.p05_x = None
        self.t05_x = None

    def outlet_stagnation_pressure(self, p0in):
        self.p05_x = p0in * ((1 - (1 / self.efficiency) * (1 - self.tr)) ** (self.gamma / (self.gamma - 1)))
        return self.p05_x

    def outlet_stagnation_temperature(self, t0in, power):
        self.t05_x = t0in - (power / (self.cp * (1 + globals.f - self.b)))
        self.tr = self.t05_x / t0in
        if self.efficiency[1]:
            self.efficiency = Poly.turbine_p2a(self.efficiency[0], self.tr)
        else:
            self.efficiency = self.efficiency[0]
        return self.t05_x

    def compute_outlet(self, p0in, t0in, power):
        temp = self.outlet_stagnation_temperature(t0in, power)
        return [self.outlet_stagnation_pressure(p0in), temp]
