var inbox = document.getElementById("inbox")
var stattext = document.getElementById("stattext")
var input = document.getElementById("message")
var chatbox = document.getElementById("chatbox")
var stat = 0

document.getElementById("forbtn").addEventListener("click", ()=>{
    inbox.style.backgroundColor = "green";
    stattext.innerHTML = "You are FOR this topic"
    stat = 0
})
document.getElementById("agbtn").addEventListener("click", ()=>{
    inbox.style.backgroundColor = "tomato";
    stattext.innerHTML = "You are AGAINST this topic"
    stat = 1
})

input.addEventListener("keyup", (event)=>{
    if (event.keyCode === 13){
        var mess = input.value;
        if(mess){
            var inner = chatbox.innerHTML
            input.value = ""
            if(stat == 0){
                chatbox.innerHTML = "<div class='argument' style='color: white;word-wrap: break-word;margin: 2px;padding: 7px;border-radius: 10px;background-color: green; opacity: 0.7;'><p>"+mess+"</p></div>"+inner
            }
            else if(stat == 1){
                chatbox.innerHTML = "<div class='argument' style='color: white;word-wrap: break-word;margin: 2px;padding: 5px;border-radius: 10px;background-color: tomato;opacity: 0.7;'><p>"+mess+"</p></div>"+inner
            }
        }
        else{
            alert("Type message to participate")
        }
    }
})