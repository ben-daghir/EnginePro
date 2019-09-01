from EngineParts import Engine, Diffuser, Fan, Compressor, CombinedNozzle, Burner, Turbine, TurbineMixer, Nozzle, \
    NozzleMixer, Pump
import globals
from Utility import SciFi
import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
import http.server
import socketserver
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
import sys
import threading
import os
import webbrowser


def crossdomain(origin=None, methods=None, headers=None, max_age=21600,
                attach_to_all=True, automatic_options=True):
    """Decorator function that allows crossdomain requests.
      Courtesy of
      https://blog.skyred.fi/articles/better-crossdomain-snippet-for-flask.html
    """
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        """ Determines which methods are allowed
        """
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        """The decorator function
        """
        def wrapped_function(*args, **kwargs):
            """Caries out the actual cross domain code
            """
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


def add_part(part):
    part_type = part['name']
    if part_type == "Diffuser":
        #create
        globals.Engine.add_part(part_type,
            Diffuser.Diffuser(part["gamma"], globals.mach, part["efficiency"]))
    elif part_type == "Fan":
        #create
        globals.B = part['B']
        globals.Fan = Fan.Fan(part["mw"], part["gamma"], globals.mach, part["efficiency"],
                    part["pr"], part["B"], part["Cb"])
        globals.Engine.add_part(part_type, globals.Fan)
    elif part_type == "Compressor":
        # create
        globals.b = part["b"]
        globals.b_max = part["bmax"]
        globals.Compressor = Compressor.Compressor(part["mw"], part["gamma"], part["efficiency"], part["pr"])
        globals.Engine.add_part(part_type, globals.Compressor)
    elif part_type == "Main Burner":
        # create
        globals.f = part['f']
        globals.Qr = part['Q']
        globals.Engine.add_part(part_type,
            Burner.Burner(part["mw"], part["gamma"], globals.mach, part["efficiency"],
                          part["pr"], None, part["Q"], part["f"], globals.b))
    elif part_type == "Compressor Turbine":
        # create
        globals.tmax_turbine = part["t_max"]
        globals.Engine.add_part(part_type,
            Turbine.Turbine(part["mw"], part["gamma"], globals.mach, part["efficiency"], None, globals.b))
    elif part_type == "Turbine Mixer":
        # create
        globals.Engine.add_part(part_type,
            TurbineMixer.TurbineMixer(part["mw"], part["gamma"], globals.mach))
    elif part_type == "Fan Turbine":
        # create
        globals.Engine.add_part(part_type,
            Turbine.Turbine(part["mw"], part["gamma"], globals.mach, part["efficiency"], None, 0))
    elif part_type == "After Burner":
        # create
        globals.tmax_afterburner = part["t_max"]
        globals.fab = part['f']
        if part["f"] == 0:
            pr = 1
        else:
            pr = part["pr"]
        globals.Engine.add_part(part_type,
            Burner.Burner(part["mw"], part["gamma"], globals.mach, part["efficiency"],
                          pr, None, part["Q"], part["f"], -1 * globals.f))
    elif part_type == "Core Nozzle":
        # create
        globals.CoreNozzle = Nozzle.Nozzle(part["mw"], part["gamma"], globals.mach, part["efficiency"], globals.pa)
        globals.Engine.add_part(part_type, globals.CoreNozzle)
    elif part_type == "Fan Nozzle":
        # create
        globals.FanNozzle = Nozzle.Nozzle(part["mw"], part["gamma"], globals.mach, part["efficiency"], globals.pa)
        globals.Engine.add_part(part_type, globals.FanNozzle)
    elif part_type == "Nozzle Mixer":
        # create
        globals.Engine.add_part(part_type,
            NozzleMixer.NozzleMixer(part['prnm']))
    elif part_type == "Combined Nozzle":
        # create
        globals.CombinedNozzle = CombinedNozzle.CombinedNozzle(part['mw'], part['gamma'], part['efficiency'], globals.pa)
        globals.Engine.add_part(part_type, globals.CombinedNozzle)


