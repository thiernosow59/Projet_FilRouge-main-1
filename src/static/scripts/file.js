const reader = new FileReader();

let files = [];

const fileInput = document.querySelector("#fileInput")

const dropZone = document.querySelector("#drop")

const img = document.querySelector("img");

const dragOver = (event) => {
    event.preventDefault();
    event.stopPropagation();
    event.dataTransfer.dropEffect = 'copy';
}

const drop = (event) => {
    new Notification("Chargement de l'image");
    event.preventDefault();
    event.stopPropagation();
    console.log(event.dataTransfer.files)

    reader.readAsDataURL(event.dataTransfer.files[0])

}

const createImg = (src) => {
    let img = document.createElement('img');
    img.src = src;
    dropZone.appendChild(img)
}

dropZone.addEventListener("dragover", dragOver);
dropZone.addEventListener("drop", drop);

reader.addEventListener('load', ()=>{
    new Notification("L'image a été chargée");
    createImg(reader.result)
})