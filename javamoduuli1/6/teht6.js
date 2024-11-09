const ok = confirm("Should I calculate the square root?");

if (ok) {
    const num = Number(prompt("Enter a number:"));

    if (num < 0) {
        document.querySelector('#tulos').innerHTML = "The square root of a negative number is not defined.";
    } else {
        const squareRoot = Math.sqrt(num);
        document.querySelector('#tulos').innerHTML = `The square root of ${num} is ${squareRoot}.`;
    }
} else {
    document.querySelector('#tulos').innerHTML = "The square root is not calculated.";
}