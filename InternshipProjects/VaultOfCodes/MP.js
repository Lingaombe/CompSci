 function name_data(){
    const names = document.getElementById("name");
    const name2 = document.getElementById("name2");
    name2.textContent = names.value;
 }
 
 function summary_data(){
    const summary = document.getElementById("summary");
    const summary1 = document.getElementById("summary1");
    const Summary = document.getElementById("Summary");

    Summary.textContent = "Personal Summary";
    summary1.textContent = summary.value;
 }

 function addedu(){
    const node = document.createElement("li");
    const adder = document.getElementById("Education");
    adder.textContent = "Education";

    let edu = document.getElementById("education");

    let text =  document.createTextNode(edu.value);
    node.appendChild(text);
    document.getElementById("education1").appendChild(node);
 }

 function addskill(){
    const node = document.createElement("li");
    const adder = document.getElementById("Skills");
    adder.textContent = "Skills";

    let skill = document.getElementById("skills");

    let text =  document.createTextNode(skill.value);
    node.appendChild(text);
    document.getElementById("skill1").appendChild(node);
    console.log("work");
 }

 function addexpo(){
    const node = document.createElement("li");
    const adder = document.getElementById("Experience");
    adder.textContent = "Experience";

    let experience = document.getElementById("experience");

    let text =  document.createTextNode(experience.value);
    node.appendChild(text);
    document.getElementById("experience1").appendChild(node);
 }

 function contact(){
    const adder = document.getElementById("Contact");
    adder.textContent = "Contact";

    let email1 = document.getElementById("email1");
    let phone1 = document.getElementById("phone1");
    let phone = document.getElementById("phone");
    let email = document.getElementById("email");

    email1.textContent = `Email: ${email.value}`;
    phone1.textContent = `Phone num: ${phone.value}`;

 }

 function Print(){
    let printContent = document.getElementById("output").innerHTML;
    let originalContent = document.body.innerHTML;
    document.body.innerHTML = printContent;
    window.print();
    document.body.innerHTML = originalContent;
}

function Clear(){
    document.getElementById("experience").value = null;
    document.getElementById("skills").value = null;
    document.getElementById("pic").value = null;
    document.getElementById("name").value = null;
    document.getElementById("email").value = null;
    document.getElementById("phone").value = null;
    document.getElementById("summary").value = null;
    document.getElementById("education").value = null;
    document.getElementById("output").textContent = " ";
}

function dispic(event){
    let image = document.getElementById("displayedImage");
    image.style.display = "block";
    image.src = URL.createObjectURL(event.target.files[0]);
}


