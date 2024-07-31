function cambiarEstadoLista(id_lista, accion) {
    let url = '';
    let mensajeExito = '';

    if (accion === 'aprobar') {
        url = `/aprobar_lista/${id_lista}`;
        mensajeExito = 'Lista aprobada correctamente';
    } else if (accion === 'desaprobar') {
        url = `/desaprobar_lista/${id_lista}`;
        mensajeExito = 'Lista desaprobada correctamente';
    }

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        if (response.ok) {
            alert(mensajeExito);
            location.reload();  
        } else {
            alert('Error al cambiar el estado de la lista');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error al cambiar el estado de la lista');
    });
}
