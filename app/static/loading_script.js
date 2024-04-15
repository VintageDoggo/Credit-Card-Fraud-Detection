document.addEventListener("DOMContentLoaded", function() {
    // Disable the button to emulate loading time
    var redirectButton = document.getElementById("redirectButton");
    redirectButton.disabled = true;

    // Set a timeout to replace the loading spinner with the button after 4 seconds
    setTimeout(function() {
        var loadingText = document.querySelector('.loading-text');
        var loadingSpinner = document.querySelector('.loading-spinner');
        
        // Hide loading text and spinner
        loadingText.style.display = 'none';
        loadingSpinner.style.display = 'none';

        // Show the button
        //redirectButton.style.display = 'block';
        //redirectButton.disabled = false;

        // Make request to the endpoint
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    var responseData = JSON.parse(xhr.responseText);
                    var prediction = responseData.prediction
                    var destinationURL = "/prediction"; // Replace with your destination page URL
                    // Append response data as parameter to the destination URL
                    var redirectedURL = destinationURL + "?prediction=" + encodeURIComponent(prediction);
                    // Redirect after 4 seconds
                    setTimeout(function() {
                        window.location.href = redirectedURL;
                    }, 4000); // 4000 milliseconds = 4 seconds
                } else {
                    console.error('Request failed:', xhr.status);
                }
            }
        };
        xhr.open("POST", "/upload", true); // Replace with your endpoint URL
        xhr.send();
    }, 3000); // 4000 milliseconds = 4 seconds
});
