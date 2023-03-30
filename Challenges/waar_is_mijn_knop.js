function button_handel(){
    const element = document.getElementById("knop");
    if (element.innerText == 'Welkom Ogulcan'){
    document.body.removeChild(document.getElementById('knop2'))
    } else {
        element.innerHTML = 'Welkom Ogulcan';
    }

}
knop2.onclick = button_handel