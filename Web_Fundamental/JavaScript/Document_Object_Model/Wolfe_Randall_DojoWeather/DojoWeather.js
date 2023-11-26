console.log("hello")

function changetemp(){
    let change = temp.value
    console.log(temp.value)
    // console("Thanks")
    if(change == "C" ){
        
        let conversion = document.querySelectorAll(".red")
        console.log(conversion)
        for (let i=0; i<conversion.length; i++){
            let dog = conversion[i].innerText
            console.log(dog)
            conversion[i].innerText = Math.round(5 / 9 * (dog - 32))
            // Math.round(9 / 5 * dog + 32);
        }
        let conversion1 = document.querySelectorAll(".blue")
        console.log(conversion1)
        for (let i=0; i<conversion1.length; i++){
            let dog = conversion1[i].innerText
            console.log(dog)
            conversion1[i].innerText = Math.round(5 / 9 * (dog - 32))
            // Math.round(9 / 5 * dog + 32);
        }
    }else{
        let conversion = document.querySelectorAll(".red")
        console.log(conversion)
        for (let i=0; i<conversion.length; i++){
            let dog = conversion[i].innerText
            console.log(dog)
            conversion[i].innerText = Math.round(9 / 5 * dog + 32);
            // Math.round(9 / 5 * dog + 32);
        }
        let conversion1 = document.querySelectorAll(".blue")
        console.log(conversion1)
        for (let i=0; i<conversion1.length; i++){
            let dog = conversion1[i].innerText
            console.log(dog)
            conversion1[i].innerText = Math.round(9 / 5 * dog + 32)
            // Math.round(9 / 5 * dog + 32);
        }
        console.log("Bye")
    }
}

function byecookie() {
    let cookieDiv = document.getElementById('cookie');
    cookieDiv.remove();
}

function burbank(){
    alert("loading weather report")
}
function chicago(){
    alert("loading weather report")
}
function dallas(){
    alert("loading weather report")
}

