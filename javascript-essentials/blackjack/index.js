let firstCard = 10
let secondCard = 12

let sum = firstCard + secondCard

if (sum < 21) {
    console.log("do you want to draw a new card?")
} else if (sum === 21) {
    console.log("you win!")
} else {
    console.log("you're out!")
}