def create_new_engine(parts):
    globals.Engine = Engine.Engine()
    for part in parts:
        add_part(part)


def create_environment(data):
    globals.mach = float(data['mach'])
    globals.pa = float(data['pa'])
    globals.ta = float(data['ta'])


def store_values(out, part_type):
    if part_type == "Diffuser":
        globals.p01 = out[0]
        globals.t01 = out[1]
    elif part_type == "Fan":
        globals.p02 = out[0]
        globals.t02 = out[1]
    elif part_type == "Compressor":
        globals.p03 = out[0]
        globals.t03 = out[1]
    elif part_type == "Main Burner":
        globals.p04 = out[0]
        globals.t04 = out[1]
    elif part_type == "Compressor Turbine":
        globals.p05_1 = out[0]
        globals.t05_1 = out[1]
    elif part_type == "Turbine Mixer":
        globals.p05_m = out[0]
        globals.t05_m = out[1]
    elif part_type == "Fan Turbine":
        globals.p05_2 = out[0]
        globals.t05_2 = out[1]
    elif part_type == "After Burner":
        globals.p06 = out[0]
        globals.t06 = out[1]
    elif part_type == "Core Nozzle":
        globals.pe = out[0]
        globals.te = out[1]
    elif part_type == "Fan Nozzle":
        globals.pef = out[0]
        globals.tef = out[1]
    elif part_type == "Nozzle Mixer":
        globals.p07 = out[0]
        globals.t07 = out[1]
    elif part_type == "Combined Nozzle":
        globals.pec= out[0]
        globals.tec = out[1]


def calculate_performance_metrics():

    globals.u = globals.mach * ((globals.gamma * (8314 / globals.mw) * globals.ta) ** 0.5)

    try:
        try:
            d = globals.Fan.Cb * (globals.mach ** 2) * (globals.pa / 101.3) * (globals.B ** 1.5)
        except:
            d = 0
        T_ma = (((1 + globals.f + globals.fab) * globals.ue) + (globals.B * globals.uef) - ((1 + globals.B) * globals.u))
        globals.T_m = T_ma / 1000 - d
    except:
        globals.T_m = None

    try:
        T_ma_c = (((1 + globals.f + globals.fab + globals.B) * globals.uec) - ((1 + globals.B) * globals.u))
        globals.T_m_c = T_ma_c / 1000 - d
    except:
        globals.T_m_c = None

    try:
        globals.TSFC = (globals.f + globals.fab) / globals.T_m
    except:
        globals.TSFC = None

    try:
        globals.TSFC_c = (globals.f + globals.fab) / globals.T_m_c
    except:
        globals.TSFC_c = None

    try:
        globals.n_th = 100 * ((1 + globals.f + globals.fab) * ((1183 ** 2) / 2) + globals.B * ((globals.uef ** 2) / 2)
                              - (1 + globals.B) * ((globals.u ** 2) / 2)) / ((globals.f + globals.fab) * globals.Qr)
    except:
        globals.n_th = None

    try:
        globals.n_o = 100 * globals.u / (globals.Qr * (globals.TSFC / 1000))
    except:
        globals.n_o = None

    try:
        globals.n_o_c = 100 * globals.u / (globals.Qr * (globals.TSFC_c / 1000))
    except:
        globals.n_o_c = None

    try:
        globals.wc = globals.Compressor.W_m / 1000
    except:
        globals.wc = None

    try:
        globals.wp = None
    except:
        globals.wp = None

    try:
        globals.wft = globals.Fan.W_m / 1000
    except:
        globals.wft = None

    try:
        globals.wp = Pump.compute_pump_work()
    except:
        globals.wp = None

    if not isinstance(globals.ue, float) or globals.ue <= 0:
        globals.ue = None

    if not isinstance(globals.uef, float) or globals.uef <= 0:
        globals.uef = None

    if not isinstance(globals.uec, float) or globals.uec <= 0:
       globals.uec = None

    if not isinstance(globals.T_m, float) or globals.T_m < 0:
        globals.T_m = None

    if not isinstance(globals.T_m_c, float) or globals.T_m_c < 0:
        globals.T_m_c = None

    if not isinstance(globals.TSFC, float) or globals.TSFC < 0:
        globals.TSFC = None

    if not isinstance(globals.TSFC_c, float) or globals.TSFC_c < 0:
        globals.TSFC_c = None

    if not isinstance(globals.n_o, float) or globals.n_o < 0:
        globals.n_o = None

    if not isinstance(globals.n_o_c, float) or globals.n_o_c < 0:
        globals.n_o_c = None


