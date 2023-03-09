const potten_girraf = 4;
const potten_struisvogel = 2;
const potten_zebra = 4;
let aantal_girraf = parseInt(prompt('hoeveel giraffen wilt u'))
let aantal_zebra = parseInt(prompt('hoeveel zebras wilt u'))
let aantal_struisvogel = parseInt(prompt('hoeveel struisvogels wilt u'))

function bereken_potten(girraf, zebras, struisvogel){
    const aantal_potten = girraf * potten_girraf + zebras * potten_zebra + struisvogel * potten_struisvogel
    return aantal_potten
}
console.log(aantal_girraf + ' giragfen');
console.log(aantal_zebra + ' zebras');
console.log(aantal_struisvogel + ' struisvogels');
console.log(bereken_potten(aantal_girraf, aantal_zebra, aantal_struisvogel));
