let numerot = [];

while (true) {
    let numero = Number(prompt("Syötä numero"));
    if (numerot.includes(numero)) {
        alert('Numero on syötetty jo, lopetellaan')
        break;
    }
    numerot.push(numero);
}

numerot.sort((a, b) => a - b);

console.log("Numerot");
numerot.forEach(num => console.log(num));