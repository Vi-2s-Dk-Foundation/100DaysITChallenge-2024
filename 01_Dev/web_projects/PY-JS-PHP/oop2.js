
class Vehicle{
    constructor(brand, model, vin){
        this.brand = brand;
        this.model = model;
        this.#vin = vin; // Private property
    }

    getVin(){
        return this.#vin;
    }

    move(){ // Abstract method
        console.log('${this.brand} ${this.model} (VIN:${this.#vin}) is moving');
    }
}

class Car extends Vehicle{
    constructor(brand, model, color, vin){
        super(brand, model, vin);
        this.color = color;
    }

    move(){
        console.log('${this.brand} ${this.model} (VIN:${this.#vin}) is moving ON LAND!');
    }
}

class Boat extends Vehicle{
    move(){
        console.log('${this.brand} ${this.model} (VIN:${this.#vin}) is moving ON WATER!');
    }
}

// In Action

const myCar = new Car("Toyota", "Camry", "Blue", "12345");
const myBoat = new Boat("Yamaha", "WaveRunner", "09876");

myCar.move();
myBoat.move();