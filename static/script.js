document.getElementById("changeTextButton").addEventListener("click", function () {
  const greeting = document.getElementById("greeting");
  greeting.textContent = "You clicked the button! 🎉";
  greeting.style.color = "#28a745";
});

// בקשה ל-API לקבלת מידע על משתמש
document.getElementById("getUserButton").addEventListener("click", function () {
  fetch('/api/user')
    .then(response => response.json())
    .then(data => {
      const userInfo = document.getElementById("userInfo");
      userInfo.textContent = `Name: ${data.name}, Age: ${data.age}, Email: ${data.email}`;
      userInfo.style.color = "#007bff";
    })
    .catch(error => console.error('Error fetching user data:', error));
});
