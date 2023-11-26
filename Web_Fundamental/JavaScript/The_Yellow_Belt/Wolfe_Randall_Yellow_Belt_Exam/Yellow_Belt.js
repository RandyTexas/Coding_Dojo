console.log("HI")

// This is to remove the Donate Button when clicked
function donate(element){
    let money = document.getElementById("help");
    money.remove();
}

function change(element){
    if(element.value == "Cat"){
        alert("You are looking at Cats!")
    }
    if(element.value == "Dog"){
        alert("You are looking at Dogs!")
    }
    if(element.value == "anyPet"){
        alert("You are looking at any Pets!")
    }
}


// This adds to the count for Pepper likes
let pepper = 3;
let pepper1 = document.getElementById("pepper");

function addpepper(element){
    console.log("Pepper")
    pepper++;
    pepper1.innerText = pepper + " petting(s)"
    console.log(pepper)
}

// This adds to the count for Bruce likes
let bruce = 3;
let bruce1 = document.getElementById("bruce");

function addBruce(element){
    console.log("Bruce")
    bruce++;
    bruce1.innerText = bruce + " petting(s)"
    console.log(bruce)
}

// This adds to the count for Oscar likes
let oscar = 8;
let oscar1 = document.getElementById("oscar");

function addOscar(element){
    console.log('Oscars')
    oscar++;
    oscar1.innerText = oscar + " petting(s)"
    console.log(oscar)
}