document.querySelectorAll('.btn-delete').forEach(button => {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        const confirmacao = confirm('Tem certeza que deseja excluir este usuário?');
        if (confirmacao) {
            this.closest('form').submit(); 
        }});
    });