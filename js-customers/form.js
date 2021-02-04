console.log("Welcome on Ads-chatBot");
const body = document.querySelector("body");

const bot_container = document.createElement("div");
bot_container.style.display = "flex";
bot_container.style.flexDirection = "column";
bot_container.style.justifyContent = "center";
bot_container.style.position = "fixed";
bot_container.style.padding = "5px";
bot_container.style.right = "10px";
bot_container.style.bottom = "10px";
bot_container.style.overflow = "hidden";
bot_container.style.width = "50px";
bot_container.style.height = "50px";
bot_container.style.backgroundColor = "white";
bot_container.style.border = "1px solid black";
bot_container.style.borderRadius = "100%";
bot_container.style.zIndex = "9999999";
bot_container.style.transition = "width 1s linear"

const minimize = document.createElement('div');
minimize.style.display = 'flex';
minimize.style.height = '45px';
minimize.style.width = '45px';
minimize.style.margin = 'auto';
minimize.style.fontSize = "30px";
minimize.style.alignItems = "center";
minimize.style.justifyContent = "center";
minimize.style.cursor = "pointer";
minimize.style.borderRadius = "100%";

minimize.innerHTML = '⭐';
bot_container.appendChild(minimize);


const chat_content = document.createElement('div');
chat_content.style.maxHeight = "300px";
chat_content.style.width = "190px";
chat_content.style.overflow = "hidden";
chat_content.style.backgroundColor = "white";
chat_content.style.display = "none";
chat_content.style.position = "relative";
chat_content.style.marginTop = "5px";
chat_content.style.marginBottom = "5px";
chat_content.style.marginLeft = "5px";
chat_content.style.textAlign = "center";
bot_container.appendChild(chat_content);

{/* <img src="./test.jpg" style="object-fit: contain; height: 100px;"></img> */}
const img = document.createElement('img');
img.src="https://images-na.ssl-images-amazon.com/images/I/61c-sEkglwL._AC_SY355_.jpg";
img.style.objectFit = "contain";
img.style.height= "100px";
chat_content.appendChild(img);

{/* <p style="margin-top: auto; margin-bottom: auto;" >Offre exclusive !</p> */}
const content = document.createElement('p');
content.style.marginTop = "auto";
content.style.marginBottom = "auto";
content.innerHTML = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
chat_content.appendChild(content);

const form = document.createElement('form');
form.id = "form-ads-chatbot"
form.style.display = "flex";
form.style.flexDirection = "column";
form.style.margin = "5px";
form.style.height = "auto";
form.style.width = "auto";
chat_content.appendChild(form);

const inputName = document.createElement('input');
inputName.type = "text";
inputName.name = "name";
inputName.required = true;
inputName.style.marginTop = "5px";
inputName.style.width = "auto";
inputName.placeholder = "Votre nom";

form.appendChild(inputName);

const inputMail = document.createElement('input');
inputMail.type = "email";
inputMail.name = "email";
inputMail.required = true;
inputMail.style.marginTop = "5px";
inputMail.style.width = "auto";
inputMail.placeholder = "Votre e-mail";

form.appendChild(inputMail);

const inputPhone = document.createElement('input');
inputPhone.type = "phone";
inputPhone.name = "phone";
inputPhone.required = true;
inputPhone.pattern = "[0-9]{10}";
inputPhone.style.marginTop = "5px";
inputPhone.style.width = "auto";
inputPhone.placeholder = "Votre téléphone";

form.appendChild(inputPhone);

{/* <div class="group-bouton" style="display: flex; justify-content: space-around; align-items: center;" ></div> */}
const group_button = document.createElement('div');
group_button.style.display = "none";
group_button.style.justifyContent = "space-around";
group_button.style.alignItems = "center";
bot_container.appendChild(group_button);

{/* <button style="background-color: green; color: white; box-shadow: none; border: 1px solid green; height: 40px; width: 45%; border-radius: 5px;" >Voir plus</button> */}
const link = document.createElement('a');
link.href = "http://127.0.0.1:5000/";
link.style.width = "45%"
group_button.appendChild(link);

const button_more = document.createElement('button');
button_more.disabled = true;
button_more.style.backgroundColor = "gray";
button_more.style.cursor = "not-allowed"
button_more.style.color = "white";
button_more.style.boxShadow = "none";
button_more.style.border = "1px solid green";
button_more.style.height = "40px";
button_more.style.width = "100%";
button_more.style.borderRadius = "5px";
button_more.innerHTML = "Envoyer";
link.appendChild(button_more);

const button_close = document.createElement('button');
button_close.style.backgroundColor = "red";
button_close.style.color = "white";
button_close.style.boxShadow = "none";
button_close.style.border = "1px solid red";
button_close.style.height = "40px";
button_close.style.width = "45%";
button_close.style.borderRadius = "5px";
button_close.innerHTML = "Fermer";
button_close.id = "close-adbotchat";
group_button.appendChild(button_close);

body.appendChild(bot_container);

//STYLE HOVERS
button_more.addEventListener('mouseover',(e) => {
    button = e.target;
    button.style.opacity = '60%';
    button.style.cursor = 'pointer';
});
button_more.addEventListener( 'mouseleave' , (e) => {
    button = e.target;
    button.style.opacity = '100%';
})
button_close.addEventListener('mouseover', (e) => {
    button = e.target;
    button.style.opacity = '60%';
    button.style.cursor = 'pointer';
});
button_close.addEventListener( 'mouseleave' , (e) => {
    button = e.target;
    button.style.opacity = '100%';
});

//Close triggers
button_close.addEventListener('click', () =>{
    toMinimize();
})
minimize.addEventListener('click', ()=>{
    toExpense();
})
function toMinimize() {
    bot_container.style.transition = '';
    chat_content.style.display = 'none';
    group_button.style.display = 'none';
    bot_container.style.height = '50px';
    bot_container.style.width = '50px';
    bot_container.style.borderRadius = '100%';
    minimize.style.display = 'flex';
}
function toExpense() {
    bot_container.style.transition = "width 1s linear"
    chat_content.style.display = 'block';
    group_button.style.display = 'flex';
    bot_container.style.height = '';
    bot_container.style.width = '200px';
    bot_container.style.borderRadius = '5px';
    minimize.style.display = 'none';
}
//Timing Trigger
setTimeout(toExpense, 1000);

//form trigger
form.addEventListener('input', () => {
    const inputs = form.querySelectorAll('input');
    check = true;
    for (const input of inputs) {
        console.log(input.validity.valid);
        if (!input.validity.valid) {
            check = false;
            break;
        }
    }
    if (check) {
        button_more.disabled = false;
        button_more.style.backgroundColor = "green";
    } else {
        button_more.disabled = true;
        button_more.style.backgroundColor = "gray";
    }
})
//SEND FORM
button_more.addEventListener('click', (e)=>{
    e.preventDefault();    
})