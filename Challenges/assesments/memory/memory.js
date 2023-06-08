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

function shuffle(array) {
    let currentIndex = array.length, randomIndex;

    // While there remain elements to shuffle.
    while (currentIndex != 0) {

        // Pick a remaining element.
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        // And swap it with the current element.
        [array[currentIndex], array[randomIndex]] = [
            array[randomIndex], array[currentIndex]];
    }

    return array;
}

var shuffleImage = shuffle(images);
const div_bord = document.getElementById("spelbord");


for (let i = 0; i < images.length; i++) {
    let img = document.createElement('img');
    img.src = images[i];
    div_bord.appendChild(img);
}
for (let i = 0; i < shuffleImage.length; i++) {
    let img = document.createElement('img');
    img.src = shuffleImage[i];
    img.src = 
    div_bord.appendChild(img);
}




