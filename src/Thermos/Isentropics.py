def pressure(p0, p, gamma, mach):
    """
    This is the isentropic relationship for pressure. If p0 is None
    we will find p0. If p is None, we will find p.
    :param p0: Stagnation Pressure
    :param p: Static Pressure
    :param gamma: Ration of specific heats
    :param mach: Freestream mach number
    :return: the respective pressure
    """
    if p0 is None:
        return p * ((1 + ((gamma - 1) / 2) * mach ** 2) ** (gamma / (gamma - 1)))
    elif p is None:
        return p0 * ((1 + ((gamma - 1) / 2) * mach ** 2) ** -(gamma / (gamma - 1)))
    else:
        raise ValueError("Either P0 or P must be None.")


def press2temp(t0, t, p0, p, gamma=1.4):
    """
    This is the isentropic relation between pressure and temperature.
    We will find whichever parameter is None.
    :param t0: The stagnation temperature
    :param t: The static temperature
    :param p0: The stagnation pressure
    :param p: The static pressure
    :param gamma: The ratio of specific heats
    :return: the respective temperature
    """

    if p0 is None or p is None:
        raise ValueError("Pressure values cannot be None.")
    if t0 is None and t is None:
        raise ValueError("Only one parameter can be None.")

    if t0 is None:
        return t * ((p0 / p) ** ((gamma - 1) / gamma))
    elif t is None:
        return t0 * ((p / p0) ** ((gamma - 1) / gamma))
    else:
        raise ValueError("One parameter must be None.")


def temp2press(p0, p, t0, t, gamma=1.4):
    """
    This is the isentropic relation between pressure and temperature.
    We will find whichever parameter is None.
    :param t0: The stagnation temperature
    :param t: The static temperature
    :param p0: The stagnation pressure
    :param p: The static pressure
    :param gamma: The ratio of specific heats
    :return: the respective pressure
    """
    if t0 is None or t is None:
        raise ValueError("Temperature values cannot be None.")
    if p0 is None and p is None:
        raise ValueError("Only one parameter can be None.")

    if p0 is None:
        return p * ((t0 / t) ** (gamma / (gamma - 1)))
    elif p is None:
        return p0 * ((t / t0) ** (gamma / (gamma - 1)))
    else:
        raise ValueError("One parameter must be None.")

