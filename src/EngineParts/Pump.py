import globals

n_fp = 0.35
rho_f = 780
p_f1 = 104
dp_inj = 550


def compute_pump_work():
    return ((globals.f + globals.fab) * (globals.p03 + dp_inj - p_f1)) / (rho_f * n_fp)
