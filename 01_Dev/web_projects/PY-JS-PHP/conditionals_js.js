

let age = prompt("Enter your age:\n");
let ageInt = parseInt(age);

if(ageInt >= 18){
    // use curly braces
    console.log("You are an adult!");
}
else {
    console.log("You are NOT an adult...");
}


/*
Also remember, there are many operators

- Arithmetic
- Logical
- Comparison
- Assignment.

Remember differences 
&&, || vs and, or for python

Also 
=== vs == vs =

Comment below for questions!


Similar
*/

let dayEntry = parseInt(prompt("Enter a day (1-7):\n"));

switch(dayEntry){
    case 1:
        console.log('Monday');
        break;
    case 2:
        console.log('Tueday');
        break;
    case 3:
        console.log('Wednesday');
        break;
    case 4:
        console.log('Thursday');
        break;
    case 5:
        console.log('Friday');
        break;
    case 6:
        console.log('Saturday');
        break;
    case 7:
        console.log('Sunday');
        break;
    default:
        console.log("Invalid Input!");

}