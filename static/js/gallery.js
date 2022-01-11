            
    // Taking Array of Image Addresses 
    // Suppose it as information from the server
    // Modify this for different address
//     a = [
// 'https://www.geeksforgeeks.org/wp-content/uploads/javascript.png',
// 'https://www.geeksforgeeks.org/wp-content/uploads/jquery-banner.png',
// 'https://www.geeksforgeeks.org/wp-content/uploads/html-768x256.png',
// 'https://www.geeksforgeeks.org/wp-content/uploads/CSS-768x256.png',
// 'https://www.geeksforgeeks.org/wp-content/uploads/php-1-768x256.png',
// 'https://media.geeksforgeeks.org/wp-content/uploads/20200130114942/bootstrap4.png'
//     ];
//     var image = new Image();
//     var x = 0;
//     for (var i = 0; x < a.length; i++) {
//         image.src = a[i];
//         document.getElementById('galleryimages').appendChild(image);
//         // appender(a[i]);
//     }


    // // Function to append the data
    // function appender(x) {
    //     $('galleryimages').html(function(i, original_html) {
    //         return (original_html + x);
    //     });
    // }

{/* <a href="images/1.jpg" data-lightbox="mygallery"><img src="images/1-thumb.jpg"></a>

<a href="https://media.geeksforgeeks.org/wp-content/uploads/20200318142254/html9.png" data-lightbox="mygallery">
                <img src=
    "https://media.geeksforgeeks.org/wp-content/uploads/20200318143104/html10.png">
            </a> */}

// var url = 'https://avatarfiles.alphacoders.com/822/82242.png';

// var image = new Image();
// image.src = url;
// document.getElementById('container').appendChild(image);

// a = [
//     'https://www.geeksforgeeks.org/wp-content/uploads/javascript.png',
//     'https://www.geeksforgeeks.org/wp-content/uploads/jquery-banner.png',
//     'https://www.geeksforgeeks.org/wp-content/uploads/html-768x256.png',
//     'https://www.geeksforgeeks.org/wp-content/uploads/CSS-768x256.png',
//     'https://www.geeksforgeeks.org/wp-content/uploads/php-1-768x256.png',
//     'https://media.geeksforgeeks.org/wp-content/uploads/20200130114942/bootstrap4.png'
//           ];
//           var x = 0;
//           for (var i = 0; x < a.length; i++) {
//             $('#galleryimages').html(function(i, original_html) {
//                 return (original_html + x);
//             });

              
//           };
      
        //   // Function to append the data
        //   function appender(x) {
        //       $('#galleryimages').html(function(i, original_html) {
        //           return (original_html + x);
        //       });
        //   }

// img_count = [
//     'https://www.geeksforgeeks.org/wp-content/uploads/javascript.png',
//     'https://www.geeksforgeeks.org/wp-content/uploads/jquery-banner.png',
//     'https://www.geeksforgeeks.org/wp-content/uploads/html-768x256.png',
//     'https://www.geeksforgeeks.org/wp-content/uploads/CSS-768x256.png',
//     'https://www.geeksforgeeks.org/wp-content/uploads/php-1-768x256.png',
//     'https://media.geeksforgeeks.org/wp-content/uploads/20200130114942/bootstrap4.png'
//           ];
// var url = 'https://avatarfiles.alphacoders.com/822/82242.png';
// $(document).ready(function() {
//     var image = new Image();
//     image.src = url;
//     $('#galleryimages').append(image);
// });
// function addImages(img_count) {
//     var images='';
//     for (var i = 1; i <= img_count; i++) {
//      image = '<img src="images/'+i+'.jpg">';
//     }
//     $(".galleryimages").html(image);
//  }

// var URLs = [
//     "http://placehold.it/128x128.png/f00/400?text=Red",
//     "http://placehold.it/128x128.png/0f0/040?text=Green",
//     "http://placehold.it/128x128.png/00f/004?text=Blue",
//     "http://placehold.it/128x128.png/ff0/440?text=Yellow"
//   ];
  
//   var imgs = URLs.map(function(URL) {
//     var img = new Image();
//     img.src = URL;
//     document.body.appendChild(img);
//     return img;
//   });



// working!!
//   var URLs = [
// 	"http://placekitten.com/200/300",
// 	"http://placekitten.com/200/200",
// 	"http://placekitten.com/100/300",
// 	"http://placekitten.com/300/300"
// ];
var URLs = [
    'https://www.geeksforgeeks.org/wp-content/uploads/javascript.png',
    'https://www.geeksforgeeks.org/wp-content/uploads/jquery-banner.png',
    'https://www.geeksforgeeks.org/wp-content/uploads/html-768x256.png',
    'https://www.geeksforgeeks.org/wp-content/uploads/CSS-768x256.png',
    'https://www.geeksforgeeks.org/wp-content/uploads/php-1-768x256.png',
    'https://media.geeksforgeeks.org/wp-content/uploads/20200130114942/bootstrap4.png'
          ];
var imgs = URLs.map(function(URL) {
	var img = new Image();
    // href=URL;
    // data-lightbox="mygallery"; 
	img.src = URL;
  // img.datalightbox = "roadtrip";
  // img.attr("data-lightbox", "roadtrip")
  // img.attr("roadtrip", img.attr(data-lightbox));
  img.attr = "testrinus"
	galleryimages.appendChild(img);
	return img;
});

$(function(){
  $(".testrinus").each(function () {
          var img = $(this);
          img.attr("data-lightbox", "roadtrip");
          // img.attr("src", 'image_url');
  });
  });

// https://www.jqueryscript.net/lightbox/lightbox2.html

const lightbox = document.createElement('div')
lightbox.id = 'lightbox'
// lightbox.data-lightbox = "mygallery"
document.body.appendChild(lightbox)

const images = document.querySelectorAll('img')
images.forEach(image => {
  // image.attr(data-lightbox, "roadtrip")
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