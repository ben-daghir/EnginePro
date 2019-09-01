import globals
import EngineParts.Engine as Engine
import Thermos.Isentropics as Istrop
Engine = Engine.Engine


class CombinedNozzle(Engine):
    """"
    This is the class responsible for modeling a nozzle.
    """

    def __init__(self, mw=28.8, gamma=1.4, efficiency=1, pa=10):
        R = 8314 / mw
        self.cp = gamma * R / (gamma - 1)
        self.mw = 28.8
        self.gamma = gamma
        self.efficiency = efficiency
        self.pec = pa
        self.tec = None
        self.uec = None

    def outlet_stagnation_temperature(self, p07, t07):
        self.tec = t07 * (self.efficiency * ((self.pec / p07) ** ((self.gamma - 1) / self.gamma) - 1) + 1)
        return self.tec

    def compute_exit_velocity(self, t07):
        globals.uec = (2 * self.cp * (t07 - self.tec)) ** 0.5

    def compute_outlet(self, p07, t07):
        out = [self.pec, self.outlet_stagnation_temperature(p07, t07)]
        self.compute_exit_velocity(t07)
        return out

