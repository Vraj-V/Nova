$(document).ready(function () {
    // Correct spelling + match Python function name
    eel.expose(DisplayMessage);

    function DisplayMessage(message) {
        console.log("Message from Python:", message); // debug
        $(".siri-message li:first-child").text(message);

        // Restart textillate animation
        $(".siri-message").textillate("in");
    }


    eel.expose(showHood)
    function showHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
        
    }
});
