function insert(num) {
    document.form.textview.value = document.form.textview.value + num; 
}

function equal() {
    var e = document.form.textview.value;
    if (e) {
        document.form.textview.value = eval(e);
    }
}

function clean() {
    document.form.textview.value = "";
}

function back() {
    var e = document.form.textview.value;
    document.form.textview.value = e.substring(0,e.length-1);
}