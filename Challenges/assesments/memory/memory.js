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

function shuffle(array) {
    return array.sort(() => Math.random() - 0.5);
}

const shuffledImages = shuffle(images);
const div_bord = document.getElementById("spelbord");

shuffledImages.forEach((src) => {
    const image = document.createElement("img");
    image.src = src;
    div_bord.appendChild(image);
});
  
