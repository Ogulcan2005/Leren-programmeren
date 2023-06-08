const images = [
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

function shuffle(array){
    let currentindex = array.length,   randomindex;

    while(currentindex != 0 ){
        randomindex = Math.floor(Math.random() * currentindex);
        currentindex--;

        [array[currentindex]], [array[randomindex]] = [array[randomindex]], [array[currentindex]];
    }
    return array;
}

const div_bord = document.getElementById("spelbord");

for(let i = 0; i < images.length; i++){
    let img = document.createElement('img')
    img.src = images[i]
    div_bord.appendChild(img);
}



