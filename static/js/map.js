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

// Initialize the platform object:
var platform = new H.service.Platform({
'app_id': '{{app_ID}}',
'app_code': '{{app_CODE}}',
 useHTTPS: true
});

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

// Define a variable holding SVG mark-up that defines an icon image for user
var svgMarkup = '<svg width="24" height="24" ' +
'xmlns="http://www.w3.org/2000/svg">' +
'<rect stroke="white" fill="red" x="1" y="1" width="22" ' +
'height="22" /><text x="12" y="18" font-size="12pt" ' +
'font-family="Arial" font-weight="bold" text-anchor="middle" ' +
'fill="white">U</text></svg>';

// Create a special marker for the ussr location
var icon = new H.map.Icon(svgMarkup);
var user_marker = new H.map.Marker(user_coords, {icon: icon});
map.addObject(user_marker);

const group = new H.map.Group()
//map.addObject(group)

// Gets all the references from the specified realtime database folder
const database = getDatabase();
const firebaseRef = ref(database, "Images");

// Create the storage link
const storage = getStorage();

async function getURL(store, reference) {
    return await getDownloadURL(sRef(store, reference));
}

// Function dat gets the uploads from the realtime database and makes markers on the map accordingly
async function createMarkersFromPromises(worldMap, folderReference, store) {

    // Gets all the upload references in the reference folder and creates markers for them
    await get(folderReference).then(function(result) {
        result.forEach(function(itemRef) {

            // Creates a marker belonging to the referenced upload and adds it to the map
            var marker = new H.map.Marker({lat: itemRef._node.children_.root_.value.value_,
                                            lng: itemRef._node.children_.root_.right.value.value_})

            // Stores the download URLs of the corresponding image in the markers
            const url = getURL(store, "Images/" + itemRef.ref._path.pieces_[1] + ".jpg");
            url.then(function(result) {
                marker.setData(result);
            });

            // Adds the marker to the group
            group.addObject(marker)
        });
    }).catch(function(error){
      console.log(error);
    });
}

createMarkersFromPromises(map, firebaseRef, storage);
map.addObject(group);

// Adds the click event listener to all marker elements of group
group.addEventListener("tap", event => {
    const bubble = new H.ui.InfoBubble(
    event.target.getPosition(),
    {
        content: '<img src="'+event.target.getData()+'">'
    }
    );
    ui.addBubble(bubble)
});

// Set the scale bar in the top left
var scalebar = ui.getControl('scalebar');
scalebar.setAlignment('top-left');
};