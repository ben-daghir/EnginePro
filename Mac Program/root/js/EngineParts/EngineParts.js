function diffuserConfig(mw=28.8, gamma=1.4, ad_e=0.92) {
    str = '<div>Molecular Weight</div>'
    + '<input style="width:100px" type="number" step="0.1" value='+mw+' id="mw"><br>'
    + '<div>Gamma</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+gamma+' id="gamma"><br>'
    + '<div>Efficiency</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+ad_e+' id="efficiency">'
    return str;
}

function fanConfig(mw=28.8, gamma=1.4, e=0.9, pl=true, ad=false, pr=1.2, by=2, cd=0.245) {
    str = '<div>Molecular Weight</div>'
    + '<input style="width:100px" type="number" step="0.1" value='+mw+' id="mw"><br>'
    + '<div>Gamma</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+gamma+' id="gamma"><br>'
    + '<div>Efficiency</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+e+' id="efficiency"><br>'
    + '<fieldset id=poly>'
    + '<input type="radio" checked=true name="efficiency">Polytropic</input>'
    + '<input type="radio"  name="efficiency">Adiabtaic</input><br>'
    + '</fieldset>'
    + '<div>Pressure Ratio</div>'
    + '<input style="width:100px" type="number" value='+pr+' id="pr"><br>'
    + '<div>Bypass Ratio</div>'
    + '<input style="width:100px" type="number" value='+by+' id="B"><br>'
    + '<div>Drag Coefficient</div>'
    + '<input style="width:100px" type="number" value='+cd+' id="Cb"><br>'
    return str;
}

function compressorConfig(mw=28.8, gamma=1.38, e=0.9, pl=true, ad=false, pr=30,
    b=0.1, bmax=0.12) {
    str = '<div class="configurelabels">Molecular Weight</div>'
    + '<input style="width:100px" type="number" step="0.1" value='+mw+' id="mw"><br>'
    + '<div class="configurelabels">Gamma</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+gamma+' id="gamma"><br>'
    + '<div class="configurelabels">Efficiency</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+e+' id="efficiency"><br>'
    + '<fieldset id=poly>'
    + '<input type="radio" checked=true name="efficiency">Polytropic</input>'
    + '<input type="radio" name="efficiency">Adiabtaic</input><br>'
    + '</fieldset>'
    + '<div>Bleed Air</div>'
    + '<input style="width:100px" type="number" step="0.001" value='+b+' id="b"><br>'
    + '<div>Max Bleed Air</div>'
    + '<input style="width:100px" type="number" step="0.001" value='+bmax+' id="bmax"><br>'
    + '<div class="configurelabels">Pressure Ratio</div>'
    + '<input style="width:100px" type="number" value='+pr+' id="pr"><br>'
    return str;
}

function burnerConfig(t_max=2200, f=0.018, ad_e=0.99, pr=0.98,  gamma=1.33, mw=28.8, q=45000000) {
         str = '<div>Molecular Weight</div>'
    + '<input style="width:100px" type="number" step="0.1" value='+mw+' id="mw"><br>'
    + '<div>Gamma</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+gamma+' id="gamma"><br>'
    + '<div>Adiabatic Efficiency</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+ad_e+' id="efficiency"><br>'
    + '<div>Pressure Ratio</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+pr+' id="pr"><br>'
    + '<div>Max Temperature (K)</div>'
    + '<input style="width:100px" type="number" step="10" value='+t_max+' id="t_max"><br>'
    + '<div>Heating Value</div>'
    + '<input style="width:100px" type="number" step="100000" value='+q+' id="Q"><br>'
    + '<div>Fuel to Air Ratio</div>'
    + '<input style="width:100px" type="number" step="0.0001" value='+f+' id="f"><br>'
    return str;
}

function compressorTurbineConfig(mw=28.8, gamma=1.33, e=0.92, pl=true, ad=false,
     f=0.018, t_max=1300, cb=700) {
    str = '<div>Molecular Weight</div>'
    + '<input style="width:100px" type="number" step="0.1" value='+mw+' id="mw"><br>'
    + '<div>Gamma</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+gamma+' id="gamma"><br>'
    + '<div>Efficiency</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+e+' id="efficiency"><br>'
    + '<fieldset id=poly>'
    + '<input type="radio" checked=true name="efficiency">Polytropic</input>'
    + '<input type="radio" name="efficiency">Adiabtaic</input><br>'
    + '</fieldset>'
    + '<div>Max Temperature (K)</div>'
    + '<input style="width:100px" type="number" step="10" value='+t_max+' id="t_max"><br>'
    + '<div>Coefficient of Bleed, Cbl (K)</div>'
    + '<input style="width:100px" type="number" step="10" value='+cb+' id="Cbl"><br>'
    return str;
}

