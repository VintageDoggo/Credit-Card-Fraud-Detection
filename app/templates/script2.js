$(document).ready(function() {
  $('#uploadForm').submit(function(e) {
      e.preventDefault(); // prevent the form from submitting normally

      var formData = new FormData();
      formData.append('file', $('#file')[0].files[0]);

      $.ajax({
          url: '/upload', // Replace 'your-flask-endpoint' with your actual Flask endpoint
          type: 'POST',
          data: formData,
          processData: false,
          contentType: false,
          success: function(response) {
              $('#pred').text(response); // Update the prediction result
          },
          error: function(xhr, status, error) {
              console.error('Error:', error);
          }
      });
  });
});