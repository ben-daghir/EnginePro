import EnginePro
import globals
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


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
                   "mach": 0, "pa": 101.3, "ta": 298}

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
                "mach": 0.85, "pa": 30.1, "ta": 229}

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
                "mach": 2.4, "pa": 11.6, "ta": 216}

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 15}

matplotlib.rc('font', **font)

def maximize_thrust_1():
    f_data_ab_on = []
    f_data_ab_off = []
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    for b in np.flip(np.linspace(0, .12, 7)):
        config = configurations(1, 0, b, 0)
        EnginePro.create_environment(config)
        EnginePro.create_new_engine(config["engine"])
        out = EnginePro.run_analysis()
        f_max = out['out-fmax']

        tm_f = []
        for f in np.linspace(0, f_max, 100):
            globals.reset()
            config = configurations(1, f, b, 0)
            EnginePro.create_environment(config)
            EnginePro.create_new_engine(config["engine"])
            out = EnginePro.run_analysis()
            fab_max = out['out-fmax,ab']
            globals.reset()
            config = configurations(1, f, b, fab_max)
            EnginePro.create_environment(config)
            EnginePro.create_new_engine(config["engine"])
            out = EnginePro.run_analysis()
            tm_f.append(out["out-t-ma-c"])
        f_data_ab_on.append({'b': b, "f": np.linspace(0, f_max, 100), "t_m": tm_f})
        ax1.plot(np.linspace(0, f_max, 100), tm_f, '-')

        tm_f = []
        for f in np.linspace(0, f_max, 100):
            globals.reset()
            config = configurations(1, f, b, 0)
            EnginePro.create_environment(config)
            EnginePro.create_new_engine(config["engine"])
            out = EnginePro.run_analysis()
            tm_f.append(out["out-t-ma-c"])
        f_data_ab_off.append({'b': b, "f": np.linspace(0, f_max, 100), "t_m": tm_f})
        ax2.plot(np.linspace(0, f_max, 100), tm_f, '--')

    ax1.set_xlabel('Fuel to Air Ratio, Main Burner')
    ax1.set_ylabel('Specific Thrust, Afterburner On (Solid)')
    ax2.set_ylabel('Specific Thrust, Afterburner Off (Dashed)')
    ax1.legend(['b = 0.12', 'b = 0.10', 'b = 0.08', 'b = 0.06', 'b = 0.04', 'b = 0.02', 'b = 0.00'], loc='upper left')
    ax2.legend(['b = 0.12', 'b = 0.10', 'b = 0.08', 'b = 0.06', 'b = 0.04', 'b = 0.02', 'b = 0.00'], loc='lower right')


def maximize_thrust_2():
    f_data_ab_off = []
    fig, ax1 = plt.subplots()
    for b in np.flip(np.linspace(0, .12, 7)):
        globals.reset()
        config = configurations(2, 0, b, 0)
        EnginePro.create_environment(config)
        EnginePro.create_new_engine(config["engine"])
        out = EnginePro.run_analysis()
        f_max = out['out-fmax']
        tm_f = []
        for f in np.linspace(0, f_max, 100):
            globals.reset()
            config = configurations(2, f, b, 0)
            EnginePro.create_environment(config)
            EnginePro.create_new_engine(config["engine"])
            out = EnginePro.run_analysis()
            tm_f.append(out["out-t-ma-c"])
        f_data_ab_off.append({'b': b, "f": np.linspace(0, f_max, 100), "t_m": tm_f})
        ax1.plot(np.linspace(0, f_max, 100), tm_f, '-')

    ax1.set_xlabel('Fuel to Air Ratio, Main Burner')
    ax1.set_ylabel('Specific Thrust')
    ax1.legend(['b = 0.12', 'b = 0.10', 'b = 0.08', 'b = 0.06', 'b = 0.04', 'b = 0.02', 'b = 0.00'], loc='upper left')


def maximize_thrust_3():
    f_data_ab_off = []
    fig, ax1 = plt.subplots()
    for b in np.flip(np.linspace(0, .12, 7)):
        globals.reset()
        config = configurations(3, 0, b, 0)
        EnginePro.create_environment(config)
        EnginePro.create_new_engine(config["engine"])
        out = EnginePro.run_analysis()
        f_max = out['out-fmax']
        tm_f = []
        for f in np.linspace(0, f_max, 100):
            globals.reset()
            config = configurations(3, f, b, 0)
            EnginePro.create_environment(config)
            EnginePro.create_new_engine(config["engine"])
            out = EnginePro.run_analysis()
            tm_f.append(out["out-t-ma"])
        f_data_ab_off.append({'b': b, "f": np.linspace(0, f_max, 100), "t_m": tm_f})
        ax1.plot(np.linspace(0, f_max, 100), tm_f, '-')

    ax1.set_xlabel('Fuel to Air Ratio, Main Burner')
    ax1.set_ylabel('Specific Thrust')
    ax1.legend(['b = 0.12', 'b = 0.10', 'b = 0.08', 'b = 0.06', 'b = 0.04', 'b = 0.02', 'b = 0.00'], loc='upper left')


def maximize_thrust_4():
    f_data_ab_on = []
    f_data_ab_off = []
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    for b in np.flip(np.linspace(0, .12, 7)):
        config = configurations(4, 0, b, 0)
        EnginePro.create_environment(config)
        EnginePro.create_new_engine(config["engine"])
        out = EnginePro.run_analysis()
        f_max = out['out-fmax']

        tm_f = []
        for f in np.linspace(0, f_max, 100):
            globals.reset()
            config = configurations(4, f, b, 0)
            EnginePro.create_environment(config)
            EnginePro.create_new_engine(config["engine"])
            out = EnginePro.run_analysis()
            fab_max = out['out-fmax,ab']
            globals.reset()
            config = configurations(4, f, b, fab_max)
            EnginePro.create_environment(config)
            EnginePro.create_new_engine(config["engine"])
            out = EnginePro.run_analysis()
            tm_f.append(out["out-t-ma"])
        f_data_ab_on.append({'b': b, "f": np.linspace(0, f_max, 100), "t_m": tm_f})
        ax1.plot(np.linspace(0, f_max, 100), tm_f, '-')

        tm_f2 = []
        for f in np.linspace(0, f_max, 100):
            globals.reset()
            config = configurations(4, f, b, 0)
            EnginePro.create_environment(config)
            EnginePro.create_new_engine(config["engine"])
            out = EnginePro.run_analysis()
            tm_f2.append(out["out-t-ma"])
        f_data_ab_off.append({'b': b, "f": np.linspace(0, f_max, 100), "t_m": tm_f2})
        ax2.plot(np.linspace(0, f_max, 100), tm_f2, '--')

    ax1.set_xlabel('Fuel to Air Ratio, Main Burner')
    ax1.set_ylabel('Specific Thrust, Afterburner On (Solid)')
    ax2.set_ylabel('Specific Thrust, Afterburner Off (Dashed)')
    ax1.legend(['b = 0.12', 'b = 0.10', 'b = 0.08', 'b = 0.06', 'b = 0.04', 'b = 0.02', 'b = 0.00'], loc='upper left')
    ax2.legend(['b = 0.12', 'b = 0.10', 'b = 0.08', 'b = 0.06', 'b = 0.04', 'b = 0.02', 'b = 0.00'], loc='lower right')


t1 = maximize_thrust_1()
t2 = maximize_thrust_2()
t3 = maximize_thrust_3()
t4 = maximize_thrust_4()
print("done.")



