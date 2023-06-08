const image1 = new Image();
const image2 = new Image();
const image3 = new Image();
const image4 = new Image();
const image5 = new Image();
const image6 = new Image();
const image7 = new Image();
const image8 = new Image();
const image9 = new Image();
const image10 = new Image();

image1.src = "audi.png";
image2.src = "auto.png";
image3.src = "bmw.png";
image4.src = "bugatti.png";
image5.src = "ferrari.png";
image6.src = "fiat.png";
image7.src = "lambo.png";
image8.src = "mercedes.png";
image9.src = "oud.png";
image10.src = "zentorno.png";

function shuffle(array){
    let currentindex = array.length,   randomindex;

    while(currentindex != 0 ){
        randomindex = Math.floor(Math.random() * currentindex);
        currentindex--;

        [array[currentindex]], [array[randomindex]] = [array[randomindex]], [array[currentindex]];
    }
    return array;
}

var auto_lijst = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10];
var auto_lijst2 = shuffle(auto_lijst);

div_bord = document.getElementById("spelbord");
div_bord.appendChild(auto_lijst);