from math import log10, floor, inf


def round_sig(i, sig=2):
    if i is not None:
        if i != inf:
            try:
                out = []
                if isinstance(i, list):
                    for x in i[::-1]:
                        out.append(round(x, sig-int(floor(log10(abs(x))))-1))
                else:
                    try:
                        out = round(i, sig-int(floor(log10(abs(i))))-1)
                    except TypeError:
                        out = i
            except ValueError:
                out = i
            return out
        else:
            return i
    else:
        return None
