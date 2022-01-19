console.log('Hello World')
//
// const copyBtns = [...document.getElementsByClassName('copy-btn')]
// console.log(copyBtns)
//
// copyBtns.forEach(btn=> btn.addEventListener('Copy', ()=>{
//     console.log('Copy')
//     const password = btn.getAttribute('data-hex')
//     console.log(password)
//     navigator.clipboard.writeText(password)
//     btn.textContent = 'Copied'
// }))

// // this works! but it copies spaces which is not cool!:
// function CopyPassword(elementID) {
//     let element = document.getElementById(elementID);
//     let elementText = element.textContent;
//
//     function copyText(text) {
//         navigator.clipboard.writeText(text);
//     }
//
//     copyText(elementText);
// }

function CopyPass() {
    var copyPassword = document.getElementById('thepassword');
    copyPassword.select();
    document.execCommand('copy');
}