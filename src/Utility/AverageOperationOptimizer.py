import numpy as np
import globals
import EnginePro

def configurations(i, f, b, fab):
    if i == 1:
        return {"engine": [{'name': 'Diffuser', 'id': 'diffuser-0', 'mw': 28.8, 'gamma': 1.4, 'efficiency': 0.92},
                  {'name': 'Fan', 'id': 'fan-1', 'mw': 28.8, 'gamma': 1.4, 'efficiency': [0.9, True], 'pr': 1.2, 'B': 2.0,
                   'Cb': 0.245},
                  {'name': 'Compressor', 'id': 'compressor-2', 'mw': 28.8, 'gamma': 1.38, 'efficiency': [0.9, True],
                   'pr': 30.0, 'b': b, 'bmax': 0.12},
                  {'name': 'Main Burner', 'id': 'burner-3', 'mw': 28.8, 'gamma': 1.33, 'efficiency': 0.99, 'pr': 0.98,
                   'Q': 45000000.0, 'f': f},
                  {'name': 'Compressor Turbine', 'id': 'turbine-4', 'mw': 28.8, 'gamma': 1.33, 'efficiency': [0.92, True],
                   'Cbl': 700.0, 't_max': 1300.0},
                  {'name': 'Turbine Mixer', 'id': 'turbine_mixer-5', 'mw': 28.8, 'gamma': 1.34},
                  {'name': 'Fan Turbine', 'id': 'turbine-6', 'mw': 28.8, 'gamma': 1.33, 'efficiency': [0.92, True]},
                  {'name': 'After Burner', 'id': 'burner-7', 'mw': 28.8, 'gamma': 1.32, 'efficiency': 0.96,
                   'pr': 0.97, 'Q': 45000000.0, 't_max': 2200.0, 'f': fab},
                  {'name': 'Nozzle Mixer', 'id': 'nozzle_mixer-10', 'prnm': 0.8},
                  {'name': 'Combined Nozzle', 'id': 'combined_nozzle-11', 'mw': 28.8, 'gamma': 1.37, 'efficiency': 0.95}],
                   "mach": 0.85, "pa": 30.1, "ta": 229}

    elif i == 2:
          return {'engine': [{'name': 'Diffuser', 'id': 'diffuser-0', 'mw': 28.8, 'gamma': 1.4, 'efficiency': 0.92},
              {'name': 'Fan', 'id': 'fan-1', 'mw': 28.8, 'gamma': 1.4, 'efficiency': [0.9, True], 'pr': 1.2, 'B': 2.0,
               'Cb': 0.245},
              {'name': 'Compressor', 'id': 'compressor-2', 'mw': 28.8, 'gamma': 1.38, 'efficiency': [0.9, True],
               'pr': 30.0, 'b': b, 'bmax': 0.12},
              {'name': 'Main Burner', 'id': 'burner-3', 'mw': 28.8, 'gamma': 1.33, 'efficiency': 0.99, 'pr': 0.98,
               'Q': 45000000.0, 'f': f},
              {'name': 'Compressor Turbine', 'id': 'turbine-4', 'mw': 28.8, 'gamma': 1.33, 'efficiency': [0.92, True],
               'Cbl': 700.0, 't_max': 1300.0},
              {'name': 'Turbine Mixer', 'id': 'turbine_mixer-5', 'mw': 28.8, 'gamma': 1.34},
              {'name': 'Fan Turbine', 'id': 'turbine-6', 'mw': 28.8, 'gamma': 1.33, 'efficiency': [0.92, True]},
              {'name': 'Nozzle Mixer', 'id': 'nozzle_mixer-10', 'prnm': 0.8},
              {'name': 'Combined Nozzle', 'id': 'combined_nozzle-11', 'mw': 28.8, 'gamma': 1.37, 'efficiency': 0.95}],
                "mach": 0, "pa": 101.3, "ta": 298}

    elif i == 3:
        return {'engine': [{'name': 'Diffuser', 'id': 'diffuser-0', 'mw': 28.8, 'gamma': 1.4, 'efficiency': 0.92},
              {'name': 'Compressor', 'id': 'compressor-2', 'mw': 28.8, 'gamma': 1.38, 'efficiency': [0.9, True],
               'pr': 30.0, 'b': b, 'bmax': 0.12},
              {'name': 'Main Burner', 'id': 'burner-3', 'mw': 28.8, 'gamma': 1.33, 'efficiency': 0.99, 'pr': 0.98,
               'Q': 45000000.0, 'f': f},
              {'name': 'Compressor Turbine', 'id': 'turbine-4', 'mw': 28.8, 'gamma': 1.33, 'efficiency': [0.92, True],
               'Cbl': 700.0, 't_max': 1300.0},
              {'name': 'Turbine Mixer', 'id': 'turbine_mixer-5', 'mw': 28.8, 'gamma': 1.34},
              {'name': 'Core Nozzle', 'id': 'nozzle-8', 'mw': 28.8, 'gamma': 1.35, 'efficiency': 0.95}],
                "mach": 0.8, "pa": 45.6, "ta": 248}

    elif i == 4:
        return {'engine': [{'name': 'Diffuser', 'id': 'diffuser-0', 'mw': 28.8, 'gamma': 1.4, 'efficiency': 0.92},
              {'name': 'Compressor', 'id': 'compressor-2', 'mw': 28.8, 'gamma': 1.38, 'efficiency': [0.9, True],
               'pr': 30.0, 'b': b, 'bmax': 0.12},
              {'name': 'Main Burner', 'id': 'burner-3', 'mw': 28.8, 'gamma': 1.33, 'efficiency': 0.99, 'pr': 0.98,
               'Q': 45000000.0, 'f': f},
              {'name': 'Compressor Turbine', 'id': 'turbine-4', 'mw': 28.8, 'gamma': 1.33, 'efficiency': [0.92, True],
               'Cbl': 700.0, 't_max': 1300.0},
              {'name': 'Turbine Mixer', 'id': 'turbine_mixer-5', 'mw': 28.8, 'gamma': 1.34},
              {'name': 'After Burner', 'id': 'burner-7', 'mw': 28.8, 'gamma': 1.32, 'efficiency': 0.96, 'pr': 0.97,
               'Q': 45000000.0, 't_max': 2200.0, 'f': fab},
              {'name': 'Core Nozzle', 'id': 'nozzle-8', 'mw': 28.8, 'gamma': 1.35, 'efficiency': 0.95}],
                "mach": 0.8, "pa": 45.6, "ta": 248}

def optimize():
    goal_tma = 0.3
    best = {'tsfc': 99}
    for b in np.linspace(0, 0.12, 25):
        for f in np.linspace(0, 0.08, 101):
            for fab in np.linspace(0, 0.08, 101):
                config = configurations(4, f, b, fab)
                globals.reset()
                EnginePro.create_environment(config)
                EnginePro.create_new_engine(config["engine"])
                out = EnginePro.run_analysis()
                if out['out-t-ma'] is not None and out['out-t-ma'] > goal_tma:
                    if best['tsfc'] > out['out-tsfc']:
                        best = {'tsfc': out['out-tsfc'], 'f': globals.f,
                                'fab': globals.fab, 'b': globals.b, 'tma': out['out-t-ma']}
                        print(best)
        print(b)

    print(best)
optimize()