let image1 = document.createElement("img");
image1.src = "audi.png";

let image2 = document.createElement("img");
image2.src = "auto.png";

let image3 = document.createElement("img");
image3.src = "bmw.png";

let image4 = document.createElement("img");
image4.src = "bugatti.png";

let image5 = document.createElement("img");
image5.src = "ferrari.png";

let image6 = document.createElement("img");
image6.src = "fiat.png";

let image7 = document.createElement("img");
image7.src = "lambo.png";

let image8 = document.createElement("img");
image8.src = "mercedes.png";

let image9 = document.createElement("img");
image9.src = "oud.png";

let image10 = document.createElement("img");
image9.src = "zentorno.png";




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

for (let i = 0; i < auto_lijst.length; i++) {
    div_bord.appendChild(auto_lijst[i]);
  }



