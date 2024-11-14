let koirat = [];

for (let i = 0; i < 6; i++) {
    let nimi = prompt(`koiran nimi ${i + 1}:`);
    koirat.push(nimi);
}

koirat.sort().reverse();

let ul = document.createElement("ul");
koirat.forEach(nimi => {
    let li = document.createElement("li");
    li.textContent = nimi;
    ul.appendChild(li);
});

document.querySelector("#tulos").appendChild(ul);
