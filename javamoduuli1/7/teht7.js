const kerrat = Number(prompt("How many times would you like to the roll?"));

let summa = 0;

for (let i = 0; i < kerrat; i++) {
    summa += Math.floor(Math.random() * 6) + 1;
}

document.querySelector('#tulos').innerHTML = summa;
