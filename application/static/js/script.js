// script.js

// Example JavaScript code for adding interactivity to the web application

// Function to toggle the visibility of the sidebar
function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('active');
}

// Function to display a confirmation dialog before deleting a record
function confirmDelete() {
    return confirm('Are you sure you want to delete this record?');
}

// Function to handle form validation before submission
function validateForm() {
    var inputField = document.getElementById('inputField').value;

    // Check if inputField is empty
    if (inputField.trim() === '') {
        alert('Please enter a value in the input field.');
        return false; // Prevent form submission
    }

    return true; // Allow form submission
}

// Add event listeners for interactive elements
document.getElementById('toggleSidebarButton').addEventListener('click', toggleSidebar);

var deleteButtons = document.querySelectorAll('.delete-button');
deleteButtons.forEach(function(button) {
    button.addEventListener('click', confirmDelete);
});

document.getElementById('submitFormButton').addEventListener('click', validateForm);
