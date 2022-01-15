// Set constraints for the video stream
var constraints = { video: { facingMode: "user" }, audio: false };
var track = null;


// Define constants
const cameraView = document.querySelector("#camera--view"),
cameraOutput = document.querySelector("#camera--output"),
cameraSensor = document.querySelector("#camera--sensor"),
cameraTrigger = document.querySelector("#camera--trigger");


// Access the device camera and stream to cameraView
function cameraStart() {
    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(function(stream) {
            track = stream.getTracks()[0];
            cameraView.srcObject = stream;
        })
        .catch(function(error) {
            console.error("Oops. Something is broken.", error);
        });
};

// Take a picture when cameraTrigger is tapped
cameraTrigger.onclick= function() {
    if (navigator.geolocation) {
        navigator.geolocation.watchPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
    cameraSensor.width = cameraView.videoHeight;
    cameraSensor.height = cameraView.videoHeight;
    cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
    cameraSensor.toBlob(photo, "image/jpg");
    cameraOutput.src = cameraSensor.toDataURL("image/jpg");
    cameraOutput.classList.add("taken");
    // track.stop();
};

function photo(file) {
    var formdata =  new FormData();
    formdata.append("snap", file);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "{{ url_for('photo_1') }}", true);
    xhr.onload = function() {
        if(this.status = 200) {
            console.log(this.response);
        } else {
            console.error(xhr);
        }
        alert(this.response);
    };
    xhr.send(formdata);
};


function showPosition(position) {
    var lat =position.coords.latitude;
    var lon= position.coords.longitude;
}

// Start the video stream when the window loads
window.addEventListener("load", cameraStart, false);
