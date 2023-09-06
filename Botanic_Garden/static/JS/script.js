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