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
 
  Mover() {
    
    location = new PVector(width/2, height/2);
    velocity = new PVector(0, 0);
    acceleration = new PVector(0, 0);
    //think of small quantities when accelerating
   
    
  }
  
  //Newton's 2nd Law (the beginning)
  
  void applyForce(PVector force) {
     acceleration.add(force); //force accumulation 
  }
  
  void update() {
   velocity.add(acceleration);
   location.add(velocity); 
   acceleration.mult(0); //clears out acceleration
   
   
   //add velocity to location, essentially making the ball move
   //creates a physics engine
    //velocity.limit(5);
    //constructs an artificial constraint; the velocity can never have a magnitutde greater than 5
    //limit is good to control the shape when it follows mouse PVector
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
    fill(127);
    ellipse(location.x, location.y, 48, 48);
    //draw the object at the updated location
  }
}
