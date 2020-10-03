function check() {
    var param = document.form1.param1.value;
    if (param == '') {
        alert("’l‚ğ“ü—Í‚µ‚Ä‚­‚¾‚³‚¢B");
        return false;
    } else if (param.match(/[^0-9]+/)) {
        alert("”š‚Ì‚İ‚ğ“ü—Í‚µ‚Ä‚­‚¾‚³‚¢B");
        return false;
    }
    return true;
}

