document.getElementById("changeTextButton").addEventListener("click", function () {
  const greeting = document.getElementById("greeting");
  greeting.textContent = "You clicked the button! 🎉";
  greeting.style.color = "#28a745";
});
