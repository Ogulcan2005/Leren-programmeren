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

function apply_bg_image(){
    foto[0].src = 'kaart_achterkant.png';
    foto[1].src = 'kaart_achterkant.png';
    foto = [];
}

let foto = []

function click(e){
    this.src = this.afbeelding;    
    foto.push(this.afbeelding)
    console.log(foto)

    if(foto.length == 2){
        if(foto[0].afbeelding === foto[1].afbeelding){
            alert('je hebt 2 afbeeldingen geklikt')
            foto = [];
        }else{
            setTimeout(apply_bg_image, 300)
        }
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




