import Thermos.Polytropics as Poly
import EngineParts.Engine as Engine
import globals
Engine = Engine.Engine

class TurbineMixer(Engine):
    """
    This is the class responsible for modeling a turbine
    """

    def __init__(self):
        self.gamma = 1.4
        self.mach = 0
        self.pr = 1
        self.tr = None
        self.p05m = None
        self.t05m = None

    def __init__(self, mw=28.8, gamma=1.4, mach=0):
        R = 8314 / mw
        self.cp = (gamma * R) / (gamma - 1)
        self.gamma = gamma
        self.mach = mach
        self.b = globals.b
        self.f = globals.f
        self.tr = None
        self.p05m = None
        self.t05m = None

    def outlet_stagnation_pressure(self, p05_1, t05_1, compressor):
        first_term = (t05_1 / compressor.t03) ** ((self.b / (1 + globals.f)) * (self.gamma / (self.gamma - 1)))
        second_term = (self.t05m / t05_1) ** (self.gamma / (self.gamma - 1))
        self.p05m = p05_1 * first_term * second_term
        return self.p05m

    def outlet_stagnation_temperature(self, t05_1, compressor):
        self.t05m = ((1 + globals.f - self.b) * t05_1 + self.b * compressor.t03) / (1 + globals.f)
        self.tr = self.t05m / t05_1
        return self.t05m

    def compute_outlet(self, p05_1, t05_1, compressor):
        temp = self.outlet_stagnation_temperature(t05_1, compressor)
        return [self.outlet_stagnation_pressure(p05_1, t05_1, compressor), temp]
