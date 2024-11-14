let osallistujanum = Number(prompt("Osallstuja määrä:"));

let osallistujat = [];

for (let i = 0; i < osallistujanum; i++) {
    let nimi = prompt(`Osallistujan nimi ${i + 1}:`);
    osallistujat.push(nimi);
}

osallistujat.sort();

let ol = document.createElement("ol");
osallistujat.forEach(nimi => {
    let li = document.createElement("li");
    li.textContent = nimi;
    ol.appendChild(li);
});

document.querySelector("#tulos").appendChild(ol);