def format_output():
    sig_fig = 4
    print("*******************************************")
    print("Output")
    print("*******************************************")
    print("T01: " + str(SciFi.round_sig(globals.t01, sig_fig)) + " P01: " + str(SciFi.round_sig(globals.p01, sig_fig)))
    print("T02: " + str(SciFi.round_sig(globals.t02, sig_fig)) + " P02: " + str(SciFi.round_sig(globals.p02, sig_fig)))
    print("T03: " + str(SciFi.round_sig(globals.t03, sig_fig)) + " P03: " + str(SciFi.round_sig(globals.p03, sig_fig)))
    print("T04: " + str(SciFi.round_sig(globals.t04, sig_fig)) + " P04: " + str(SciFi.round_sig(globals.p04, sig_fig)))
    print("T05.1: " + str(SciFi.round_sig(globals.t05_1, sig_fig)) + " P05: " + str(
        SciFi.round_sig(globals.p05_1, sig_fig)))
    print("T05.m: " + str(SciFi.round_sig(globals.t05_m, sig_fig)) + " P05: " + str(
        SciFi.round_sig(globals.p05_m, sig_fig)))
    print("T05.2: " + str(SciFi.round_sig(globals.t05_2, sig_fig)) + " P05: " + str(
        SciFi.round_sig(globals.p05_2, sig_fig)))
    print("T06: " + str(SciFi.round_sig(globals.t06, sig_fig)) + " P06: " + str(SciFi.round_sig(globals.p06, sig_fig)))
    print("Te: " + str(SciFi.round_sig(globals.te, sig_fig)) + " Pe: " + str(SciFi.round_sig(globals.pe, sig_fig)))
    print("Tef: " + str(SciFi.round_sig(globals.tef, sig_fig)) + " Pef: " + str(SciFi.round_sig(globals.pef, sig_fig)))
    print("T07: " + str(SciFi.round_sig(globals.t07, sig_fig)) + " P07: " + str(SciFi.round_sig(globals.p07, sig_fig)))
    print("Tec: " + str(SciFi.round_sig(globals.tec, sig_fig)))
    print("ue: " + str(SciFi.round_sig(globals.ue, sig_fig)))
    print("uef: " + str(SciFi.round_sig(globals.uef, sig_fig)))
    print("T/m: " + str(SciFi.round_sig(globals.T_m, sig_fig)))
    print("TSFC: " + str(SciFi.round_sig(globals.TSFC, sig_fig)))
    print("n_th: " + str(SciFi.round_sig(globals.n_th, sig_fig)))
    print("n_o: " + str(SciFi.round_sig(globals.n_o, sig_fig)))
    print("wc: " + str(SciFi.round_sig(globals.wc, sig_fig)))
    print("wp: " + str(SciFi.round_sig(globals.wp, sig_fig)))
    print("wft: " + str(SciFi.round_sig(globals.wft, sig_fig)))
    print("fmax: " + str(SciFi.round_sig(globals.fmax, sig_fig)))
    print("fmax,ab: " + str(SciFi.round_sig(globals.fmax_ab, sig_fig)))

    print("uec: " + str(SciFi.round_sig(globals.uec, sig_fig)))
    print("T/m: " + str(SciFi.round_sig(globals.T_m_c, sig_fig)))
    print("TSFC: " + str(SciFi.round_sig(globals.TSFC_c, sig_fig)))
    print("n_o: " + str(SciFi.round_sig(globals.n_o_c, sig_fig)))

    print("*******************************************")

    output = {"out-t01": SciFi.round_sig(globals.t01, sig_fig),
             "out-p01": SciFi.round_sig(globals.p01, sig_fig),
             "out-t02": SciFi.round_sig(globals.t02, sig_fig),
             "out-p02": SciFi.round_sig(globals.p02, sig_fig),
             "out-t03": SciFi.round_sig(globals.t03, sig_fig),
             "out-p03": SciFi.round_sig(globals.p03, sig_fig),
             "out-t04": SciFi.round_sig(globals.t04, sig_fig),
             "out-p04": SciFi.round_sig(globals.p04, sig_fig),
             "out-t05-1": SciFi.round_sig(globals.t05_1, sig_fig),
             "out-p05-1": SciFi.round_sig(globals.p05_1, sig_fig),
             "out-t05-m": SciFi.round_sig(globals.t05_m, sig_fig),
             "out-p05-m": SciFi.round_sig(globals.p05_m, sig_fig),
             "out-t05-2": SciFi.round_sig(globals.t05_2, sig_fig),
             "out-p05-2": SciFi.round_sig(globals.p05_2, sig_fig),
             "out-t06": SciFi.round_sig(globals.t06, sig_fig),
             "out-p06": SciFi.round_sig(globals.p06, sig_fig),
             "out-te": SciFi.round_sig(globals.te, sig_fig),
             "out-pe": SciFi.round_sig(globals.pe, sig_fig),
             "out-tef": SciFi.round_sig(globals.tef, sig_fig),
             "out-pef": SciFi.round_sig(globals.pef, sig_fig),
             "out-t07": SciFi.round_sig(globals.t07, sig_fig),
             "out-gamma-nm": SciFi.round_sig(globals.gamma_nm, sig_fig),
             "out-p07": SciFi.round_sig(globals.p07, sig_fig),
             "out-tec": SciFi.round_sig(globals.tec, sig_fig),
             "out-ue": SciFi.round_sig(globals.ue, sig_fig),
             "out-uef": SciFi.round_sig(globals.uef, sig_fig),
             "out-t-ma": SciFi.round_sig(globals.T_m, sig_fig),
             "out-tsfc": SciFi.round_sig(globals.TSFC, sig_fig),
             "out-nth": SciFi.round_sig(globals.n_th, sig_fig),
             "out-n0": SciFi.round_sig(globals.n_o, sig_fig),
             "out-wc": SciFi.round_sig(globals.wc, sig_fig),
             "out-wp": SciFi.round_sig(globals.wp, sig_fig),
             "out-wft": SciFi.round_sig(globals.wft, sig_fig),
             "out-fmax": SciFi.round_sig(globals.fmax, sig_fig),
             "out-fmax,ab": SciFi.round_sig(globals.fmax_ab, sig_fig),
             "out-uec": SciFi.round_sig(globals.uec, sig_fig),
             "out-t-ma-c": SciFi.round_sig(globals.T_m_c, sig_fig),
             "out-tsfc-c": SciFi.round_sig(globals.TSFC_c, sig_fig),
             "out-n0-c": SciFi.round_sig(globals.n_o_c, sig_fig),
             "out-t-ma-max": None,
             "out-t-ma-c-max": None}

    return output



