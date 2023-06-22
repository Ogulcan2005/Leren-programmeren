var images = [
    "audi.png",
    "auto.png",
    "bmw.png",
    "bugatti.png",
    "ferrari.png",
    "fiat.png",
    "lambo.png",
    "mercedes.png",
    "oud.png",
    "zentorno.png"
];

const div_bord = document.getElementById("galerij");

let i = 0;
let afbeelding = document.createElement('img');
afbeelding.src = images[i];
div_bord.appendChild(afbeelding);

function volgende() {
    i++;
    if (i >= images.length) {
        i = 0;
    }
    afbeelding.src = images[i];
    
}

function vorige() {
    i--;
    if (i < 0) {
        i = images.length - 1;
    }
    afbeelding.src = images[i];
}
