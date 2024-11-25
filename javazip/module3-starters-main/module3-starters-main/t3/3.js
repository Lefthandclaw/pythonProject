const names = ['John', 'Paul', 'Jones'];
let nimet = "";

for (let name of names) {
    nimet += `<li>${name}</li>`;
}

document.querySelector("#target").innerHTML = nimet;