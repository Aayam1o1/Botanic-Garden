function dropMenu(){
    
    const dropMenu = document.getElementById("dropdown-menu")
    if (dropMenu.style.display === "block") {
        dropMenu.style.display = "none"

    }
    else
    {
        dropMenu.style.display = "block"
    }
}

// Custom function to display and keep the value in a tooltip
function updateValue() {
    const valueSlider = document.getElementById('valueSlider');
    const valuePopup = document.getElementById('valuePopup');
    const value = valueSlider.value;
    valuePopup.textContent = `Rs${value}`;
    valuePopup.style.left = `${(value / 20000) * 100}%`;
    console.log("message")
}

// Attach the custom function to the input event
// const valueSlider = document.getElementById('valueSlider');
// valueSlider.addEventListener('input', updateValue);

// Display the tooltip initially when the page loads
window.addEventListener('DOMContentLoaded', updateValue);



function lol()
    {
        console.log("script js ko")
    }
