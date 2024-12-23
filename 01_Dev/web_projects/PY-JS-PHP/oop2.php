<?php
# We use abstract keyword

abstract class Vehicle{
    protected $brand;
    protected $model;
    private $vin;

    public function __construct($brand, $model, $vin){
        $this->brand = $brand;
        $this->model = $model;
        $this->vin = $vin;
    }

    public function getVin(){
        return $this->vin;
    }

    abstract public function move();
} //end vehicle

class Car extends Vehicle{
    private $color;
    public function __construct($brand, $model, $vin){
        parent::__construct($brand, $model, $vin);
        $this->color = $color;
    }

    public function move(){
        echo "{$this->brand} {$this->model} (VIN: {$this->vin}) is moving ON LAND!\n";
    }
} //end car

class Boat extends Vehicle{
    public function move(){
        echo "{$this->brand} {$this->model} (VIN: {$this->vin}) is moving ON LAND!\n";
    }
} //end boat

# In Action

$myCar = new Car("Toyota", "Camry", "Blue", "12345");
$myBoat = new Boat("Yamaha", "WaveRunner", "09876");
?>