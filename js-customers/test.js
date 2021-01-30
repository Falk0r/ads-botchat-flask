console.log("Welcome on Ads-chatBot");
const body = document.querySelector("body");

const bot_container = document.createElement("div");
bot_container.style.display = "flex";
bot_container.style.flexDirection = "column";
bot_container.style.position = "absolute";
bot_container.style.right = "10px";
bot_container.style.bottom = "10px";
bot_container.style.height = "200px";
bot_container.style.width = "200px";
bot_container.style.backgroundColor = "white";
bot_container.style.border = "1px solid black";
bot_container.style.borderRadius = "5px";
bot_container.style.zIndex = "9999999";


const chat_content = document.createElement('div');
chat_content.style.height = "150px";
chat_content.style.width = "190px";
chat_content.style.backgroundColor = "white";
chat_content.style.display = "block";
chat_content.style.position = "relative";
chat_content.style.marginTop = "5px";
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
content.innerHTML = "Offre Exclusive !!"
chat_content.appendChild(content);

{/* <div class="group-bouton" style="display: flex; justify-content: space-around; align-items: center;" ></div> */}
const group_button = document.createElement('div');
group_button.style.display = "flex";
group_button.style.justifyContent = "space-around";
group_button.style.alignItems = "center";
bot_container.appendChild(group_button);

{/* <button style="background-color: green; color: white; box-shadow: none; border: 1px solid green; height: 40px; width: 45%; border-radius: 5px;" >Voir plus</button> */}
const link = document.createElement('a');
link.href = "http://127.0.0.1:5000/";
link.style.width = "45%"
group_button.appendChild(link);

const button_more = document.createElement('button');
button_more.style.backgroundColor = "green";
button_more.style.color = "white";
button_more.style.boxShadow = "none";
button_more.style.border = "1px solid green";
button_more.style.height = "40px";
button_more.style.width = "100%";
button_more.style.borderRadius = "5px";
button_more.innerHTML = "Voir plus";
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










