class Mover {
 PVector location;
 PVector velocity;
 //create an object with two vectors
 //location describes where it is
 //velocity describes the change in location over time
 
 PVector acceleration;
 //acceleration is any change in velocity-- can change magnitude or direction
 //we don't set velocity to anything directly
 //we don't set location to anything directly
 
 float mass;
 
  Mover() {
    
    location = new PVector(random(width), height/2);
    velocity = new PVector(0, 0);
    acceleration = new PVector(0, 0);
    //think of small quantities when accelerating
   mass = random(0.5, 4);
    
  }
  
  //Newton's 2nd Law with mass!
  
  void applyForce(PVector force) {
    PVector f = PVector.div(force,mass); //force divided by mass
    //the div ensures every PVector f giving to an object is individual; distributing copies of f so that different objects can do different things to it
    
     acceleration.add(f); //force accumulation  -- now with PVector f, it makes the smaller balls accelerate faster
  }
  
  void update() {
   velocity.add(acceleration);
   location.add(velocity); 
   acceleration.mult(0); //clears out acceleration
   
 
  }
  void checkEdges() {
    if (location.x > width) {
      location.x = width;
      velocity.x *= -1;
    } else if (location.x < 0) {
      velocity.x *= -1;
      location.x = 0;
    }
       if (location.y > height) {


//if the ball hits the edge, the velocity makes the ball go in the opposite direction, as if it bounced off it
      velocity.y *= -1;
      location.y = height;
    }
  }
  
  void display() {
   println(location.x, location.y);
    stroke(0);
    strokeWeight(2);
    fill(127, 100);
    ellipse(location.x, location.y, mass*20, mass*20);
    //draw the object at the updated location
  }
}
