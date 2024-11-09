const ekavuosi = Number(prompt("Enter the start year:"));
const loppuvuosi = Number(prompt("Enter the end year:"));

function valivuosi(vuosi) {
    return (vuosi % 4 === 0 && (vuosi % 100 !== 0 || vuosi % 400 === 0));
}

let valivuodet = [];

for (let vuosi = ekavuosi; vuosi <= loppuvuosi; vuosi++) {
    if (valivuosi(vuosi)) {
        valivuodet.push(vuosi);
    }
}

const ul = document.querySelector('#tulos');

valivuodet.forEach(vuosi => {
    const li = document.createElement('li');
    li.textContent = vuosi;
    ul.appendChild(li);
});