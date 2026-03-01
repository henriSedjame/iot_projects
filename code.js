
function showCode() {
    let codeElement = document.getElementById('python_code');

    codeElement.classList.add('cm-s-default');
    let code = codeElement.innerText;

    codeElement.innerHTML = "";

    CodeMirror.runMode(
        code,
        'python',
        codeElement
    );
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
    showCode();
});

hideCodeBtn.addEventListener('click', function () {
    codeFinal.style.display = "none";
    showCodeBtn.style.display = "block";
    hideCodeBtn.style.display = "none"
})
