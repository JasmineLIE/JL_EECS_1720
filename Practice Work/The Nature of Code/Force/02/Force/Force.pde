Mover [] movers;

void setup() {
 size(640, 360);
 movers = new Mover[5];
 for (int i = 0; i < movers.length; i++) {
    movers[i] = new Mover(); 
 }
}

void draw() {
 background(255);
 
 for (Mover m : movers) { //enhanced loop; for every Mover m in the array movers, do this: basically made another instance from the array to use
 PVector gravity = new PVector(0.0, 0.3);
 gravity.mult(m.mass); //scaling gravity according to mass; though bigger balls are heavier, they fall at the same acceleration
 //but wind is not scalled according to mass-- a smaller object will blow faster against wind
m.applyForce(gravity);
 
 if(mousePressed) {
 PVector wind = new PVector(0.2, 0);
 m.applyForce(wind);
 
 }
 m.update();
 m.checkEdges();
 m.display();


}
}
