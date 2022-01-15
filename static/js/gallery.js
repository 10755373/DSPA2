// Necessary import statements
import {initializeApp} from "https://www.gstatic.com/firebasejs/9.6.2/firebase-app.js";
import {getAnalytics} from "https://www.gstatic.com/firebasejs/9.6.2/firebase-analytics.js";
import { getStorage, ref, listAll, list, getDownloadURL } from "https://www.gstatic.com/firebasejs/9.6.2/firebase-storage.js"


// The web app's Firebase configuration
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
const storage = getStorage();
const storageRef = ref(storage, "Images/");

// Reads all the photos in the database into img elements in the gallery
const lightbox = document.createElement('div')
lightbox.id = 'lightbox'
document.body.appendChild(lightbox)
listAll(storageRef).then(function(result){
    console.log(result);
    result.items.forEach(function(itemRef){
      getDownloadURL(itemRef).then(function(url){

            // Makes a new img element for each photo
            var idhtml = document.getElementsByClassName("gallery")[0];
            	var img = new Image();
	            img.src = url;
              img.setAttribute("data-lightbox", "galdatalight");
            idhtml.appendChild(img);
        });
    })
}).catch(function(error){
    console.log(error);
});


// The onclick part is not yet working!!
// const lightbox = document.createElement('div')
// lightbox.id = 'lightbox'
// document.body.appendChild(lightbox)
// var images = document.getElementById('myGallery0').querySelectorAll('img');
// images.forEach(image => {
//   image.addEventListener('click', e => {
//     lightbox.classList.add('active')
//     const img = document.createElement('img')
//     img.src = image.src
//     while (lightbox.firstChild) {
//       lightbox.removeChild(lightbox.firstChild)
//     }
//     lightbox.appendChild(img )
//   })
// })

// lightbox.addEventListener('click', e => {
//   if (e.target !== e.currentTarget) return
//   lightbox.classList.remove('active')
// })

