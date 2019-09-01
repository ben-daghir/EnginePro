import EngineParts.Engine as Engine
from Thermos import Isentropics as Isen
from Thermos import Polytropics as Poly
import globals
Engine = Engine.Engine


class NozzleMixer(Engine):
    """"
    This is the class responsible for modeling a nozzle mixer.
    """

    def __init__(self, prnm=1):
        self.gamma = 1.36
        self.prnm = prnm
        self.B = globals.B
        self.f = globals.f
        self.fab = globals.fab
        self.p07 = None
        self.t07 = None

    def outlet_stagnation_pressure(self, t02, t06, p02, p06):
        first_term = (t02 / self.t07) ** ((self.gamma/(self.gamma - 1)) * (self.B / (1 + globals.fab + globals.f)))
        second_term = (self.t07 / t06) ** (-self.gamma / (self.gamma - 1))
        third_term = p02 ** (-self.B / (1 + globals.fab + globals.f))
        fourth_term = p06 ** -1
        p07_rev = (first_term * second_term * third_term * fourth_term) \
                    ** (1 / (-(self.B / (1 + globals.fab + globals.f)) - 1))
        return p07_rev * self.prnm

    def outlet_stagnation_temperature(self, t02, t06):
        return ((self.B * t02) + (1 + globals.fab + globals.f) * t06) / (1 + globals.fab + globals.f + self.B)

    def compute_outlet(self, t02, t06, p02, p06):
        self.t07 = self.outlet_stagnation_temperature(t02, t06)
        self.gamma = Poly.nozzle_mixer(self.t07)
        globals.gamma_nm = self.gamma
        self.p07 = self.outlet_stagnation_pressure(t02, t06, p02, p06)
        return [self.p07, self.t07]

