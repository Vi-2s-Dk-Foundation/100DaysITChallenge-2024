<?php   

// not input ot prompt
$age = readline("Enter your age:\n");

$ageInt = (int) age; 
// Cast from string to int

if($ageInt >= 18){
    //same as JavaScript
    echo "You are an adult!";
}
else{
    echo "You are NOT an adult...";
}

# Also works for comments
// Worthy of note... 
// use of switch statements

$dayEntry = (int) readline("Enter a day (1-7):\n");

switch($dayEntry){
    case 1:
        echo 'Monday';
        break;
    case 2:
        echo 'Tueday';
        break;
    case 3:
        echo 'Wednesday';
        break;
    case 4:
        echo 'Thursday';
        break;
    case 5:
        echo 'Friday';
        break;
    case 6:
        echo 'Saturday';
        break;
    case 7:
        echo 'Sunday';
        break;
    default:
        echo "Invalid Input!";

}
    

?>