def run_analysis():
    engine = globals.Engine.parts
    globals.p0in = globals.pa
    globals.t0in = globals.ta
    has_ab = False;
    for item in engine:
        name = item[0]
        part = item[1]
        if isinstance(part, Turbine.Turbine):
            if name == "Fan Turbine":
                out = part.compute_outlet(globals.p0in, globals.t0in, globals.Fan.W_m)
            elif name == "Compressor Turbine":
                out = part.compute_outlet(globals.p0in, globals.t0in, globals.Compressor.W_m)
        elif name == "Turbine Mixer":
            out = part.compute_outlet(globals.p0in, globals.t0in, globals.Compressor)
        elif name == "Nozzle Mixer":
            out = part.compute_outlet(globals.t02, globals.t0in, globals.p02, globals.p0in)
        elif name == "Fan Nozzle":
            out = part.compute_outlet(globals.p02, globals.t02)
            globals.uef = out[2]
        elif name == "Core Nozzle":
            out = part.compute_outlet(globals.p0in, globals.t0in)
            globals.ue = out[2]
        elif name == "Main Burner":
            tmax = globals.tmax_turbine
            if globals.b != 0:
                tmax = globals.tmax_turbine + globals.Cb1 * ((globals.b / globals.b_max) ** 0.5)
            out = part.compute_outlet(globals.p0in, globals.t0in, tmax, globals.b, globals.f)
            globals.fmax = out[2]
            globals.f = part.f
        elif name == "After Burner":
            out = part.compute_outlet(globals.p0in, globals.t0in, globals.tmax_afterburner, -1 * globals.f, globals.fab)
            globals.fmax_ab = out[2]
            globals.fab = part.f
            has_ab = True
        else:
            out = part.compute_outlet(globals.p0in, globals.t0in)

        globals.p0in = out[0]
        globals.t0in = out[1]
        store_values(out, name)

    if not has_ab:
        globals.fab = 0

    calculate_performance_metrics()
    return format_output()



