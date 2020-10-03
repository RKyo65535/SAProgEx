function check() {
    var param = document.form1.param1.value;
    if (param == '') {
        alert("値を入力してください。");
        return false;
    } else if (param.match(/[^0-9]+/)) {
        alert("数字のみを入力してください。");
        return false;
    }
    return true;
}
