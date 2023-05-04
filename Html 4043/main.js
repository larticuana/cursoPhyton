var nombre = "Luis";
var edad = 24
var estatura = 183
var peso = 83

var datos = document.getElementById("datos");

let alturaMetros = estatura / 100;


let imc = peso / (alturaMetros ** 2);


imc = imc.toFixed(2);


datos.innerHTML = `
<h1>Soy una caja de datos</h1>
<h2>Mi nombre es: ${nombre}</h2>
<h2>Mi edad es: ${edad}</h2>
<h2>Mi altura es: ${estatura}</h2>
<h2>Mi indice de masa corporal es: ${imc}</h2>
`;

