$(document).ready(function () {
    $('#contact-form').submit(function (e) {
        // Always prevent the default form submission behavior
        e.preventDefault();

        // Clear all error messages and reset input borders
        clearErrorMessages();
        resetInputBorders();

        var valid = true; // Flag to track overall validation status

        // Validate the name (should not be only numbers)
        var nameValue = $("#contact-name").val();
        if (/^\d+$/.test(nameValue)) {
            valid = false;
            $("#name-error").removeClass("success").addClass("error").html("نام نمی‌تواند فقط شامل اعداد باشد");
            $("#contact-name").addClass("error-border");
        }

        // Validate the phone number (11 characters and numeric)
        var phoneNumber = $("#contact-phone").val();
        if (phoneNumber.length !== 11 || !/^\d+$/.test(phoneNumber)) {
            valid = false;
            $("#phone-error").removeClass("success").addClass("error").html("لطفا یک شماره تلفن معتبر وارد کنید");
            $("#contact-phone").addClass("error-border");
        }

        // Validate the message (should not be empty or too short)
        var messageValue = $("#contact-message").val();
        if (messageValue.length < 10) {
            valid = false;
            $("#message-error").removeClass("success").addClass("error").html("پیام نمی‌تواند کمتر از ۱۰ کاراکتر باشد");
            $("#contact-message").addClass("error-border");
        }

        if (valid) {
            // Perform AJAX submission
            $.ajax({
                type: "POST",
                url: "{% url 'contact:contact' %}", // Replace with the actual URL for form submission
                data: $(this).serialize(),
                success: function (response) {
                    // Handle the successful response here (e.g., show a success message)
                    console.log("Subscription successful!");

                    // Clear error messages and reset input borders
                    clearErrorMessages();
                    resetInputBorders();

                    $("#success-message").removeClass("error").addClass("success").html("پیام شما با موفقیت ارسال شد");
                },
                error: function (xhr, status, error) {
                    // Handle errors here (e.g., show an error message)
                    console.error("Error occurred:", error);
                    var errorMessage = xhr.responseText; // Get the error message from the server

                    // Display the error message and change input border colors
                    $(".message").removeClass("success").addClass("error").html(errorMessage);
                    $(".form-input").addClass("error-border");
                },
            });
        }
    });
});

function clearErrorMessages() {
    $(".message").empty().removeClass("error").addClass("success");
}

function resetInputBorders() {
    $(".form-input").removeClass("error-border");
}

