$(document).ready(function () {
    $("input[name=login]").change(function() {
        if ($("input[name=login]").val().length < 5) {
            $("input[name=login]").attr("style", "margin-top: 2px !important;");
            $("#login-label").css("display", "block");
        }
        else {
            $("input[name=login]").attr("style", "margin-top: 15px !important;");
            $("#login-label").css("display", "none");
        }
    });

    $("input[name=password]").change(function() {
        if ($("input[name=password]").val().length < 8) {
            $("input[name=password]").attr("style", "margin-top: 2px !important;");
            $("#password-label").css("display", "block");
        }
        else {
            $("input[name=password]").attr("style", "margin-top: 15px !important;");
            $("#password-label").css("display", "none");
        }

        if ($("input[name=confirm-password]").val() == $("input[name=password]").val()) {
            $("input[name=confirm-password]").attr("style", "margin-top: 15px !important;");
            $("#mismatch-password-label").css("display", "none");
        }
    });

    $("input[name=email").change(function() {
        let regex = /\S+@\S+\.\S+/;
        if (!regex.test($("input[name=email").val())) {
            $("input[name=email]").attr("style", "margin-top: 2px !important;");
            $("#email-label").css("display", "block");
        }
        else {
            $("input[name=email]").attr("style", "margin-top: 15px !important;");
            $("#email-label").css("display", "none");
        }
    });

    $("input[name=confirm-password]").change(function() {
        if ($("input[name=password]").val().length != 0) {
            if ($("input[name=confirm-password]").val() != $("input[name=password]").val()) {
                $("input[name=confirm-password]").attr("style", "margin-top: 2px !important;");
                $("#mismatch-password-label").css("display", "block");
            }
            else {
                $("input[name=confirm-password]").attr("style", "margin-top: 15px !important;");
                $("#mismatch-password-label").css("display", "none");
            }
        }
    });

    $(".registration-form").submit(function() {
        let error_label_check = false;
        $(".error-label").each(function() {
            if ($(this).css("display") != "none" && $(this).attr("id") != "post-status-error") {
                error_label_check = true;
                return false;
            }
        });
        if (error_label_check) {
            return false;
        }

        if ($("input[name=login]").val().length == 0) {
            $("input[name=login]").attr("style", "margin-top: 2px !important;");
            $("#login-label").css("display", "block");
            return false;
        }

        if ($("input[name=email]").val().length == 0) {
            $("input[name=email]").attr("style", "margin-top: 2px !important;");
            $("#email-label").css("display", "block");
            return false;
        }

        if ($("input[name=password]").val().length == 0) {
            $("input[name=password]").attr("style", "margin-top: 2px !important;");
            $("#password-label").css("display", "block");
            return false;
        }

        if ($("input[name=confirm-password]").val().length == 0) {
            $("input[name=confirm-password]").attr("style", "margin-top: 2px !important;");
            $("#mismatch-password-label").css("display", "block");
            return false;
        }
    });
});
