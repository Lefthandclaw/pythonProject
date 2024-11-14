let numerot = [];

while (true) {
    let numero = Number(prompt("Syötä numero, 0 lopettaa:"));
    if (numero === 0) {
        break;
    }
    numerot.push(numero);
}

numerot.sort((a, b) => b - a);

console.log("Numerot isomasta pienempään:");
numerot.forEach(num => console.log(num));
