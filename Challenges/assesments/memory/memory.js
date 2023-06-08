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

function click(e){
    console.log(this.afbeelding)
    this.src = this.afbeelding;
    let poging1 = img;
    let poging2 = img;
    if(poging1 != poging2){
        this.src = 'kaart_achterkant.png';
    }
}

for (let i = 0; i < images.length; i++) {
    let img = document.createElement('img');
    img.src = 'kaart_achterkant.png';
    img.afbeelding = images[i];
    div_bord.appendChild(img);
    img.onclick = click


}
for (let i = 0; i < shuffleImage.length; i++) {
    let img = document.createElement('img');
    img.src = 'kaart_achterkant.png';
    img.afbeelding = shuffleImage[i];
    div_bord.appendChild(img);
    img.onclick = click
}




