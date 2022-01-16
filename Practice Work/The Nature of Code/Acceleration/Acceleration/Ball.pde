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
    //
    
  }
  
  void update() {
   location.add(velocity); 
   velocity.add(acceleration);
   //add velocity to location, essentially making the ball move
   //creates a physics engine
   
  }
  void edges() {
   if (location.x > width) location.x = 0;
   if (location.x < 0 ) location.x = width;
   if (location.y > height) location.y = 0;
   if (location.y < 0) location.y = height;
  }
  
  void display() {
    stroke(0);
    strokeWeight(2);
    fill(127);
    ellipse(location.x, location.y, 48, 48);
    //draw the object at the updated location
  }
}
