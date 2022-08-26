// URL = "https://api.thedogapi.com/v1/breeds/"

// function getDogBreeds(event){
//     event.preventDefault()
//     breedsResultDiv = document.querySelector("#breedsResult")
//     dogApi = document.querySelector('#dogApi').value
//     console.log("Dog Breeds")
//     breedsResultDiv.innerHTML = "loading...."
//     console.log("form submitted")
//     fetch(URL+dogApi)
//         .then(res => res.json())
//         .then(data => {console.log(data)
        
//     })
//         .catch(err => console.log(err))
// }
// var data = null;

// var xhr = new XMLHttpRequest();
// xhr.withCredentials = true;

// xhr.addEventListener("readystatechange", function () {
//     if (this.readyState === this.DONE) {
//         console.log(this.responseText);
//     }
//     });

// xhr.open("GET", "https://api.thedogapi.com/v1/breeds?attach_breed=0");
// xhr.setRequestHeader("x-api-key", "live_J4SrAyQeWaJGz4GTWEdTaVRigLiFDQEx78KtKndKua9PihQ7AA3dQidiwF8ceujK");

// xhr.send(data);

var settings = {
    "async": true,
    "crossDomain": true,
    "url": "https://api.thedogapi.com/v1/breeds?attach_breed=0",
    "method": "GET",
    "headers": {
        "x-api-key": "live_J4SrAyQeWaJGz4GTWEdTaVRigLiFDQEx78KtKndKua9PihQ7AA3dQidiwF8ceujK"
    }
    }
    
    $.ajax(settings).done(function (response) {
    dogBreeds = response;
    var select = document.getElementById("breed");
    var options = ["Afgan", "2", "3", "4", "5"];

    var breedNameArray = [];
    for (var i = 0; i < dogBreeds.length; i++) {
        var breedName = dogBreeds[i]['name'];
        breedNameArray.push(breedName);
    }

    console.log(breedNameArray);


    for(var i = 0; i < breedNameArray.length; i++) {
        var opt = breedNameArray[i];
        var el = document.createElement("option");
        el.textContent = opt;
        el.value = opt;
        select.appendChild(el);
    }
    });

