import EngineParts.Engine as Engine
import Thermos.Isentropics as Istrop
Engine = Engine.Engine


class Nozzle(Engine):
    """"
    This is the class responsible for modeling a nozzle.
    """

    def __init__(self, mw=28.8, gamma=1.4, mach=0, efficiency=1, pa=10):
        self.R = 8314 / mw
        self.mw = mw
        self.gamma = gamma
        self.efficiency = efficiency
        self.mach = mach
        self.pe = pa
        self.te = None
        self.u = None

    def outlet_stagnation_temperature(self, p0in, t0in):
        t0e = Istrop.press2temp(t0in, None, p0in, self.pe, self.gamma)
        self.te = t0in - self.efficiency * (t0in - t0e)
        return self.te

    def compute_exit_velocity(self, p0in, t0in):
        self.u = (2 * self.efficiency * (self.gamma / (self.gamma - 1)) * self.R * t0in \
                  * (1 - ((self.pe / p0in) ** ((self.gamma - 1) / self.gamma)))) ** 0.5

    def compute_outlet(self, p0in, t0in):
        out = [self.pe, self.outlet_stagnation_temperature(p0in, t0in)];
        self.compute_exit_velocity(p0in, t0in)
        out.append(self.u)
        return out
