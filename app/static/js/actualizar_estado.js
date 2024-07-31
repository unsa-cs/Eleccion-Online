function cambiarEstadoLista(id_lista, accion) {
    let url = '';
    let metodo = '';
    let mensajeExito = '';

    if (accion === 'aprobar') {
        url = `/listas/${id_lista}/aprobar`;
        metodo = 'PUT';  
        mensajeExito = 'Lista aprobada correctamente';
    } else if (accion === 'desaprobar') {
        url = `/listas/${id_lista}/desaprobar`;
        metodo = 'PUT'; 
        mensajeExito = 'Lista desaprobada correctamente';
    } else {
        alert('Acción no válida');
        return;
    }

    fetch(url, {
        method: metodo,
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            return response.text().then(text => {throw new Error(text)});
        }
    })
    .then(data => {
        alert(mensajeExito);
        location.reload();
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error al cambiar el estado de la lista');
    });
}