function turbineMixerConfig(mw=28.8, gamma=1.34) {
    str = '<div>Molecular Weight</div>'
    + '<input style="width:100px" type="number" step="0.1" value='+mw+' id="mw"><br>'
    + '<div>Gamma</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+gamma+' id="gamma"><br>'
    return str;
}

function fanTurbineConfig(mw=28.8, gamma=1.33, e=0.92) {
    str = '<div>Molecular Weight</div>'
    + '<input style="width:100px" type="number" step="0.1" value='+mw+' id="mw"><br>'
    + '<div>Gamma</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+gamma+' id="gamma"><br>'
    + '<div>Efficiency</div>'
    + '<input style="width:100px" type="number" step="0.01" value='+e+' id="efficiency"><br>'
    + '<fieldset id=poly>'
    + '<input type="radio" checked=true name="efficiency">Polytropic</input>'
    + '<input type="radio" name="efficiency">Adiabtaic</input><br>'
    + '</fieldset>'
    return str;
}

function nozzleConfig(gamma=1.4, ad_e=0.95, mw=28.8) {
    str = '<div>Molecular Weight</div>'
    + '<input style="width:100px" type="number" step="0.1" value=' + mw + ' id="mw"><br>'
    + '<div>Gamma</div>'
    + '<input style="width:100px" type="number" step="0.01" value=' + gamma + ' id="gamma"><br>'
    + '<div>Efficiency</div>'
    + '<input style="width:100px" type="number" step="0.01" value=' + ad_e+' id="efficiency">'
    return str
}

function nozzleMixerConfig(prnm=0.80) {
    str = '<div>Effective Pressure Loss, (Prnm)</div>'
    + '<input style="width:100px" type="number" step="0.01" value=' + prnm + ' id="prnm"><br>'
    return str
}

const EVERTHING = ["Diffuser", "Fan", "Compressor", "Main Burner", "Compressor Turbine",
                    "Turbine Mixer", "Fan Turbine", "After Burner", "Core Nozzle",
                    "Fan Nozzle", "Nozzle Mixer", "Combined Nozzle"]

const TURBOFAN = ["Diffuser", "Fan", "Compressor", "Main Burner", "Compressor Turbine",
                    "Turbine Mixer", "Fan Turbine", "Core Nozzle", "Fan Nozzle"]

const TURBOJET = ["Diffuser", "Compressor", "Main Burner", "Compressor Turbine",
                    "Turbine Mixer", "After Burner", "Core Nozzle"]

const RAMJET = ["Diffuser", "Compressor", "Main Burner", "Core Nozzle"]

function quickConfig(items) {
    modal2.style.display = "block";
    for (var i = 0; i < items.length; i++) {
        updateConfigOptions(items[i]);
        addComponent(items[i]);
    }
}

function updateConfigOptions(value=null) {
    if (value == null) {
        var e = document.getElementById("choose-component");
        var value = e.options[e.selectedIndex].text;
    }
    if (value == "Diffuser") {
        $("#part-parameters").html(diffuserConfig());
    } else if (value == "Fan") {
        $("#part-parameters").html(fanConfig());
    } else if (value == "Compressor") {
        $("#part-parameters").html(compressorConfig());
    } else if (value == "Main Burner") {
        $("#part-parameters").html(burnerConfig());
    } else if (value == "Compressor Turbine") {
        $("#part-parameters").html(compressorTurbineConfig());
    } else if (value == "Turbine Mixer") {
        $("#part-parameters").html(turbineMixerConfig());
    } else if (value == "Fan Turbine") {
        $("#part-parameters").html(fanTurbineConfig());
    } else if (value == "After Burner") {
        $("#part-parameters").html(burnerConfig(t_max=2200, f=0.01, ad_e=.96, pr=.97, gamma=1.32));
    } else if (value == "Core Nozzle") {
        $("#part-parameters").html(nozzleConfig(gamma=1.35, ad_e=0.95));
    } else if (value == "Fan Nozzle") {
        $("#part-parameters").html(nozzleConfig(gamma=1.4, ad_e=0.97));
    } else if (value == "Nozzle Mixer") {
        $("#part-parameters").html(nozzleMixerConfig());
    }  else if (value == "Combined Nozzle") {
        $("#part-parameters").html(nozzleConfig(gamma=1.37, ad_e=0.95));
    }
}


$("#choose-component").change(function() {
    updateConfigOptions();
});
