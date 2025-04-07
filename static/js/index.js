document.addEventListener("DOMContentLoaded", async function(){

    const response = await fetch("/place/limit/20")
    try {
        if(!response.ok) {
            throw new Error("Error finding places.");
        }
        const data = await response.json()
        console.log("Response ok", data)
        displayPlaces(data);
    } catch (error) {
        console.log("Error loading data", error)
        // document.getElementById("location-info").textContent = "Error al cargar datos";
    }
});

function displayPlaces(data) {
    try {
        const placesGallery = document.createElement("div");
        placesGallery.className = "row";
        data.forEach(element => {        
            console.log(element)
            const place = document.createElement("div")
            place.className ="col s8 m4"
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
                        <a href="/place/${element[0]}" class="card-action-a">Ver más</a>
                    </div>
                </div>
            `;
            placesGallery.appendChild(place);
    });

    const locationInfo = document.getElementById("location-info");
        if (locationInfo) {
            locationInfo.appendChild(placesGallery);
        } else {
            console.error("Element with id 'location-info' not found.");
        }
    } catch (error) {
        console.error("Error in displayPlaces:", error);
    }
    

    document.getElementById("location-info").appendChild(placesGallery);

    document.getElementById("search_form").addEventListener("submit", async function (e) {
        e.preventDefault();

        var formData = new FormData(e.target);
        var data = Object.fromEntries(formData);

        alert(JSON.stringify(data))
        
    })
    
}