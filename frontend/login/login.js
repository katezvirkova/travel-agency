document.getElementById("loginForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;


    const data = {
        username: username,
        password: password,
    };

    fetch("http://127.0.0.1:8000/users/login/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
    })

        .then(response => {
    if (response.ok) {
        return response.json();
    } else {
        throw new Error('Error in login');
    }
        })
        .then(data => {
            if (data.access && data.refresh) {
                alert("Login successful!");
                localStorage.setItem('access_token', data.access);
                localStorage.setItem('refresh_token', data.refresh);
                localStorage.setItem('username', data.username);
                window.location.href = '../destinations/destinations.html';
            } else {
                alert("Login failed. No access token received.");
            }
        })
        .catch(error => {
            alert(error.message);
        })})

