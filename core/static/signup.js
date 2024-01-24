function validateForm() {
    // Get all checkboxes with the name "church"
    var checkboxes = document.querySelectorAll('input[name="church"]:checked');

    // Check if at least one checkbox is checked
    if (checkboxes.length === 0) {
        alert("Please select at least one option.");
        return false; // Prevent form submission
    }

    // Form is valid, allow submission
    return true;
}