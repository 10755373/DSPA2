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

var URLs = [];

// Find all the prefixes and items.
listAll(storageRef)
    .then((res) => {
        res.prefixes.forEach((folderRef) => {
          // All the prefixes under listRef.
          // You may call listAll() recursively on them.
        });
        res.items.forEach((itemRef) => {
          // All the items under listRef.
//          console.log("itemref: ", itemRef);
          getDownloadURL(itemRef).then((url) => {
            console.log("download url: " + url);
            URLs.push(url);
          })
        });
    }).catch((error) => {
        console.log("error")
    });

console.log(URLs)

var URLs = [
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142254/html9.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143104/html10.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142245/CSS8.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143101/CSS9.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142240/Bootstrap5.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143058/Bootstrap6.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142257/JavaScript2.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143106/JavaScript3.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142303/jquery.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143108/jquery4.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142309/php7.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142254/html9.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143104/html10.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142245/CSS8.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143101/CSS9.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142240/Bootstrap5.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143058/Bootstrap6.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142257/JavaScript2.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143106/JavaScript3.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142303/jquery.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143108/jquery4.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142309/php7.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142254/html9.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143104/html10.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142245/CSS8.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143101/CSS9.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142240/Bootstrap5.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143058/Bootstrap6.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142257/JavaScript2.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143106/JavaScript3.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142303/jquery.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143108/jquery4.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142309/php7.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142254/html9.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143104/html10.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142245/CSS8.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143101/CSS9.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142240/Bootstrap5.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143058/Bootstrap6.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142257/JavaScript2.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143106/JavaScript3.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142303/jquery.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143108/jquery4.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318142309/php7.png",
  "https://media.geeksforgeeks.org/wp-content/uploads/20200318143112/php8.png"
  ];
var imgs = URLs.map(function(URL) {
	var img = new Image();
	img.src = URL;
  img.setAttribute("data-lightbox", "galdatalight");
  var idhtml = document.getElementsByClassName("grid")[0];
  idhtml.appendChild(img);
	return img;
});

const lightbox = document.createElement('div')
lightbox.id = 'lightbox'
document.body.appendChild(lightbox)

const images = document.querySelectorAll('img')
images.forEach(image => {
  image.addEventListener('click', e => {
    lightbox.classList.add('active')
    const img = document.createElement('img')
    img.src = image.src
    while (lightbox.firstChild) {
      lightbox.removeChild(lightbox.firstChild)
    }
    lightbox.appendChild(img )
  })
})

lightbox.addEventListener('click', e => {
  if (e.target !== e.currentTarget) return
  lightbox.classList.remove('active')
})