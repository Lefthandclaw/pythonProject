const name = prompt("Enter name:");

const random = Math.floor(Math.random() * 4) + 1;

let house;
if (random === 1) {
    house = 'Gryffindor';
} else if (random === 2) {
    house = 'Slytherin';
} else if (random === 3) {
    house = 'Hufflepuff';
} else {
    house = 'Ravenclaw';
}

document.querySelector('#tulos').innerHTML = `${name}, in ${house}.`;
