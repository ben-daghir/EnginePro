var Engine = [];
var Ids = [];

var Pa = 0;
var Ta = 0;
var Mach = 0;
var Ind = -1;
var ChangedPart = null;

var engineArea = document.getElementById("engine-area");
var createButton = document.getElementById("create-button");

function size(arr) {
    count = 0;
    for (var i = 0; i < arr.length; i++) {
        arr[i]
        count = count + 1;
    }
    return count;
}

var timeout = 2000
function createNewEngine(type) {
    Pa = $("#pa").val();
    Ta = $("#ta").val();
    Mach = $("#mach").val();
    modal1.style.display = "none";
    console.log("new engine...");
    createButton.style.height = "0px";
    createButton.style.width = "0px";
    createButton.innerHTML = "";
    setTimeout(function()
    {createButton.parentNode.removeChild(createButton)}, 500);
    setTimeout(function() {
        document.getElementById("addComponentButton").style.display = "inline";
        document.getElementById("runAnalysisButton").style.display = "inline";
        document.getElementById("clearEngine").style.display = "inline";
        document.getElementById("mach").style.display = "inline";
        document.getElementById("ta").style.display = "inline";
        document.getElementById("pa").style.display = "inline";
        document.getElementById("mach2").style.display = "inline";
        document.getElementById("ta2").style.display = "inline";
        document.getElementById("pa2").style.display = "inline";

    }, 1500)
    engineArea.style.height = '400px';
    setTimeout(function() {
        if (type == "everything") {
            quickConfig(EVERTHING);
        } else if (type == "turbofan") {
            quickConfig(TURBOFAN);
        } else if (type == "turbojet") {
            quickConfig(TURBOJET);
        } else if (type == "ramjet") {
            quickConfig(RAMJET);
        }
    }, timeout)
    timeout = 0
}

function updateNewPart(part) {
    var e = document.getElementById(part['id']);
    str = part['name'];
    e.childNodes[0].nodeValue = str;
    modal2.style.display = "None";
}

function rebuildEngine() {
    document.getElementById('parts-area').innerHTML = ""
    wrappedRebuildEngine(0)
}

function wrappedRebuildEngine(i) {
    if (i == Engine.length) {
        return;
    }
    part = Engine[i]
    str = part['name'];
    var newNode = document.createElement("div")
    newNode.classList.add("enginepart");
    newNode.innerHTML = str;
    newNode.id = part['id'];
    var br = document.createElement('br');
    var deleteButton = document.createElement('button');
    deleteButton.innerHTML = "Delete";
    deleteButton.id = part['id'] + '-delete'
    var editButton = document.createElement('button');
    editButton.innerHTML = "Edit";
    editButton.id = part['id'] + '-edit'
    newNode.appendChild(document.createElement('div'))
    newNode.appendChild(br)
    newNode.appendChild(editButton)
    newNode.appendChild(br)
    newNode.appendChild(deleteButton);
    document.getElementById('parts-area').appendChild(newNode);
    modal2.style.display = "None";
    var id = part['id'].split('-');
    var id = id[id.length - 1];
    $("#" + part['id'] + '-edit').click(function() {
        editComponent(id);
    });
    $("#" + part['id'] + '-delete').click(function() {
        deleteComponent(id);
    });
    wrappedRebuildEngine(i + 1);
}

function editComponent(id) {
    modal2.style.display = "Block";
    part = Engine[id];
    var val = part['name'];
    document.getElementById(val).selected = true;
    updateConfigOptions();
    keys = Object.keys(part);
    console.log(keys);
    for (var i = 0; i < keys.length; i++) {
        var e = document.getElementById(keys[i]);
        if (e != null) {
            if (keys[i] == 'efficiency' && Array.isArray(part[keys[i]])) {
                e.value = part[keys[i]][0];
            } else {
                e.value = part[keys[i]];
            }
        }
    }
    var button = document.getElementById('submit-button');
    Ind = id;
    ChangedPart = part;
    button.innerHTML = "Update Component"
}

/**
 * Deletes a component
 * @param  {event} event the triggered event
 * @return {none}       none
 */
function deleteComponent(id) {
    id = parseInt(id);
    newEngine = []
    newIds = []
    for (var j = 0; j < id; j++) {
        newEngine.push(Engine[j])
        newIds.push(Ids[j])
    }
    for (var i = id + 1; i < Engine.length; i++) {
        newEngine.push(Engine[i]);
        newIds.push(Ids[i])
        id_split = Engine[i]['id'].split('-');
        num = parseInt(id_split[id_split.length - 1]) - 1;
        new_id = ""
        for (var j = 0; j < id_split.length - 1; j++) {
            if (j != 0) {
                new_id = new_id + '-' + id_split[j]
            } else {
                new_id = new_id + id_split[j]
            }
        }
        new_id = new_id + "-" + num;
        document.getElementById(Engine[i]['id']).id = new_id
        newIds[i - 1] = new_id;
        newEngine[i - 1]['id'] = new_id;
    }
    Engine = newEngine;
    Ids = newIds;
    console.log("Deleted. New Engine...");
    console.log(Engine);
    console.log(Ids);
    rebuildEngine();

}

