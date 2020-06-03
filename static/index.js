



document.addEventListener("DOMContentLoaded",() =>{
    var messages = [];
    if(!localStorage.getItem('messages'))
    localStorage.setItem('messages',messages);
    var socket= io.connect(location.protocol + "//"+ document.domain +":"+ location.port);
    const ul = document.getElementById("#messages");
    for (i=0,i<= messages.length -1;i++){
    const li = document.createElement('li');
    li.innerHTML= messages[i];
    ul.appendChild(li);
    };


    document.querySelector("#send").onClick = () => {
    var message = document.querySelector('message').innerHTML;
    messages.push(message);

    localStorage.setItem('messages',messages)

    socket.emit("Send message", {'message' :message});
    };




    };





});