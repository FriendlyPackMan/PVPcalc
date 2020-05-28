var checked = "";
var player = "green";

function play_green(id) {
    nick = document.getElementById("nickview").value;
    document.location.href = "game/" + id + "/" + nick;
    // player = "green";
    // checked = [];
}

function check(answer, id) {
    attemp = document.form.textview.value;
    if (checked.includes(id)) {
        return;
    }
    if (attemp == answer) {
        checked += id;
        if (player == "green") {
            val = document.getElementById("scores-red").innerHTML;
            document.getElementById("scores-red").innerHTML = val - 1;
        }
        else {
            val = document.getElementById("scores-green").innerHTML;
            document.getElementById("scores-green").innerHTML = val - 1;
        }
        document.getElementById("task-butt-"+id).innerHTML = "Solved";
        document.getElementById("task-butt-"+id).style.background = "#6e6e6e";
    }
    else {
        document.getElementById("task-butt-"+id).innerHTML = "Again";
    }
}