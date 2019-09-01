import globals
import EnginePro
import numpy as np

# # config 1
goal_tma = 2.74
M = 0
Pa = 101.3
Ta = 298

# config 2
# goal_tma = 0.825
# M = 0.85
# Pa = 30.1
# Ta = 229

# config 3
# goal_tma = 0.3
# M = 0.80
# Pa = 45.6
# Ta = 248

# config 4
# goal_tma = 0.7
# M = 2.4
# Pa = 11.6
# Ta = 216

good_configs = []
best = None


def min_config(out, parts, f, b, fab):
    global good_configs
    global best
    global goal_tma

    if "Main Burner" in parts and "Compressor Turbine" in parts and "Compressor" in parts \
        and (("Fan" in parts and "Fan Turbine" in parts) or ("Fan" not in parts and "Fan Turbine")) \
        and "Turbine Mixer" in parts and ((("Core Nozzle" in parts or "Fan Nozzle" in parts) and "Combined Nozzle" not in parts)\
        or (("Core Nozzle" not in parts and "Fan Nozzle" not in parts) and ("Combined Nozzle" in parts and "Nozzle Mixer" in parts))):

        if ((out["out-t-ma"] is not None and out["out-t-ma"] > goal_tma) \
                or (out["out-t-ma-c"] is not None and out["out-t-ma-c"] > goal_tma)) and out['out-fmax'] > 0:

            if "Combined Nozzle" in parts:
                tsfc = out["out-tsfc-c"]
                tma = out["out-t-ma-c"]
            else:
                tsfc = out["out-tsfc"]
                tma = out["out-t-ma"]
        #
        #     if out["out-t-ma-c"] is None:
        #         tsfc = out["out-tsfc"]
        #         tma = out["out-t-ma"]
        #     elif out["out-t-ma"] is None:
        #         tsfc = out["out-tsfc-c"]
        #         tma = out["out-t-ma-c"]
        #     elif out["out-t-ma-c"] > goal_tma and out["out-t-ma"] < goal_tma:
        #         tsfc = out["out-tsfc-c"]
        #         tma = out["out-t-ma-c"]
        #     elif out["out-t-ma-c"] < goal_tma and out["out-t-ma"] > goal_tma:
        #         tsfc = out["out-tsfc"]
        #         tma = out["out-t-ma"]
        #     elif out["out-tsfc"] is None or out["out-tsfc"] < 0:
        #         tsfc = out["out-tsfc-c"]
        #         tma = out["out-t-ma-c"]
        #     elif out["out-t-ma-c"] is None or out["out-t-ma-c"] < 0:
        #         tsfc = out["out-tsfc"]
        #         tma = out["out-t-ma"]
        #     elif out["out-t-ma-c"] < out["out-t-ma"]:
        #         tsfc = out["out-t-ma-c"]
        #         tma = out["out-t-ma-c"]
        #     else:
        #         tsfc = out["out-t-ma"]
        #         tma = out["out-t-ma"]

            good_configs.append({"parts": parts,
                                 "t-ma": tma,
                                 "f": f,
                                 "b": b,
                                 "fab": fab,
                                 "f_max": globals.fmax,
                                 "fab_max": globals.fmax_ab,
                                 'ff': input_f,
                                 'ffab': input_fab})

            if best is None:
                best = {"parts": parts,
                        "t-ma": tma,
                        "f": globals.f,
                        "b": globals.b,
                        "fab": globals.fab,
                        "f_max": globals.fmax,
                        "fab_max": globals.fmax_ab,
                        "tsfc": tsfc,
                        'ff': input_f,
                        'ffab': input_fab}
                print(best)
            else:
                if best["tsfc"] > tsfc:
                    best = {"parts": parts,
                            "t-ma": tma,
                            "f": globals.f,
                            "b": globals.b,
                            "fab": globals.fab,
                            "f_max": globals.fmax,
                            "fab_max": globals.fmax_ab,
                            "tsfc": tsfc,
                            'ff': input_f,
                            'ffab': input_fab}
                    print(best)


def analyze(parts, f, b, fab):
    global M
    global Pa
    global Ta
    globals.reset()
    globals.Engine = EnginePro.Engine.Engine()
    EnginePro.create_environment({"mach": M,
                                  "pa": Pa,
                                  "ta": Ta})
    final_parts = []
    try:
        for part in parts:
            if part['name'] != "None":
                EnginePro.add_part(part)
                final_parts.append(part["name"])

        output = EnginePro.run_analysis()
        min_config(output, final_parts, f, b, fab)
    except:
        ww=0


