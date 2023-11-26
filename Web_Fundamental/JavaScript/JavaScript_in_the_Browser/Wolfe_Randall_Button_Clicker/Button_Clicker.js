function logon(onOff) {
    if (onOff.innerText === "Login") {
        onOff.innerText = "Logout";
    } else {
        onOff.innerText = "Login";
    }
}
function gone(button) {
    button.remove();
}

