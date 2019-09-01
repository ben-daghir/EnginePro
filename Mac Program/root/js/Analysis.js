function postAnalysis() {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'htt' + 'p://localho' + 'st:8080/run_analysis', true);

    //Send the proper header information along with the request
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    xhr.onreadystatechange = function() { // Call a function when the state changes.
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            fillTable(JSON.parse(xhr.responseText))
        }
    }
    mach = document.getElementById("mach").value;
    ta = document.getElementById("ta").value;
    pa = document.getElementById("pa").value;
    output = {"engine": Engine, "mach": mach, "ta": ta, "pa": pa};
    xhr.send(JSON.stringify(output));
}
