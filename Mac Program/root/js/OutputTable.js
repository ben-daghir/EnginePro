function fillTable(data) {
    keys = Object.keys(data)
    for (var i = 0; i < keys.length; i++) {
        cell = document.getElementById(keys[i]);
        currVal = cell.innerHTML;

        color = compareValue(data[keys[i]], currVal, keys[i]);
        if (data[keys[i]] == null || data[keys[i]] == 0) {
            cell.innerHTML = "N/A";
        } else {
            cell.innerHTML = data[keys[i]];
        }
        cell.style.backgroundColor = color;
    }
}

const lessIsGood = ["out-tsfc", "out-wc", "out-wp", "out-wft","out-tsfc-c"]

function compareValue(newVal, oldVal, key) {
    try {
        newVal = parseFloat(newVal)
        oldVal = parseFloat(oldVal)
    } catch {
        return "black"
    }

    if (lessIsGood.includes(key)) {
        if (newVal > oldVal) {
            return "red"
        } else if (newVal < oldVal) {
            return "green"
        } else {
            return "white"
        }
    } else {
        if (newVal > oldVal) {
            return "green"
        } else if (newVal < oldVal) {
            return "red"
        } else {
            return "white"
        }
    }

}
