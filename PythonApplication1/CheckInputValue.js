function check() {
    var param = document.form1.param1.value;
    if (param == '') {
        alert("�l����͂��Ă��������B");
        return false;
    } else if (param.match(/[^0-9]+/)) {
        alert("�����݂̂���͂��Ă��������B");
        return false;
    }
    return true;
}

