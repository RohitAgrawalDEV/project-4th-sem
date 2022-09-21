/* let likebtn = document.querySelector('#like-btn');
let dislikebtn = document.querySelector('#dislike-btn');
let input1 = document.querySelector('#input-1');
let input2 = document.querySelector('#input-2');


likebtn.addEventListener('click',()=>{
    input1.value = parseInt(input1.value) + 1;
    input1.style.color = "#12ff00";
})

dislikebtn.addEventListener('click',()=>{
    input2.value = parseInt(input2.value) + 1;
    input2.style.color = "#12ff00";
})

latest.addEventListener('click',()=>{
    latest.style.color =  "blue";
}) */



// JS code for report button

const openModalButtons = document.querySelectorAll('[data-modal-target]')
const closeModalButtons = document.querySelectorAll('[data-close-button]')
const overlay = document.getElementById('overlay')

openModalButtons.forEach(button => {
  button.addEventListener('click', () => {
    const modal = document.querySelector(button.dataset.modalTarget)
    openModal(modal)
  })
})

overlay.addEventListener('click', () => {
  const modals = document.querySelectorAll('#modal.active')
  modals.forEach(modal => {
    closeModal(modal)
  })
})

closeModalButtons.forEach(button => {
  button.addEventListener('click', () => {
    const modal = button.closest('#modal')
    closeModal(modal)
  })
})

function openModal(modal) {
  if (modal == null) return
  modal.classList.add('active')
  overlay.classList.add('active')
}

function closeModal(modal) {
  if (modal == null) return
  modal.classList.remove('active')
  overlay.classList.remove('active')
}

function show_Message(){
    alert("Your report has been successfully submitted!");
}