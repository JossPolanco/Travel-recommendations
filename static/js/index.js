document.addEventListener("DOMContentLoaded", async function(){
    
    // Calls an endpoint of the api to call a limited number of places and show it below the form
    const response = await fetch("/place/limit/20")
    try {
        // if the response is not ok then shows an error
        if(!response.ok) {
            throw new Error("Error finding places.");
        }
        // saves the response in json format in data
        const data = await response.json()
        console.log("Loading data successful.")
        // Calls the function that displays each place in data
        displayPlaces(data);
    } catch (error) {
        console.log("Error loading data", error)
    }

    document.getElementById("search_form").addEventListener("submit", async function (e) {
        e.preventDefault();
        // Collect the data from the form
        var formData = new FormData(e.target);
        var data = Object.fromEntries(formData);        
        // Calls to the api
        fetch("/search", {
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json()) // We convert it in json format
        .then(places => {
            // Calls the method to display all the places
            displayPlaces(places)
        })
        
    })
});

// function to display all the data collected when the page is loaded
function displayPlaces(data) {
    console.log("Data:", data)
    // Creates the div where all the info is going to be print
    const locationInfo = document.getElementById("location-info");
    try {        
        // Clears the div before print the new info
        locationInfo.innerHTML = ``
        // Creates and div element
        const placesGallery = document.createElement("div");
        // Adds the name row in the div element
        placesGallery.className = "row";
        // If there is places
        if(data.length){
            // For each place in data we create the card
            data.forEach(element => {
                // Creates and div element
                const place = document.createElement("div")
                // Adds the name class in the div element
                place.className ="col s8 m4"            
                // Adds all the info needed in the card
                place.innerHTML = `
                    <div class="card fixed-card-height">
                        <div class="card-image">
                            <img src="${element[12]}" class="card-img">
                            <span class="card-title">${element[1]}</span>
                        </div>
                        <div class="card-content truncate-text">
                            <p>${element[7]}</p>
                        </div>
                        <div class="card-action">
                            <a href="/place/detailed/${element[0]}" class="card-action-a">Ver más</a>
                        </div>
                    </div>
                `;
                // Appends each place in the div
                placesGallery.appendChild(place);
            });        
            // If there is no places
        } else {
            // Creates and div element
            const place = document.createElement("div")
            // Adds the name class in the div element
            place.className ="col s8 m4"            
            // Adds all the info needed in the card
            place.innerHTML = `
                <div class="col s12">
                    <div class="card-no-content">
                        <p>No se encontraron lugares.</p>
                    </div>
                </div>
            `;
            // Appends each place in the div
            placesGallery.appendChild(place);
        }
            // If there is the element
            if (locationInfo) {
                // Appends the gallery of the places to the element
                locationInfo.appendChild(placesGallery);
            } else {
                console.error("Element with id 'location-info' not found.");
            }
        } catch (error) {
            console.error("Error in display places:", error);
        }            
}