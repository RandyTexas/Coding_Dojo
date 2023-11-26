function howMuchLeftOverCake(numberOfPieces ,numberOfPeople){
    var LeftOver = numberOfPieces / numberOfPeople
    if(LeftOver <= 0){
        console.log("No leftovers for you!");  //if there aren't any leftovers 1
    }if(LeftOver >= 2){
        console.log("You have " + Math.round(LeftOver) +  " leftovers!");   //if there are 2 pieces of cake or less 0
    } if(LeftOver >= 3){
        console.log("You have leftovers to share")   //if there are 3 - 5 pieces of cake left over
    }
    if(LeftOver >= 5){
        console.log("Hold another party!")    //if there are more than 5 pieces of cake left over.
    }
    return LeftOver
} 
howMuchLeftOverCake(12, 5)



//5 People
//12 Pieces of cake
// 12/5 = 2.4 or 2 each and 2 left over 

// howMuchLeftOverCake
// numberOfPieces 

// I had to do some outside research on YouTube and Mdn to help me get this I remeber in the eailer lesson about math. and how you can use it to manupilate numbers