function addComponent(value=null) {
    if (Ind == -1) {
        id = Engine.length;
        console.log(id);
    } else {
        id = Ind;
    }
    try {
        ifPoly = document.querySelector('input[id="poly"]:checked').checked;
        console.log(ifPoly);
    } catch {
        ifPoly = true;
    }
    if (value == null) {
        var e = document.getElementById("choose-component");
        var value = e.options[e.selectedIndex].text;
    }
    console.log(value);
    if (value == "Diffuser") {
        part = {"name": "Diffuser",
                "id": ("diffuser-" + id),
                "mw": $("#mw").val(),
                "gamma": $("#gamma").val(),
                "efficiency": $("#efficiency").val()}
    } else if (value == "Fan") {
        if (ifPoly) {
            poly = true;
        } else {
            poly = false;
        }
        part = {"name": "Fan",
                "id": ("fan-" + id),
                "mw": $("#mw").val(),
                "gamma": $("#gamma").val(),
                "efficiency": [$("#efficiency").val(), poly],
                "pr": $("#pr").val(),
                "B": $("#B").val(),
                "Cb": $("#Cb").val()}

    } else if (value == "Compressor") {
        if (ifPoly) {
            poly = true;
        } else {
            poly = false;
        }
        part = {"name": "Compressor",
                "id": ("compressor-" + id),
                "mw": $("#mw").val(),
                "gamma": $("#gamma").val(),
                "efficiency": [$("#efficiency").val(), poly],
                "pr": $("#pr").val(),
                "b": $("#b").val(),
                "bmax": $("#bmax").val()}
    } else if (value == "Main Burner") {
        part = {"name": "Main Burner",
                "id": ("burner-" + id),
                "mw": $("#mw").val(),
                "gamma": $("#gamma").val(),
                "efficiency": $("#efficiency").val(),
                "pr": $("#pr").val(),
                "Q": $("#Q").val(),
                "f": $("#f").val()}
    } else if (value == "Compressor Turbine") {
        if (ifPoly) {
            poly = true;
        } else {
            poly = false;
        }
        part = {"name": "Compressor Turbine",
                "id": ("turbine-" + id),
                "mw": $("#mw").val(),
                "gamma": $("#gamma").val(),
                "efficiency": [$("#efficiency").val(), poly],
                "pr": $("#pr").val(),
                "Cbl": $("#Cbl").val(),
                "t_max": $("#t_max").val()}
    } else if (value == "Turbine Mixer") {
        part = {"name": "Turbine Mixer",
                "id": ("turbine_mixer-" + id),
                "mw": $("#mw").val(),
                "gamma": $("#gamma").val()}
    } else if (value == "Fan Turbine") {
        if (ifPoly) {
            poly = true;
        } else {
            poly = false;
        }
        part = {"name": "Fan Turbine",
                "id": ("turbine-" + id),
                "mw": $("#mw").val(),
                "gamma": $("#gamma").val(),
                "efficiency": [$("#efficiency").val(), poly]}
    } else if (value == "After Burner") {
        part = {"name": "After Burner",
                "id": ("burner-" + id),
                "mw": $("#mw").val(),
                "gamma": $("#gamma").val(),
                "efficiency": $("#efficiency").val(),
                "pr": $("#pr").val(),
                "Q": $("#Q").val(),
                "t_max": $("#t_max").val(),
                "f": $("#f").val()}
    } else if (value == "Core Nozzle") {
        part = {"name": "Core Nozzle",
                "id": ("nozzle-" + id),
                "mw": $("#mw").val(),
                "gamma": $("#gamma").val(),
                "efficiency": $("#efficiency").val()}
    } else if (value == "Fan Nozzle") {
        part = {"name": "Fan Nozzle",
                "id": ("nozzle-" + id),
                "mw": $("#mw").val(),
                "gamma": $("#gamma").val(),
                "efficiency": $("#efficiency").val()}
    } else if (value == "Nozzle Mixer") {
        part = {"name": "Nozzle Mixer",
                "id": ("nozzle_mixer-" + id),
                "prnm": $("#prnm").val()}
    }  else if (value == "Combined Nozzle") {
        part = {"name": "Combined Nozzle",
                "id": ("combined_nozzle-" + id),
                "mw": $("#mw").val(),
                "gamma": $("#gamma").val(),
                "efficiency": $("#efficiency").val()}
    }
    if (Ind==-1) {
        Engine.push(part);
        Ids.push(part['id'] + "")
        rebuildEngine();
    } else {
        Engine[Ind] = part;
        _id = part['id'].split('-');
        _id = _id[_id.length - 1];
        Ids[_id] = part['id']
        document.getElementById(ChangedPart['id']).id = part['id']
        updateNewPart(part);
    }
    Ind = -1;
}

// Button
var addComponentButton = document.getElementById("addComponentButton")
// Get the modal
var modal2 = document.getElementById('addComponentModal');
// Get the <span> element that closes the modal
var close2 = document.getElementsByClassName("close2")[0];
// When the user clicks on the button, open the modal
addComponentButton.onclick = function() {
    modal2.style.display = "block";
    var button = document.getElementById('submit-button');
    button.innerHTML = "Create Component";
}
// When the user clicks on <span> (x), close the modal
close2.onclick = function() {
    modal2.style.display = "none";
}

function reselectEngine() {
    modal1.style.display = "block";
    document.getElementById("parts-area").innerHTML = ""
    Engine = [];
    Ids = [];
    Pa = 0;
    Ta = 0;
    Mach = 0;
    Ind = -1;
    ChangedPart = null;
}


// Get the modal
var modal1 = document.getElementById('myModal');
// Get the <span> element that closes the modal
var close1 = document.getElementsByClassName("close")[0];
// When the user clicks on the button, open the modal
createButton.onclick = function() {
    modal1.style.display = "block";
}
// When the user clicks on <span> (x), close the modal
close1.onclick = function() {
    modal1.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal1) {
        modal1.style.display = "none";
    } else if (event.target == modal2) {
        modal2.style.display = "none";
    }
}
