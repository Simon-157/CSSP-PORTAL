let popup = document.querySelector(".popup")
let exitButton = document.querySelector(".close-btn")
let body_modal = document.querySelector(".body")

const Display = () => {
    popup.style.display = "block"
    body_modal.style.opacity = "0.6"
    body_modal.style.background = "rgba(240, 248, 255, 0.18)"
}
const Close = () => {
 popup.style.display = "none"
}

window.onclick = function(event) {
    if (event.target == popup) {
      popup.style.display = "none";
    }
  }

  

let popup2 = document.querySelector(".popup2")
let exitButton2 = document.querySelector(".close-btn2")
let body_modal2 = document.querySelector(".body")

const Display2 = () => {
popup2.style.display = "block"
body_modal2.style.opacity = "0.6"
body_modal2.style.background = "rgba(240, 248, 255, 0.18)"
}
const Close2 = () => {
popup2.style.display = "none"
}

window.onclick = function(event) {
    if (event.target == popup2) {
        popup2.style.display = "none";
    }
  }



