// Get the Sidenav
var year={};
var main=function() {
    var mySidenav = document.getElementById("mySidenav");

// Get the DIV with overlay effect
    var overlayBg = document.getElementById("myOverlay");

// Toggle between showing and hiding the sidenav, and add overlay effect
    function w3_open() {
        if (mySidenav.style.display === 'block') {
            mySidenav.style.display = 'none';
            overlayBg.style.display = "none";
        } else {
            mySidenav.style.display = 'block';
            overlayBg.style.display = "block";
        }
    }

// Close the sidenav with the close button
    function w3_close() {
        mySidenav.style.display = "none";
        overlayBg.style.display = "none";
    }

    /*function initMap() {
        var myLatLng = {lat: -25.363, lng: 131.044};

         var map = new google.maps.Map(document.getElementById('map'), {
         zoom: 4,
         center: myLatLng
         });

         var marker = new google.maps.Marker({
         position: myLatLng,
         map: map,
         title: 'Hello World!'
         });
         map.addListener("click", function (event) {
         var latitude = event.latLng.lat();
         var longitude = event.latLng.lng();

         var myLatLng = {lat: latitude, lng: longitude};

         marker.setPosition(myLatLng);
         console.log(latitude + ', ' + longitude);


         // Center of map
         map.panTo(new google.maps.LatLng(latitude, longitude));


         }); //end addListener
         map.addListener("bounds_changed", function (event) {
         var bounds = map.getBounds();
         var north=bounds.getNorthEast().lat();
         var south=bounds.getSouthWest().lat();
         var west=bounds.getNorthEast().lng();
         var east = bounds.getNorthEast().lng();

         });

    }*/

    $('#year').on('click','input', function () {
        var filter = document.getElementById("year");
        console.log(filter);
        for(var i = 0; i < filter.children.length; i++){
            var curr = yearfilter.children[i];
            year[curr.value] = curr.checked?true:false;
        }
        console.log(year);
    });
}
$(document).ready(main);




