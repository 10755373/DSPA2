import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.2/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.6.2/firebase-analytics.js";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDsgkvnYUtXSDQbG6VHQ1wsA85OgMl35dg",
    authDomain: "dspa2-89403.firebaseapp.com",
    databaseURL: "https://dspa2-89403-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "dspa2-89403",
    storageBucket: "dspa2-89403.appspot.com",
    messagingSenderId: "1067069276652",
    appId: "1:1067069276652:web:a7905bfd04c842886780c9",
    measurementId: "G-9LFKZ5YGHG"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// Initialize Realtime Firebase
import { getDatabase, ref, get } from "https://www.gstatic.com/firebasejs/9.6.2/firebase-database.js"

// Initialize Storage
import { getStorage, ref as sRef, getDownloadURL } from "https://www.gstatic.com/firebasejs/9.6.2/firebase-storage.js"



// Get the location from the user
function showPosition(position) {
    var user_crd = {lat: position.coords.latitude, lng:position.coords.longitude};
    if (userMarker == null){
        var userIcon = new H.map.Icon("/static/img/you_icon.png", {size: {w: 100, h: 100}});
        var userMarker = new H.map.Marker(user_crd, {icon: userIcon});
        window.map.addObject(userMarker);
    } else {
        userMarker.setGeometry(user_crd);
    }
    window.map.setCenter(user_crd);     
}

function geoError(error){
        switch(error.code) {
            case error.PERMISSION_DENIED:
              Swal.fire({
                icon: 'error',
                text: "Request for Geolocation denied. Please, give permission.",
              })
              break;
            case error.POSITION_UNAVAILABLE:
              Swal.fire({
                icon: 'error',
                text: "Location information is unavailable",
              })
              break;
            case error.TIMEOUT:
              Swal.fire({
                icon: 'error',
                text: "User location request timed out.",
              })
              break;
            case error.UNKNOWN_ERROR:
              Swal.fire({
                icon: 'error',
                text: "An unknown error occurred.",
              })
              break;
        }    
}

// Check if geolocation is supported by the browser
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition,geoError);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}



// Initialize the platform object:
function map_init(){
        var default_coords = {lat: 52, lng: 5};
        var platform = new H.service.Platform({
            'apikey': '6yITc3tU0SIV6hPr3Aaxk1iIdMBHTQPv8sWIBpuLvnY',
        });

        var pixelRatio = window.devicePixelRatio || 1;
        var defaultLayers = platform.createDefaultLayers({
            tileSize: pixelRatio === 1 ? 256 : 512,
            ppi: pixelRatio === 1 ? undefined : 320
        });

        // Step 2: initialize a map
        window.map = new H.Map(document.getElementById('mapContainer'),
            defaultLayers.vector.normal.map,{
            pixelRatio: pixelRatio,
            zoom: 13,
            center: default_coords
        });

    // Step 3: make the map interactive
        var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
        window.ui = H.ui.UI.createDefault(map, defaultLayers);

    // Set the scale bar in the top left
        var scalebar = ui.getControl('scalebar');
        scalebar.setAlignment('top-left');

        var zoom = ui.getControl('zoom');
        zoom.setAlignment('right-middle');
}


const groupmarkers = new H.map.Group()

// Gets all the references from the specified realtime database folder
const database = getDatabase();
const firebaseRef = ref(database, "Images");
// Create the storage link
const storage = getStorage();

// Create a special marker for the pins
var pinIcon = new H.map.Icon("/static/img/pin.png", {size: {w: 100, h: 100}});

var cctvCounter = 0;

// Function dat gets the uploads from the realtime database and makes markers on the map accordingly
async function createMarkersFromPromises(worldMap, folderReference, store) {

    // Gets all the upload references in the reference folder and creates markers for them
    await get(folderReference).then(function(result) {
        result.forEach(function(itemRef) {
            // Creates a marker belonging to the referenced upload and adds it to the map
            var marker = new H.map.Marker({lat: itemRef._node.children_.root_.value.value_,
                                            lng: itemRef._node.children_.root_.right.value.value_},
                                            {icon: pinIcon});
            
            // Stores the download URLs of the corresponding image in the markers
            getDownloadURL(sRef(store, "Images/" + itemRef.ref._path.pieces_[1] + ".jpg"))
            .then(function(result) {
                marker.setData(result);
            });
            cctvCounter += 1;
            // Adds the marker to the group
            groupmarkers.addObject(marker);
        });
        document.getElementById("CctvCounter").innerHTML = "CCTV Counter: "+ cctvCounter;
    }).catch(function(error){
      console.log(error);
    });
}

map_init();
getLocation();
createMarkersFromPromises(map, firebaseRef, storage);

map.addObject(groupmarkers);


// Adds the click event listener to all marker elements of group
groupmarkers.addEventListener("tap", event => {
    const bubble = new H.ui.InfoBubble(
    event.target.getGeometry(),
    {
        content: '<img src="'+event.target.getData()+'">' +
                    '<a href="'+event.target.getData()+'" target="_self" > Click here to Open Image</a>'
    });
    ui.getBubbles().forEach(bub => ui.removeBubble(bub));

    ui.addBubble(bubble)
}, );


var modal = document.getElementById("myModal")
var span = document.getElementsByClassName("close")[0];

function showModal() {
   modal.style.display = 'block';
}

window.addEventListener('load', showModal);

span.onclick = function(){
  modal.style.display = "none";
}

window.onclick = function(event){
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

