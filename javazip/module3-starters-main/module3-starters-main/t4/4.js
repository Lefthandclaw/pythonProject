const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
for (let i = 0; i < students.length; i++) {
    const option = document.createElement("option");  // Create <option> element
    option.value = students[i].value;  // Set the value attribute
    option.textContent = students[i].name;  // Set the text content
    document.querySelector("#target").appendChild(option);  // Append the <option> to #target
}