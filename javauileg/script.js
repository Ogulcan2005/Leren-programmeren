let loggedin = ['berat', 'ogulcan']

function handelInloggen(){
    console.log(loggedin)
    let naam = document.getElementById('inputnaam').value;
    if (naam.length <=0){
        alert('voer een naam in')
        return
    }
    console.log('u hebt op de button geklikt')
    if (loggedin.includes(naam)){
        loggedin.splice(loggedin.indexOf(naam), 1);
        console.log('u bent uitgelogd')
        document.getElementById('melding').innerText = 'u bent uitgelogd ' + naam;
        document.getElementById('inputnaam').value = '';
    } else {
        loggedin.push(naam);
        console.log('u bent ingelogd');
        document.getElementById('melding').innerText = 'u bent ingelogd' + naam;
    }
document.getElementById('inputnaam').value = '';
console.log(loggedin)
    // console.log('u hebt ingelogd: ' + naam)
    // document.getElementById('inputnaam').value = '';
    // document.getElementById('melding').innerText = 'gelukt';
}