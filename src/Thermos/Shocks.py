def diffuser_shock_loss(mach):
    """
    This method takes into account aerodynamic losses
    due to shock formations.
    :param mach: The freestream mach number
    :return: the percentage loss
    """
    if 0 <= mach < 1:
        return 1
    elif mach >= 1:
        return 1 - 0.075 * ((mach - 1) ** 1.35)
    else:
        raise ValueError("Cannot travel at a Mach < 0.")

