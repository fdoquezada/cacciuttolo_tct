// Función para manejar la vista de imágenes en el modal
// Función para mostrar alertas personalizadas
function showAlert(type, message) {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-3`;
    alertDiv.style.zIndex = '1050';
    alertDiv.innerHTML = `
        <strong>${type === 'success' ? '¡Éxito!' : 'Error'}:</strong> ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(alertDiv);
    
    // Configurar el botón de cierre
    const closeButton = alertDiv.querySelector('.btn-close');
    closeButton.addEventListener('click', () => {
        alertDiv.remove();
    });
    
    // Eliminar automáticamente después de 5 segundos
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

$(document).ready(function() {
    // Evento para mostrar la imagen en el modal
    $('.ver-imagen').on('click', function() {
        var imagenUrl = $(this).data('imagen-url');
        $('#imagenModalImg').attr('src', imagenUrl);
    });

    // Evento para cerrar el modal
    $('#imagenModal').on('hidden.bs.modal', function () {
        // Limpiar la imagen cuando se cierre el modal
        $('#imagenModalImg').attr('src', '');
    });

    // Evento para el formulario de registro
    $('form').on('submit', function(e) {
        const form = e.target;
        const action = form.action;
        
        // Si es el formulario de registro
        if (action.includes('register')) {
            // Mostrar alerta de éxito al crear cuenta
            showAlert('success', 'Cuenta creada exitosamente. Redirigiendo al inicio de sesión...');
        }
        // Si es el formulario de cierre de sesión
        else if (action.includes('logout')) {
            // Mostrar alerta de éxito al cerrar sesión
            showAlert('success', 'Sesión cerrada exitosamente. Hasta pronto!');
        }
    });
});