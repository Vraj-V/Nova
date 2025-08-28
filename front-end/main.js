$(document).ready(function () {
    $('.text').textillate({
        loop:true,
        speed: 1500,
        sync: true,
        in:{
            effect: "bounceIn"
        },
        out:{
            effect: "bounceOut"
        }
    })

        $('.siri-message').textillate({
        loop:true,
        speed: 1500,
        sync: true,
        in:{
            effect: "fadeInUp",
        },
        out:{
            effect: "fadeOutUp",
        }
    })
var siriWave = new SiriWave({
  container: document.getElementById("siri-container"),
  width: 940,
  height: 200,
  style:"ios9",
  amplitude: 1,
  speed: 0.3,
  autostart: true,
  rippleEffect: true,   
  rippleColor: "#ffffff" ,
  color: "#ff0000"
});


$("#Micbtn").click(function () {
    if (typeof eel !== "undefined" && eel.playAssistantSound) {
        eel.playAssistantSound();
    }
    $("#Oval").attr("hidden", true);
    $("#SiriWave").attr("hidden", false);
    eel.takeAllCommand()();
});
});