app = Flask(__name__)
cors = CORS(app, resources={r"/run_analysis": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/run_analysis', methods=["POST", "OPTIONS"])
@crossdomain(origin='*')
def new_engine():
    globals.reset()
    data = request.data
    data = json.loads(data)
    for i in range(0, len(data['engine'])):
        for k, v in data['engine'][i].items():
            if k != 'name' and k != 'id':
                if isinstance(v, list):
                    data['engine'][i][k] = [float(v[0]), v[1]]
                else:
                    try:
                        data['engine'][i][k] = float(v)
                    except ValueError:
                        raise ValueError("Engine parameter, " + str(k) + ", inputted incorrectly.")
    print(data)
    create_environment(data)
    create_new_engine(data["engine"])
    output = run_analysis()

    globals.reset()
    for i in range(0, len(data['engine'])):
        for k, v in data['engine'][i].items():
            if k != 'name' and k != 'id':
                if data['engine'][i]["name"] == "After Burner":
                    data['engine'][i]["f"] = 999
                elif data['engine'][i]["name"] == "Compressor":
                    data['engine'][i]["b"] = 0.12
                elif data['engine'][i]["name"] == "Main Burner":
                    data['engine'][i]["f"] = 99
    create_environment(data)
    create_new_engine(data["engine"])
    max_out = run_analysis()
    output["out-t-ma-max"] = max_out["out-t-ma"]
    output["out-t-ma-c-max"] = max_out["out-t-ma-c"]
    return json.dumps(output)


FLASKPORT = 8080
HTTPPORT = 3000


def run_backend():
    print("Backend serving on port 8888")
    app.run("", FLASKPORT)


def setup_program():
    th = threading.Thread(target=run_backend)
    th.daemon = True

    web_dir = os.path.join(os.path.dirname(sys.executable), 'root')
    print(web_dir)
    os.chdir(web_dir)

    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", HTTPPORT), handler)
    print("Running EnginePro on port", HTTPPORT)
    th.start()
    webbrowser.open_new("htt"+"p://"+"localhos"+"t:3000")
    httpd.serve_forever()

setup_program()