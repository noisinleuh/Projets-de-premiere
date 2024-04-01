function toggle_nuit() {
    if (document.querySelector("body").className == 'jour') {
        nuit();
    }
    else {
        jour();
    }
}
function nuit() {
    document.querySelector("body").className = 'nuit';
    let newsrc = document.querySelector("img[id='mode']").src.replace("moon", "sun");
    document.querySelector("img[id='mode']").src = newsrc;
}

function jour() {
    document.querySelector("body").className = 'jour';
    let newsrc = document.querySelector("img[id='mode']").src.replace("sun","moon" );
    document.querySelector("img[id='mode']").src = newsrc;
}

//function toggle_nuit2() {
//    if (document.querySelector("body").class == 'jour') {
//        nuit2();
//    }
//    else {
//        jour2();
//    }
//}

//function nuit2() {
//    document.querySelector("body").class = 'nuit';
//    document.querySelector("link[name='maincss']").href = '../style/main_nuit.css';
//    document.querySelector("img[id='mode']").src = '../media/sun.png';
//}

//function jour2() {
//    document.querySelector("body").class = 'jour';
//    document.querySelector("link[name='maincss']").href = '../style/main.css';
//    document.querySelector("img[id='mode']").src = '../media/moon.png';
//}
