PVector mouse, center;
void setup() {
 size(500, 300); 
}

void draw() {
background (255);
strokeWeight(2);
stroke(0);
noFill();

translate(width/2, height/2);
ellipse(0, 0, 4, 4);

PVector mouse = new PVector(mouseX, mouseY);
PVector center = new PVector(width/2, height/2);

mouse.sub(center);
mouse.mult(1);

//float m = mouse.mag(); //get the vector's length and store it into the variable 
//if the magnitude of the velocity is > 10, then it's going too fast

//fill(255, 0, 0);
//rect(0, 0, m, 20);


mouse.normalize();
mouse.mult(50);

//normalizing is useful since once you have length 1, you can scale it using multi to any length
//no matter where you move the mouse the length of the line will remain the same 

mouse.setMag(50); //Does what the two lines of code above do in all in one

line(0, 0, mouse.x, mouse.y);

}
