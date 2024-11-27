// Function to fetch all destinations
async function fetchDestinations() {
    const response = await fetch('http://localhost:8000/destinations/');
    if (response.ok) {
        return await response.json(); // Return the parsed JSON data
    } else {
        throw new Error("Can't fetch destinations");
    }
}

// Function to render the page
async function renderPage() {
    const mainElement = document.getElementById('main');

    try {
        const destinations = await fetchDestinations();

        // Clear existing content in the main container
        mainElement.innerHTML = '';

        // Loop through the destinations and create elements
        destinations.forEach(destination => {
            // Create a card for each destination
            const card = document.createElement('div');
            card.classList.add('destination-card'); // Add a CSS class for styling

            // Add content to the card
            card.innerHTML = `
                <h2>${destination.name}</h2>
                <img src="${destination.image_url}" alt="${destination.name}" class="destination-image" />
                <p><strong>Country:</strong> ${destination.country}</p>
                <p>${destination.description}</p>
                <p>Ціна: ${destination.slug}</p>
             
                <!-- Link to the second page, passing the destination name -->
                <a href="../destination_detail/destination%20detail.html?name=${destination.name}" class="see-more-link">See more</a>
                <a href="https://web.telegram.org/k/#@trevel_agency_bot" id="buyLink">
                    <button onclick="buyButton(event)">Купити</button>
                </a>
            `;
            // Append the card to the main container
            mainElement.appendChild(card);
        });
    } catch (error) {
        // Handle errors gracefully
        console.error(error);
        mainElement.innerHTML = '<p>Failed to load destinations. Please try again later.</p>';
    }
}

// Call renderPage on page load
document.addEventListener('DOMContentLoaded', renderPage);

// Buy button functionality to check login
function buyButton(event){
    try {
        const accessToken = localStorage.getItem('access_token');

        // If there's no access token, show an alert and prevent navigation
        if (!accessToken) {
            alert('Вам потрібно залогінитися!');
            event.preventDefault(); // Prevent the link from being followed
        }
    } catch (error) {
        alert('Вам потрібно залогінитися!');
        event.preventDefault(); // Prevent the link from being followed
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const userNameDisplay = document.getElementById("user-name");
    const accessToken = localStorage.getItem('access_token');
    const username = localStorage.getItem('username');
    const loginLink = document.getElementById("login-btn");
    const logoutLink = document.getElementById("logout-btn");
    const registerLink = document.getElementById("register-btn");

    // Logout functionality
    logoutLink.addEventListener('click', function (e) {
        e.preventDefault(); // Prevent default link behavior
        localStorage.removeItem('access_token'); // Remove access token
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('username'); // Remove username
        location.reload(); // Refresh page to update UI
    });

    // Check if user is logged in and update UI
    if (accessToken) {
        userNameDisplay.style.display = 'inline';
        loginLink.style.display = 'none';
        logoutLink.style.display = 'block';
        registerLink.style.display = 'none'; // Optionally hide registration button
    } else {
        userNameDisplay.style.display = 'none';
        loginLink.style.display = 'inline';
        registerLink.style.display = 'inline';
        logoutLink.style.display = 'none';
    }
})