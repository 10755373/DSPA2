// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.2/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.6.2/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// The web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
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

import { getStorage, ref as sRef, uploadBytesResumable, getDownloadURL } from "https://www.gstatic.com/firebasejs/9.6.2/firebase-storage.js"

// Initialize Realtime Firebase
import { getDatabase, ref, set, child, get, update, remove } from "https://www.gstatic.com/firebasejs/9.6.2/firebase-database.js"
const realdb = getDatabase();

// Useful functions for file extraction and naming
function GetFileExt(file){
    var temp = file.name.split('.');
    var ext = temp.slice((temp.length-1),(temp.length));
    return '.' + ext[0];
}

function GetFileName(file){
    var temp = file.name.split('.');
    var fname = temp.slice(0,-1).join('.');
    return fname;
}

function ValidateName(){
    var regex = /[\.#$\[\]]/
    return !(regex.test(namebox.value));
}

// Upload process

async function UploadProcess(ImgToUpload, ImgName, location){

    const storage = getStorage();
    const storageRef = sRef(storage, "Images/"+ImgName);
    const UploadTask = uploadBytesResumable(storageRef, ImgToUpload, location);
}

// Functions for realtime database

// Saves the URL, name and location of a photo to the database.
function SaveURLtoRealtimDB(URL, filename, location){

    set(ref(realdb, "ImagesLinks/"+filename),{
        ImageName: filename,
        ImageLocation: location,
        ImageUrl: URL
    });
}

function GetURLtoRealtimDB(filename){
    var dbRef = ref(realdb);

    get(child(dbRef, "ImagesLinks/"+filename)).then((snapshot)=>{
        if(snapshot.exists()){
            return snapshot.val().ImgUrl; // This returns the image source URL in real time
        }
    })
}

// @ALEX: CALL THIS FUNCTION WHEN THE MODEL CLASSIFIES THE IMAGE AS GOOD
//UploadProcess(ImgToUpload, ImgName, location);

// @RINUS: USE (A VARIATION OF) THIS FUNCTION TO GET THE IMAGES FOR THE GALLERY
//GetURLtoRealtimDB(filename);
