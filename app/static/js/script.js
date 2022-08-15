// global variables
const flash = document.getElementById("flash");
const flash_close = document.getElementById("flash_close");

// close flash message section after 3 seconds
setInterval(() => {
    flash.style.display = "none";
}, 3000);

// flash message close button
flash_close.addEventListener("click", function(event) {
    flash.parentNode.removeChild(flash);
    // FIX: prevent site from reloading
    event.preventDefault();
});