
  document.querySelector('form').addEventListener('submit', function (event) {
   // Prevent default form submission
    Swal.fire({
      position: 'top-end',
      icon: 'success',
      title: 'Your work has been saved!', // Add exclamation mark for better readability
      showConfirmButton: false,
      timer: 1500
    });
  });
