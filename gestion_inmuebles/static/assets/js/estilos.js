document.querySelectorAll('.menu-button').forEach(button => {
    button.addEventListener('click', () => {
      const submenu = button.nextElementSibling;
  
      // Cierra otros menús abiertos
      document.querySelectorAll('.submenu').forEach(item => {
        if (item !== submenu) item.style.display = 'none';
      });
  
      // Alterna el estado del menú seleccionado
      submenu.style.display = submenu.style.display === 'block' ? 'none' : 'block';
    });
  });