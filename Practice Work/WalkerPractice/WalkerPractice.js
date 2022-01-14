var w;
let c;

function setup() {
  createCanvas(640, 360);
  // Make a Walker object
  w = new Walker();
}

function draw() {
  background(51);
  // Update and display object
  w.update();
  w.display();
}

function Walker() {

  // Start Walker in center
  this.pos = createVector(width / 2, height / 2);

  this.update = function() {
    // Move Walker randomly
    var vel = createVector(random(-5, 5), random(-5, 5));
    this.pos.add(vel);
    
    //colour generator uses randomGaussian() to generate values close to one another
    //ref: https://p5js.org/reference/#/p5/randomGaussian, https://p5js.org/reference/#/p5/color
   for (let y = 0; y < 100; y++) {
  let x = randomGaussian(355, 355);
 c = color(x, y, x);
}
    
  }

  this.display = function() {
    // Draw Walker as circle
    fill(c);
    ellipse(this.pos.x, this.pos.y, 48, 48);
  }
}
