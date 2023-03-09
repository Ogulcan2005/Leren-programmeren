let uitkomst = "";
const drank = ["fris","bier","wijn","stop"];
let bon = [];

let element = bon.find(element => element.drank == gekozen_drank)

let fris = 6.99;
let bier= 4.99;
let wijn= 7.99;

let gekozen_drank = ''

while(gekozen_drank != 'stop'){
    gekozen_drank = prompt('wat wilt u bestellen');
    if (drank.includes(gekozen_drank)){
        if (gekozen_drank == 'bier'){
            console.log('1 bier is ', bier, ' euro');
            let vraag_hoeveel = parseInt(prompt('hoeveel ', gekozen_drank, ' wilt u'));
            if (element = bon.find(element => element.drank == 'bier')){
                element['aantal'] += vraag_hoeveel
            } else {element = {'drank' : 'bier', 'aantal' : vraag_hoeveel, 'prijs' : (bier), 'totaal' : (bier * vraag_hoeveel)};
            bon.push(element);
        }}else if (gekozen_drank == 'fris'){
            console.log('1 fris is ', fris, ' euro');
            vraag_hoeveel = parseInt(prompt('hoeveel ', gekozen_drank, ' wilt u'));
            if (element = bon.find(element => element.drank == 'fris')){
                element['aantal'] += vraag_hoeveel
            } else {element = {'drank' : 'fris', 'aantal' : vraag_hoeveel, 'prijs' : (fris), 'totaal' : (fris * vraag_hoeveel)};
            bon.push(element);
        } console.log(element);
        } else if (gekozen_drank == 'wijn'){
            console.log('1 wijn is '+ '' + wijn + '' + ' euro');
            vraag_hoeveel = parseInt(prompt('hoeveel ' + gekozen_drank + ' wilt u'));
            if (element = bon.find(element => element.drank == 'wijn')){
                element['aantal'] += vraag_hoeveel
            } else {element = {'drank' : 'wijn', 'aantal' : vraag_hoeveel, 'prijs' : (wijn), 'totaal' : (wijn * vraag_hoeveel)};
            bon.push(element);
        }} else if(gekozen_drank == 'stop'){
            break
        }
    }else {
        console.log('kies bier, wijn of fris');
    }
}    
console.log(bon);