counter = 0
def optimize(f_a, b_a=0.1, fab=0):
    global counter
    engine = [{'name': 'Diffuser', 'id': 'diffuser-0', 'mw': 28.8, 'gamma': 1.4, 'efficiency': 0.92},
                {'name': 'Fan', 'id': 'fan-1', 'mw': 28.8, 'gamma': 1.4, 'efficiency': [0.9, True], 'pr': 1.2, 'B': 2.0,
                 'Cb': 0.245},
                {'name': 'Compressor', 'id': 'compressor-2', 'mw': 28.8, 'gamma': 1.38, 'efficiency': [0.9, True],
                 'pr': 30.0, 'b': b_a, 'bmax': 0.12},
                {'name': 'Main Burner', 'id': 'burner-3', 'mw': 28.8, 'gamma': 1.33, 'efficiency': 0.99, 'pr': 0.98,
                 'Q': 45000000.0, 'f': f_a},
                {'name': 'Compressor Turbine', 'id': 'turbine-4', 'mw': 28.8, 'gamma': 1.33, 'efficiency': [0.92, True],
                 'Cbl': 700.0, 't_max': 1300.0},
                {'name': 'Turbine Mixer', 'id': 'turbine_mixer-5', 'mw': 28.8, 'gamma': 1.34},
                {'name': 'Fan Turbine', 'id': 'turbine-6', 'mw': 28.8, 'gamma': 1.33, 'efficiency': [0.92, True]},
                {'name': 'After Burner', 'id': 'burner-7', 'mw': 28.8, 'gamma': 1.32, 'efficiency': 0.96, 'pr': 0.97,
                 'Q': 45000000.0, 't_max': 2200.0, 'f': fab},
                {'name': 'Core Nozzle', 'id': 'nozzle-8', 'mw': 28.8, 'gamma': 1.35, 'efficiency': 0.95},
                {'name': 'Fan Nozzle', 'id': 'nozzle-9', 'mw': 28.8, 'gamma': 1.4, 'efficiency': 0.97},
                {'name': 'Nozzle Mixer', 'id': 'nozzle_mixer-10', 'prnm': 0.8},
                {'name': 'Combined Nozzle', 'id': 'combined_nozzle-11', 'mw': 28.8, 'gamma': 1.37, 'efficiency': 0.95},
                {'name': "None"}]

    length = len(engine)
    for a in range(0, len(engine)):

        part1 = engine[a]

        for b in range(a + 1, length):
            part2 = engine[b]
            if b == 11:
                b = b - 1

            for c in range(b + 1, length):
                part3 = engine[c]
                if c == 12:
                    c = c - 1

                for d in range(c + 1, length):
                    part4 = engine[d]
                    if d == 12:
                        d = d - 1

                    for e in range(d + 1, length):
                        part5 = engine[e]
                        if e == 12:
                            e = e - 1

                        for f in range(e + 1, length):
                            part6 = engine[f]
                            if f == 12:
                                f = f - 1

                            for g in range(f + 1, length):
                                part7 = engine[g]
                                if g == 12:
                                    g = g - 1

                                for h in range(g + 1, length):
                                    part8 = engine[h]
                                    if h == 12:
                                        h = h - 1

                                    for i in range(h + 1, length):
                                        part9 = engine[i]
                                        if i == 12:
                                            i = i - 1

                                        for j in range(i + 1, length):
                                            part10 = engine[j]
                                            if j == 12:
                                                j = j - 1

                                            for k in range(j + 1, length):
                                                part11 = engine[k]
                                                if k == 12:
                                                    k = k - 1

                                                for l in range(k + 1, length):
                                                    part12 = engine[l]
                                                    parts = [part1, part2, part3,
                                                             part4, part5, part6,
                                                             part7, part8, part9,
                                                             part10, part11, part12]
                                                    counter = counter + 1
                                                    analyze(parts, f_a, b_a, fab)

input_f = 0
input_fab = 0
def over_f():
    c = 1
    global input_f
    global input_fab
    for b in np.linspace(0, 0.12, 5):
        for f in np.linspace(0, 0.05, 20):
            for fab in np.linspace(0, 0.075, 10):
                input_f = f
                input_fab = fab
                print(c, f, fab, b)
                optimize(f, b, fab)
                c = c + 1

over_f()
print(good_configs)
print(best)
print(len(good_configs))
print("done")
