document.addEventListener('DOMContentLoaded', function () {
    const categoria_select = document.getElementById('cboCategoria');
    const subcategoria_select = document.getElementById('cboSubcategoria');
    const puntos_container = document.getElementById('puntos-container');
    const puntos_positivos = document.getElementById('puntosPositivosLabel');
    const puntos_negativos = document.getElementById('puntosNegativosLabel');
    const button_add = document.getElementById('btnAdd');
    const button_delete = document.getElementById('btnDel');

    // Manejar los cambios de categorias
    categoria_select.addEventListener('change', function () {
        const categoria_id = this.value;
        const subcategoria_categoria = subcategorias[categoria_id] || [];

        // limpiar opciones
        subcategoria_select.innerHTML = '<option value="" disabled selected>Seleccione una subcategoría</option>';

        // Ingresar nuevas subcategorías
        subcategoria_categoria.forEach(sub => {
            const opcion = document.createElement('option');
            opcion.value = sub.id;
            opcion.textContent = sub.nombre;
            subcategoria_select.appendChild(opcion);
        });

        // Ocultar el contenedor de puntos
        puntos_container.style.display = 'none';
        button_add.disabled = true;
        button_delete.disabled = true;
    });

    // manejar cambios en la subcategoría
    subcategoria_select.addEventListener('change', function () {
        const subcategoria_id = this.value;
        const subcategoria = Object.values(subcategorias)
            .flat()
            .find(s => s.id == subcategoria_id);

        if (subcategoria) {
            puntos_positivos.textContent = `+ ${subcategoria.puntos_positivos}`;
            puntos_negativos.textContent = `- ${subcategoria.puntos_negativos}`;
            button_add.value = subcategoria.puntos_positivos;
            button_delete.value = subcategoria.puntos_negativos;
            button_add.disabled = false;
            button_delete.disabled = false;
            puntos_container.style.display = 'block';

            console.log("Valores asignados:");
            console.log("Puntos positivos:", button_add.value);
            console.log("Puntos negativos:", button_delete.value);
        }
    });

    // Validar el formulario antes de enviarlo
    document.querySelector('form').addEventListener('submit', function (e) {
        if (!button_add.value || !button_delete.value || button_add.value === "0" || button_delete.value === "0") {
            e.preventDefault();
            alert('Por favor, selecciona una subcategoría válida.');
            return false;
        }
    });
});