Mover m;

void setup() {
 size(640, 360);
 m = new Mover();
}

void draw() {
 background(255);
 
 PVector gravity = new PVector(0.0, 0.3);
m.applyForce(gravity);
 
 if(mousePressed) {
 PVector wind = new PVector(0.2, 0);
 m.applyForce(wind);
 }
 m.update();
 m.checkEdges();
 m.display();
  
  
}
