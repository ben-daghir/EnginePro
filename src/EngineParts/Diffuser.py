import EngineParts.Engine as Engine
import Thermos.Isentropics as Istrop
import Thermos.Shocks as Shock
Engine = Engine.Engine


class Diffuser(Engine):
    """"
    This is the class responsible for modeling a diffuser.
    """

    def __init__(self):
        self.gamma = 1.4
        self.efficiency = 1
        self.mach = 0
        self.p01 = None
        self.t01 = None

    def __init__(self, gamma=1.4, mach=0, efficiency=1):
        self.gamma = gamma
        self.efficiency = efficiency
        self.mach = mach
        self.p01 = None
        self.t01 = None

    def outlet_stagnation_pressure(self, pa):
        if self.p01 is None:
            rd = Shock.diffuser_shock_loss(self.mach)
            p0a = Istrop.pressure(None, pa, self.gamma, self.mach)
            self.p01 = rd * pa * ((self.efficiency * ((p0a / pa) ** ((self.gamma - 1) / self.gamma)
                                    - 1) + 1) ** (self.gamma / (self.gamma - 1)))
        return self.p01

    def outlet_stagnation_temperature(self, pa, ta):
        if self.p01 is None:
            self.outlet_stagnation_pressure(pa)
        self.t01 = Istrop.press2temp(None, ta, Istrop.pressure(None, pa, self.gamma, self.mach), pa, self.gamma)
        return self.t01

    def compute_outlet(self, pa, ta):
        return [self.outlet_stagnation_pressure(pa), self.outlet_stagnation_temperature(pa, ta)];

