// $("#form1").submit(function(){
//     e.preventDefault();
//     console.log(5555)

//     $.ajax({
//         method: "POST",
//         url: "/predict",
//         data: { name: "John", location: "Boston" }
//       }).done(function( msg ) {
//           alert( "Data Saved: " + msg );
//         });
//   });
  document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission
        var formData = new FormData(form);
        
        // Show loading page
        window.location.href = '/loading';

        // Send AJAX request to /upload
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(prediction => {
            // Show prediction result page
            window.location.href = '/prediction?prediction=' + encodeURIComponent(prediction);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
