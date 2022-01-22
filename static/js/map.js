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

// response.addHeader("Access-Control-Allow-Origin", "*");

// Check if geolocation is supported by the browser
if (navigator.geolocation) {
    navigator.geolocation.watchPosition(showPosition);
} else {
    x.innerHTML = "Geolocation is not supported by this browser.";
}

// Get the location from the user
function showPosition(position) {
    var latit= position.coords.latitude;
    var longi= position.coords.longitude;
    var user_coords = { lng: longi, lat: latit}


// const hereCredentials = {
//     apikey: 'aZ56VZmkzI0btrmw6qpm-Z5pvNh_j3BKQ8hLig_C1ms'
//     }  

// Initialize the platform object:
var platform = new H.service.Platform({
'apikey': '6yITc3tU0SIV6hPr3Aaxk1iIdMBHTQPv8sWIBpuLvnY',
'useHTTPS': true
//app_id: 'LVzP8znwHiItQlnZsd3g',
//app_code: 'ufbceoJhaG-H270WOS1rww',
// 'apikey': '-Z5pvNh_j3BKQ8hLig_C1ms'
});
// const platform = new H.service.Platform({ 'apikey': 'hereCredentials.apikey' });

// var platform = new H.service.Platform({
//     apikey: '2uMespfkDbPGdqv-oDtU7RrWaqBvVk9woohNUPX4VOs'
// });

var pixelRatio = window.devicePixelRatio || 1;
var defaultLayers = platform.createDefaultLayers({
    tileSize: pixelRatio === 1 ? 256 : 512,
    ppi: pixelRatio === 1 ? undefined : 320
});

// Step 2: initialize a map
var map = new H.Map(document.getElementById('mapContainer'),
defaultLayers.normal.map, {
    pixelRatio: pixelRatio,
    zoom: 13,
    center: user_coords
});

// Step 3: make the map interactive
var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
var ui = H.ui.UI.createDefault(map, defaultLayers);

// Create a special marker for the ussr location
var userIcon = new H.map.Icon("/static/img/you_icon.png", {size: {w: 100, h: 100}});
var userMarker = new H.map.Marker(user_coords, {icon: userIcon});
map.addObject(userMarker);

const groupmarkers = new H.map.Group()

// Gets all the references from the specified realtime database folder
const database = getDatabase();
const firebaseRef = ref(database, "Images");

// Create the storage link
const storage = getStorage();

// Create a special marker for the pins
var pinIcon = new H.map.Icon("/static/img/pin.png", {size: {w: 100, h: 100}});

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

            // Adds the marker to the group
            groupmarkers.addObject(marker)
        });
    }).catch(function(error){
      console.log(error);
    });
}

createMarkersFromPromises(map, firebaseRef, storage);
map.addObject(groupmarkers);

// Adds the click event listener to all marker elements of group
groupmarkers.addEventListener("tap", event => {
    const bubble = new H.ui.InfoBubble(
    event.target.getPosition(),
    {
        content: '<img src="'+event.target.getData()+'">'
    }
    );
    ui.addBubble(bubble)
}, );


// Set the scale bar in the top left
var scalebar = ui.getControl('scalebar');
scalebar.setAlignment('top-left');
};



var modal = document.getElementById("myModal")
var span = document.getElementsByClassName("close")[0];

function showModal() {
   modal.style.display = 'block';
}

window.addEventListener('load', showModal);

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
