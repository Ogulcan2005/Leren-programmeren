let uitkomst = "";
const drank = ["fris","bier","wijn"];
let bon = [];

let fris = 6.99;
let bier= 4.99;
let wijn= 7.99;
let gekozen_drank = ''
while(gekozen_drank != 'stop'){
    gekozen_drank = prompt('wat wilt u bestellen');
    if (drank.includes(gekozen_drank)){
        if (gekozen_drank == 'bier'){
            console.log('1 bier is '+ '' + bier + '' + ' euro');
            let vraag_hoeveel = parseInt(prompt('hoeveel ' + gekozen_drank + ' wilt u'));
            let bon_vraag = ('aantal ' + vraag_hoeveel + gekozen_drank + ' is' + (vraag_hoeveel * bier));
            bon.push(bon_vraag);
            console.log(bon_vraag)
        } else if (gekozen_drank == 'fris'){
            console.log('1 fris is '+ '' + fris + '' + ' euro');
            vraag_hoeveel = parseInt(prompt('hoeveel ' + gekozen_drank + ' wilt u'));
            bon_vraag = ('aantal ' + vraag_hoeveel + gekozen_drank + ' is ' + (vraag_hoeveel * fris));
            bon.push(bon_vraag);
            console.log(bon_vraag)
        } else if (gekozen_drank == 'wijn'){
            console.log('1 wijn is '+ '' + wijn + '' + ' euro');
            vraag_hoeveel = parseInt(prompt('hoeveel ' + gekozen_drank + ' wilt u'));
            bon_vraag = ('aantal ' + vraag_hoeveel + gekozen_drank + ' is ' + (vraag_hoeveel * wijn));
            bon.push(bon_vraag);
            console.log(bon_vraag)}
    
    } else {
        console.log('kies wijn, bier of fris');
    }}
    console.log(bon);

