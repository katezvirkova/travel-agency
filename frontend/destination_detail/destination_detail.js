// Function to fetch the destination details by name
async function fetchDestination(name) {
    const response = await fetch(`http://localhost:8000/destinations/${name}/`);

    if (response.ok) {
        const destination = await response.json();

        // Render destination details
        document.getElementById('destination-name').textContent = destination.name;
        document.getElementById('destination-country').textContent = `Country: ${destination.country}`;
        document.getElementById('destination-description').textContent = destination.description;

        // Check if there's an image URL and display it
        if (destination.image_url) {
            const imgElement = document.createElement('img');
            imgElement.src = destination.image_url;
            imgElement.alt = destination.name;
            document.getElementById('destination-image').appendChild(imgElement);
        }
    } else {
        // Handle error if destination is not found
        document.getElementById('destination-detail').innerHTML = `<p>Destination not found.</p>`;
    }
}

// Get the destination name from the URL (e.g., localhost:8000/destinations/<name>)
document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const destinationName = urlParams.get('name'); // Retrieve the name parameter

    if (destinationName) {
        fetchDestination(destinationName);
    } else {
        document.getElementById('destination-detail').innerHTML = `<p>No destination specified.</p>`;
    }
});
