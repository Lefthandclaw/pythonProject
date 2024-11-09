const vuosi = Number(prompt("Enter a year:"));

let välivuosi;
if ((vuosi % 4 === 0 && vuosi % 100 !== 0) || (vuosi % 400 === 0)) {
    välivuosi = true;
} else {
    välivuosi = false;
}

if (välivuosi) {
    document.querySelector('#tulos').innerHTML = `${vuosi} is a leap year.`;
} else {
    document.querySelector('#tulos').innerHTML = `${vuosi} is not a leap year.`;
}