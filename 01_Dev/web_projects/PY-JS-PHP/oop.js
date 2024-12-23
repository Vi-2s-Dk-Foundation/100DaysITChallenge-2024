// constructor and this keywords used

class Dog{
    constructor(name, breed){
        this.name = name;
        this.breed = breed;
    } //end constructor

    bark(){
        console.log("Woof! I'm " + this.name + "the "+ this.breed + ". ")
    } //end bark
} //end class

const myDog = new Dog("Bingo", "German Shepherd")
myDog.bark();

// Another class

class Car{
    constructor(color, model){
        this.color = color;
        this.model = model;
    } //end constructor

    start_car(){
        console.log("Starting...")
    }

    stop_car(){
        console.log("Stopping...")
    }
}

const myCar = new Car("red", "BMW");
myCar.start_car();
myCar.stop_car();