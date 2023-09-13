console.log("Script is running!");
document.addEventListener('DOMContentLoaded', function () {
    const imageInput = document.querySelector('#imageshow');
    const selectedImage = document.querySelector('#selectedImage');

    imageInput.addEventListener('change', function () {
        console.log("File selected!"); // Debugging statement

        if (this.files && this.files[0]) {
            const reader = new FileReader();

            reader.onload = function (e) {
                console.log("File loaded!"); // Debugging statement
                selectedImage.src = e.target.result;
                selectedImage.classList.remove('hidden');
            };

            reader.readAsDataURL(this.files[0]);
        } else {
            console.log("No file selected!"); // Debugging statement
            selectedImage.src = '';
            selectedImage.classList.add('hidden');
        }
    });
});


function lol(){
    console.log("please")
}