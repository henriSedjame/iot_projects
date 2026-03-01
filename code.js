function showCode() {
    let codeElements = document.getElementsByClassName('python_code');

    for (let codeElement of codeElements) {
        codeElement.classList.add('cm-s-default');
        let code = codeElement.innerText;

        codeElement.innerHTML = "";

        CodeMirror.runMode(
            code,
            'python',
            codeElement
        );
    }

}

let codeFinal = document.getElementById('code_final');
let showCodeBtn = document.getElementById('show_code');
let hideCodeBtn = document.getElementById('hide_code');

codeFinal.style.display = "none";
hideCodeBtn.style.display = "none";

showCodeBtn.addEventListener('click', function () {
    codeFinal.style.display = "block";
    hideCodeBtn.style.display = "block";
    showCodeBtn.style.display = "none";
    document.getElementById('main').style.display = "block";
    document.getElementById('main-tab').classList.add('active');
    showCode();
});

hideCodeBtn.addEventListener('click', function () {
    codeFinal.style.display = "none";
    showCodeBtn.style.display = "block";
    hideCodeBtn.style.display = "none"
})


function showTab(name, tabs) {
    for (let tab of tabs) {
        if (tab === name) {
            document.getElementById(`${name}-tab`).classList.add('active');
            document.getElementById(name).style.display = "block";
        } else {
            document.getElementById(`${tab}-tab`).classList.remove('active');
            document.getElementById(tab).style.display = "none";
        }

    }

}