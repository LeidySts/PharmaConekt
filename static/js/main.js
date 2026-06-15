// Confirmações exclusão de registros
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.btn-confirm-delete');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if(!confirm("Tem certeza que deseja remover esta farmácia do fluxo unificado de dados?")) {
                e.preventDefault();
            }
        });
    });
});