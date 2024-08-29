document.getElementById('studentForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Fetching form values
    const email = document.getElementById('email').value;
    const college = document.getElementById('college').value;
    const branch = document.getElementById('branch').value;
    const rollNumber = document.getElementById('rollNumber').value;
    const city = document.getElementById('city').value;
    const review = document.getElementById('review').value;

    // For demonstration purposes, we'll just log the values to the console
    console.log("Email:", email);
    console.log("College:", college);
    console.log("Branch:", branch);
    console.log("Roll Number:", rollNumber);
    console.log("City:", city);
    console.log("Review:", review);

    // You can add code here to send the data to a server or display a success message
    alert('Form submitted successfully!');
});
