        /*==============================
            Ajax contact form
        ==============================*/
        if($(".contact-form").length > 0) {
          // Validate the contact form
          $('.contact-form').validate({
            // Add requirements to each of the fields
            rules: {
              name: {
                required: true,
                minlength: 2
              },
              email: {
                required: true,
                email: true
              },
              message: {
                required: true,
                minlength: 10
              }
            },

            // Specify what error messages to display
            // when the user does something horrid
            messages: {
              name: {
                required: "Please enter your first name.",
                minlength: $.format("At least {0} characters required.")
              },
              email: {
                required: "Please enter your email.",
                email: "Please enter a valid email."
              },
              message: {
                required: "Please enter a message.",
                minlength: $.format("At least {0} characters required.")
              }
            },

            // Use Ajax to send everything to processForm.php
            submitHandler: function(form) {
              $(".submit-contact").html("Sending...");
              $(form).ajaxSubmit({
                success: function(responseText, statusText, xhr, $form) {
                  $("#contact-content").slideUp(600, function() {
                    $("#contact-content").html(responseText).slideDown(600);
                    $(".submit-contact").html("Send");
                  });
                }
              });
              return false;
            }
          });
        }
