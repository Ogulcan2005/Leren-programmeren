let num1 = 0;
let num2 = 0;
let som = "";

function knop(number) {
    if (som === '') {
        num1 = parseInt(number);
    } else {
        num2 = parseInt(number);
    }
    // alert('Je hebt op de knop ' + number + ' gedrukt.');
    console.log(num1);
    console.log(num2);
    console.log('alert 1');
}

function resultaat(einde) {
    som = einde;
    // alert('Je hebt op de knop ' + som + ' gedrukt.');
    console.log("alert 2")
}

function bereken() {
    let answer = 0;
    if (som === '+') {
        answer = num1 + num2;
    } else if (som === '-') {
        answer = num1 - num2;
    }
    console.log(answer);
    alert(num1 + ' ' + som + ' ' + num2 + ' = ' + answer);
    num1 = answer
    console.log("alert 3")
}