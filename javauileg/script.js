let loggedin = []
function getindexofelementbyname(lijst,naam){
    return-1;
}

function handelInloggen(){
    console.log(loggedin)
    console.log(Date())

    let naam = document.getElementById('inputnaam').value;
    if (naam.length <=0){
        alert('voer een naam in')
        return
    }
    console.log('u hebt op de button geklikt')
    let positie = getindexofelementbyname(loggedin,naam)
    if (positie > -1){
        loggedin.splice(loggedin.indexOf(naam), 1);
        console.log('u bent uitgelogd')
        document.getElementById('melding').innerText = 'u bent uitgelogd ' + naam;
        document.getElementById('inputnaam').value = '';
    } else {
        loggedin.push({'naam' : naam, 'moment' : new Date()});
        console.log('u bent ingelogd');
        document.getElementById('melding').innerText = 'u bent ingelogd' + naam;
    }
document.getElementById('inputnaam').value = '';
console.log(loggedin)
    // console.log('u hebt ingelogd: ' + naam)
    // document.getElementById('inputnaam').value = '';
    // document.getElementById('melding').innerText = 'gelukt';
}