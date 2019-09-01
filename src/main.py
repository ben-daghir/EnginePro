from EngineParts import Engine, Diffuser, Fan, Compressor, CombinedNozzle, Burner, Turbine, TurbineMixer, Nozzle, NozzleMixer
import globals
from Utility import SciFi
import globals
globals.mach = 1.5
globals.f = 0.018
globals.fab = 0.01
globals.B = 2
globals.ta = 220
globals.pa = 10
globals.u = globals.mach * ((1.4 * (8314 / 28.8) * globals.ta) ** 0.5)
globals.Cb1 = .245
globals.Qr = 45e6
globals.b = 0.1

diff = Diffuser.Diffuser(1.4, globals.mach, 0.92)
out1 = diff.compute_outlet(globals.pa, globals.ta)

fan = Fan.Fan(28.8, 1.4, globals.mach, (0.9, True), 1.2, globals.B)
out2 = fan.compute_outlet(out1[0], out1[1])

comp = Compressor.Compressor(28.8, 1.38, (0.9, True), 30)
out3 = comp.compute_outlet(out2[0], out2[1])

burn = Burner.Burner(28.8, 1.33, globals.mach, .99, .98, None, 45e6, 0.018, globals.b)
out4 = burn.compute_outlet(out3[0], out3[1])

turbine1 = Turbine.Turbine(28.8, 1.33, globals.mach, (.92, True), None, 0.1)
out5_1 = turbine1.compute_outlet(out4[0], out4[1], comp.W_m)

turbinem = TurbineMixer.TurbineMixer(28.8, 1.34, globals.mach)
out5_m = turbinem.compute_outlet(out5_1[0], out5_1[1], comp)

turbine2 = Turbine.Turbine(28.8, 1.33, globals.mach, (0.92, True), None, 0)
out5_2 = turbine2.compute_outlet(out5_m[0], out5_m[1], fan.W_m)

afterburner = Burner.Burner(28.8, 1.32, globals.mach, .96, .97, 2200, 45e6, 0.01, 0)
out6 = afterburner.compute_outlet(out5_2[0], out5_2[1])

corenozzle = Nozzle.Nozzle(28.8, 1.35, globals.mach, 0.95, globals.pa)
oute = corenozzle.compute_outlet(out6[0], out6[1])

fannozzle = Nozzle.Nozzle(28.8, 1.4, globals.mach, 0.97, globals.pa)
outef = fannozzle.compute_outlet(out2[0], out2[1])

nozzlemixer = NozzleMixer.NozzleMixer(0.80)
out7 = nozzlemixer.compute_outlet(out2[1], out6[1], out2[0], out6[0])

combinednozzle = CombinedNozzle.CombinedNozzle(28.8, 1.37, 0.95, globals.pa)
outec = combinednozzle.compute_outlet(out7[0], out7[1])

Uec = combinednozzle.compute_exit_velocity(out7[0])
Ue = corenozzle.compute_exit_velocity(out6[0], out6[1])
Uef = fannozzle.compute_exit_velocity(out2[0], out2[1])

d = globals.Cb1 * (globals.mach ** 2) * (globals.pa / 101.3) * (globals.B ** 1.5)
T_ma = (((1 + globals.f + globals.fab) * Ue) + (globals.B * Uef) - ((1 + globals.B) * globals.u))
T_ma = T_ma / 1000 - d

TSFC = (globals.f + globals.fab) / T_ma

n_th = 100 * ((1 + globals.f + globals.fab) * ((1183 ** 2) / 2) + globals.B * ((Uef ** 2) / 2) - (1 + globals.B) * ((globals.u ** 2) / 2)) / ((globals.f + globals.fab) * globals.Qr)
n_o = 100 * globals.u / (globals.Qr * (TSFC / 1000))
w_c = comp.W_m / 1000
w_ft = fan.W_m / 1000


out1r = SciFi.round_sig(out1, 4)
out2r = SciFi.round_sig(out2, 4)
out3r = SciFi.round_sig(out3, 4)
out4r = SciFi.round_sig(out4, 4)
out5_1r = SciFi.round_sig(out5_1, 4)
out5_mr = SciFi.round_sig(out5_m, 4)
out5_2r = SciFi.round_sig(out5_2, 4)
out6r = SciFi.round_sig(out6, 4)
outer = SciFi.round_sig(oute, 4)
outefr = SciFi.round_sig(outef, 4)
out7r = SciFi.round_sig(out7, 4)


print(out1r)
print(out2r)
print(out3r)
print(out4r)
print(out5_1r)
print(out5_mr)
print(out5_2r)
print(out6r)
print(outer)
print(outefr)
print(out7r)

