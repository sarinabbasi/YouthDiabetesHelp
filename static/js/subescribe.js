$(document).ready(function () {
    // Attach a click event handler to the subscribe button
    $("#subscribe-btn").click(function (event) {
        event.preventDefault(); // Prevent the default form submission behavior

        // Reset the message and input border
        $(".message").empty();
        $("#phone").removeClass("error-border");

        // Get the form data
        var formData = $("#subscription-form").serialize();

        // Validate the phone number (11 characters and numeric)
        var phoneNumber = $("#phone").val();
        if (phoneNumber.length !== 11 || !/^\d+$/.test(phoneNumber)) {
            // Display the error message
            $(".message").removeClass("success").addClass("error").html("لطفا یک شماره تلفن معتبر وارد کنید");

            // Add red border to the input field
            $("#phone").addClass("error-border");

            return; // Abort the submission
        }

        // Perform the AJAX POST request
        $.ajax({
            type: "POST",
            url: "{% url 'home:home' %}", // Replace 'your_subscription_endpoint' with the actual URL to handle the form submission on the server-side
            data: formData,
            success: function (response) {
                // Handle the successful response here (e.g., show a success message)
                console.log("Subscription successful!");
                $(".message").removeClass("error").addClass("success").html("اشتراک با موفقیت انجام شد");
            },
            error: function (xhr, status, error) {
                // Handle errors here (e.g., show an error message)
                console.error("Error occurred:", error);
                var errorMessage = xhr.responseText; // Get the error message from the server
                $(".message").removeClass("success").addClass("error").html(errorMessage);
            },
        });
    });
});
