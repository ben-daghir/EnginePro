Engine = None

# Important Components
Fan = None
Compressor = None
CoreNozzle = None
FanNozzle = None
CombinedNozzle = None

# System Parameters
gamma = 1.4
mw = 28.8
mach = 0
u = 0
pa = 0
ta = 0
f = 0
f_main = 0
f_ab = 0
fab = 0
B = 0
b = 0
b_max = 0
Qr = 45e6
Cb1 = 700
tmax_turbine = 1300
tmax_afterburner = 2200

# Calculated Outputs
p0in = None
t0in = None

p01 = None
p02 = None
p03 = None
p04 = None
p05_1 = None
p05_m = None
p05_2 = None
p06 = None
pe = None
pef = None
p07 = None
pec = None

t01 = None
t02 = None
t03 = None
t04 = None
t05_1 = None
t05_m = None
t05_2 = None
t06 = None
te = None
tef = None
t07 = None
tec = None

gamma_nm = 0


# Performance Metrics
ue = 0
uef = 0
u = 0
T_m = 0
TSFC = 0
n_th = 0
n_o = 0
wc = 0
wp = 0
wft = 0
fmax = 0
fmax_ab = 0

uec = 0
T_m_c = 0
TSFC_c = 0
n_o_c = 0


def reset():
    global mach
    global pa
    global ta
    global Engine
    global p0in
    global t0in
    global p01
    global p02
    global p03
    global p04
    global p05_1
    global p05_m
    global p05_2
    global p06
    global pe
    global pef
    global p07
    global pec
    global t01
    global t02
    global t03
    global t04
    global t05_1
    global t05_m
    global t05_2
    global t06
    global te
    global tef
    global t07
    global tec
    global gamma_nm
    global ue
    global uef
    global u
    global T_m
    global TSFC
    global n_th
    global n_o
    global wc
    global wp
    global wft
    global fmax
    global fmax_ab
    global uec
    global T_m_c
    global TSFC_c
    global n_o_c
    global Fan
    global Compressor
    global CoreNozzle
    global FanNozzle
    global CombinedNozzle
    global gamma
    global mw
    global f
    global fab
    global B
    global b
    global Qr
    global t01
    global t07
    global p07
    global u
    global tmax_turbine
    global tmax_afterburner
    global Cb1
    global b_max
    global f_main
    global f_ab

    Engine = None

    # Important Components
    Fan = None
    Compressor = None
    CoreNozzle = None
    FanNozzle = None
    CombinedNozzle = None

    # System Parameters
    gamma = 1.4
    mw = 28.8
    mach = 0
    u = 0
    pa = 0
    ta = 0
    f_main = 0
    f_ab = 0
    f = 0
    fab = 0
    B = 0
    b = 0
    b_max = 0
    Qr = 45e6
    Cb1 = 700
    tmax_turbine = 1300
    tmax_afterburner = 2200

    # Calculated Outputs

    p0in = None
    t0in = None

    p01 = None
    p02 = None
    p03 = None
    p04 = None
    p05_1 = None
    p05_m = None
    p05_2 = None
    p06 = None
    pe = None
    pef = None
    p07 = None
    pec = None

    t01 = None
    t02 = None
    t03 = None
    t04 = None
    t05_1 = None
    t05_m = None
    t05_2 = None
    t06 = None
    te = None
    tef = None
    t07 = None
    tec = None

    gamma_nm = None

    # Performance Metrics
    ue = 0
    uef = 0
    u = 0
    T_m = 0
    TSFC = 0
    n_th = 0
    n_o = 0
    wc = 0
    wp = 0
    wft = 0
    fmax = 0
    fmax_ab = 0

    uec = 0
    T_m_c = 0
    TSFC_c = 0
    n_o_c = 0
