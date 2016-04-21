OPC opc;
PImage dot;

void setup()
{
  size(640, 360);

  // Load a sample image
  dot = loadImage("dot.png");

  // Connect to the local instance of fcserver
  opc = new OPC(this, "127.0.0.1", 7890);

  // Map an 8x8 grid of LEDs to the center of the window
  //opc.ledGrid(index, stripLength, numStrips, x, y, ledSpacing, stripSpacing, angle, zigzag)
  opc.ledGrid(0, 12, 4, width/2, height/2, width/12.0, height/4.0, 0, true);  
  
}

void draw()
{
  background(0);

  // Draw the image, centered at the mouse location
  float dotSize = height * 0.7;
  image(dot, mouseX - dotSize/2, mouseY - dotSize/2, dotSize, dotSize);
}

