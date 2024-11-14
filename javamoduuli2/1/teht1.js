let numerot = [];

for (let i = 0; i < 5; i++) {
    let numero = prompt(`Syötä numero ${i + 1}:`);
    numerot.push(Number(numero)); // Convert input to a number and store it
}

for (let i = numerot.length - 1; i >= 0; i--) {
    console.log(numerot[i]);
}
