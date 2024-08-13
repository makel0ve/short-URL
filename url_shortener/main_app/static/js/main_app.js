function hidden_input() {
    let input = document.getElementById("short_url_input");
    let div = document.getElementById("short_url");
    let div_2 = document.getElementById("short_url_copy_button");
    let copy_button = document.getElementById("copy_button");
    if (input.textContent == "") {
        div.hidden = true;
        div_2.hidden = true;
        copy_button.hidden = true;
    } else {
        div.hidden = false;
        div_2.hidden = false;
        copy_button.hidden = false;
    }
}

function click_url() {
    let span = document.getElementById("short_url_input").innerHTML;
    navigator.clipboard.writeText(span).then(function () {
        let button = document.getElementById("copy_button");
        var message = document.getElementById("copyMessage");
        // var rect = button.getBoundingClientRect();
        // message.style.top = rect.bottom + window.scrollY + "px";
        // message.style.left = rect.left + "px";
        message.style.visibility = "visible";

        setTimeout(function () {
            message.style.visibility = "hidden";
        }, 3000);
    });
}

hidden_input();
