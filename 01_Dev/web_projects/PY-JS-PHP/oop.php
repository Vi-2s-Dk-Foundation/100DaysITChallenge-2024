<?php
// Uses public/private etc access modifiers

class Dog{
    public $name;
    public $breed;

    public function __construct($name, $breed){
        $this->name = $name;
        $this->breed = $breed;
    }
    public function bark(){
        echo "Woof! I'm ".$this->name." the ".$this->breed.".\n";
    } //end bark fxn
} //end class

# Create instance of class
$myDog = new Dog("Bingo", "German Shepherd");
$myDog.bark();

// Another

class Car{
    public $color;
    public $model;

    public function __construct($color, $model){
        $this->color = $color;
        $this->model = $model;
    }

    public function start_car(){
        echo "Starting...";
    }

    public function stopoing_car(){
        echo "Stoping...";
    }
}


?>

