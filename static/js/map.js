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
    navigator.geolocation.getCurrentPosition(showPosition);
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
// useHTTPS: true
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

// Create the storage link
const storage = getStorage();

const group = new H.map.Group()
map.addObject(group)

// Function that gets all the firebase references from a realtime database folder
async function getAllReferences(folderReference) {
    const data = await get(folderReference).then(function(result) {return result});
    const refArray = []
    await data.forEach(function(itemRef){refArray.push(itemRef)});
    return refArray
}

// Gets all the references from the specified realtime database folder
const database = getDatabase();
const firebaseRef = ref(database, "Images");
const itemRefs = getAllReferences(firebaseRef);
console.log(itemRefs);

//get(firebaseRef).then(function(result){
//    result.forEach(function(itemRef){
//        var markers = new H.map.Marker({lat: itemRef._node.children_.root_.value.value_, lng: itemRef._node.children_.root_.right.value.value_})
////        console.log(itemRef.ref);
//        const url = getURL(storage, itemRef.ref._path.pieces_[1]);
//        console.log(url);
//        console.log("hello");
//        map.addObject(markers);
//        markers.setData("<p>Image needs to go here</p>");
//        markers.addEventListener("tap", event => {
//            const bubble = new H.ui.InfoBubble(
//            event.target.getPosition(),
//            {
//              content: event.target.getData()
//            }
//            );
//            ui.addBubble(bubble)
//        })
//        group.addObject(markers)
//    });
//
//    }).catch(function(error){
//      console.log(error);
//    });
//
//    // Move UI elements to the top left of the map
//    var mapSettings = ui.getControl('mapsettings');
//    var zoom = ui.getControl('zoom');
//    var scalebar = ui.getControl('scalebar');
//    var panorama = ui.getControl('panorama');
//
//    panorama.setAlignment('top-right');
//    mapSettings.setAlignment('top-left');
//    zoom.setAlignment('top-left');
//    scalebar.setAlignment('top-left');
};

// createInfoBubble(map);
// credits https://stackoverflow.com/questions/51729938/add-info-bubbles-to-here-


//console.log(getDownloadURL(sRef(storage, "Images/" + itemRef.ref.path.pieces[1])).then(function(url){
//            //markers.setData("<img src='"+ url +"' >");
//            return url
//        }));