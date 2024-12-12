document.getElementById("getUserButton").addEventListener("click", function () {
  fetch('/api/user')
    .then(response => response.json())
    .then(data => {
      const userInfo = document.getElementById("userInfo");
      if (data.message) {
        userInfo.textContent = data.message;
      } else {
        userInfo.textContent = `Name: ${data.name}, Age: ${data.age}, Email: ${data.email}`;
      }
      userInfo.style.color = "#007bff";
    })
    .catch(error => console.error('Error fetching user data:', error));
});
