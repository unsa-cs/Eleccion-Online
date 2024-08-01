document.addEventListener("DOMContentLoaded", function() {
    let mensajeElement = document.getElementById("mensaje");
    if (mensajeElement) {
        alert(mensajeElement.value);
    }
});

function agregarPropuesta() {
    let container = document.getElementById('propuestas-container');
    let newInputGroup = document.createElement('div');
    newInputGroup.className = 'input-group mb-3';
    
    let newInput = document.createElement('input');
    newInput.type = 'text';
    newInput.className = 'form-control';
    newInput.name = 'propuestas[]';
    newInput.placeholder = 'Propuesta';
    
    let newButtonDiv = document.createElement('div');
    newButtonDiv.className = 'input-group-append';
    
    let newButton = document.createElement('button');
    newButton.className = 'btn btn-outline-secondary';
    newButton.type = 'button';
    newButton.textContent = 'Añadir';
    newButton.onclick = agregarPropuesta;
    
    newButtonDiv.appendChild(newButton);
    newInputGroup.appendChild(newInput);
    newInputGroup.appendChild(newButtonDiv);
    container.appendChild(newInputGroup);
}
