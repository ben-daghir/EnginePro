

def fan_compressor_p2a(np, pr, gamma):
    """"
    :param np: the polytropic efficiency
    :param pr: the pressure ratio specific to the component
    :param gamma: the ratio of specific heats specific to the component
    :return: the equivalent adiabatic efficiency
    """
    return ((pr ** ((gamma - 1)/gamma)) - 1) / ((pr ** ((gamma - 1) / (gamma * np))) - 1)


def turbine_p2a(np, tr):
    """
    :param np: the polytropic efficiency
    :param tr: the temperature ratio of the turbine
    :return: the equivalent adiabatic efficiency
    """
    return (tr - 1) / ((tr ** (1 / np)) - 1)


def nozzle_mixer(T0in):
    """
    :param T0in: the stagnation temperature before the nozzle mixer
    :return: the specific heat ratio
    """
    return 1.44 - (1.39e-4 * T0in) + 3.57e-8 * (T0in ** 2)
