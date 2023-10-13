let totaal = 0;
let teller = 0;
let plus = true;
let keer = true;
let deel = true
function druk_op(e){
    alert("u heeft op: " + e.innerText + " gedrukt!");
    gedruktgetal = parseInt(e.innerText);
    if(plus){
        totaal += gedruktgetal;
    }else if(keer){
        totaal *= gedruktgetal
    }else{
        totaal -= gedruktgetal;
    }
    teller++;
    if(teller > 1){
        alert("het getal is nu: " + totaal);
        console.log(totaal);
    }
}

function swiitch(el){
    plus = el.innerText === '+';
}

for(let x = 0; x<10; x++){
    let mijn_button = document.createElement("button");

    mijn_button.id = x;
    mijn_button.type="button";
    mijn_button.innerText = x;
    mijn_button.setAttribute("onclick", "druk_op(this)");
    calculator.appendChild(mijn_button)
}

let plus_button = document.createElement("button");
plus_button.id = 'plus';
plus_button.type = 'button';
plus_button.innerText = '+';
plus_button.setAttribute("onclick", "swiitch(this)");
calculator.appendChild(plus_button);

let min_button = document.createElement("button");
min_button.id = 'min';
min_button.type = 'button';
min_button.innerText = '-';
min_button.setAttribute("onclick", "swiitch(this)");
calculator.appendChild(min_button);

let keer_button = document.createElement("button");
keer_button.id = 'keer';
keer_button.type = 'button';
keer_button.innerText = 'x';
keer_button.setAttribute("onclick", "swiitch(this)");
calculator.appendChild(keer_button);


// let num1 = 0;
// let num2 = 0;
// let som = "";

// function knop(number) {
//     if (som === '') {
//         num1 = parseInt(number);
//     } else {
//         num2 = parseInt(number);
//     }
//     alert('Je hebt op de knop ' + number + ' gedrukt.');
//     console.log(num1);
//     console.log(num2);
//     console.log('alert 1');
// }

// function resultaat(einde) {
//     som = einde;
//     alert('Je hebt op de knop ' + som + ' gedrukt.');
//     console.log("alert 2")
// }

// function bereken() {
//     let answer = 0;
//     if (som === '+') {
//         answer = num1 + num2;
//     } else if (som === '-') {
//         answer = num1 - num2;
//     }
//     console.log(answer);
//     alert(num1 + ' ' + som + ' ' + num2 + ' = ' + answer);
//     num1 = answer
//     console.log("alert 3")
// }