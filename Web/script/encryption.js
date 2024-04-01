window.alert("Il suffit de passer la souris sur le texte pour l'afficher correctement")
window.alert("La page journal de bord est inclus mais il faut la chercher. Bonne chance !")
window.alert("Je peux avoir 20 s'il-vous-plaît ?")

function encryptParagraph(selector) {
    let selectorElements = [];
    var mainElement = document.querySelector(selector);
    encryptElement(mainElement);
}

function encryptElement(element) {
    let children = Array.from(element.children);
    if (children.length > 0) {
        children.forEach(child => {
            encryptElement(child);
        });
    }
    else {
        var words = element.textContent.split(" ");
        const spans = words.map(wrapWord);
        let htmls = spans.map(x => x.outerHTML);
        element.innerHTML = htmls.join(" ");
        //let index = 0;
        //element.innerHTML = " ";
        //spans.forEach(span => {
        //    if (index > 0) {
        //        span.innerHTML = " " + span.innerHTML;
        //    }
        //    element.appendChild(span);
        //    index++;
        //});
    }
}

function wrapWord(word) {
    const span = document.createElement('span');
    span.className = "encrypted-container";
    const span1 = document.createElement('span');
    span1.className = "encrypted-content";
    span1.innerHTML = " " + encrypt(word);
    span.appendChild(span1);

    const span2 = document.createElement('span');
    span2.className = "decrypted-content";
    span2.innerHTML = " " + word;
    span.appendChild(span2);

    return span;
}

function encrypt(toEncrypt) {
    var encrypted = "";
    for (var i = 0; i < toEncrypt.length; i++) {
        var c = toEncrypt.charCodeAt(i);
        if (c >= 65 && c <= 90) {
            encrypted += String.fromCharCode((c - 65 + 13) % 26 + 65);
        }
        else if (c >= 97 && c <= 122) {
            encrypted += String.fromCharCode((c - 97 + 13) % 26 + 97);
        }
        else {
            encrypted += String.fromCharCode(c);
        }
    }
    return encrypted;
}
function decrypt(toDecrypt) {
    var decrypted = "";
    for (var i = 0; i < toDecrypt.length; i++) {
        var c = toDecrypt.charCodeAt(i);
        if (c >= 65 && c <= 90) {
            decrypted += String.fromCharCode((c - 65 - 13) % 26 + 65);
        }
        else if (c >= 97 && c <= 122) {
            decrypted += String.fromCharCode((c - 97 - 13) % 26 + 97);
        }
        else {
            decrypted += String.fromCharCode(c);
        }
    }
    return decrypted;
}



window.addEventListener("DOMContentLoaded", (event) => {
    window.setTimeout(startEncrypt, 2000);
});
function startEncrypt() {
    encryptParagraph(".main-content");
}