def setup():
    size(100, 100, P3D)


def draw():
    background(0);
    
    angle = mouseX * 0.01;
    c = cos(angle);  
    pushMatrix() 
    translate(width/2, height/2)
    rotate(c)
    rect(-26, -26, 52, 52)
    popMatrix();
    
    
    
