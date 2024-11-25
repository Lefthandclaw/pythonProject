const target = document.querySelector("#target");

target.appendChild(document.createElement("li")).textContent = "First item"  ;

const secondItem = target.appendChild(document.createElement("li"));
secondItem.textContent = "Second item";
secondItem.classList.add("my-item");

target.appendChild(document.createElement("li")).textContent = "Third item";
