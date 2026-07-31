import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")

artist = turtle.Turtle()
artist.speed(0)
artist.width(2)

# 3. Dynamic color loop
iterations = 360
for i in range(iterations):
    # Calculate a unique fraction for Hue (moves smoothly from 0.0 to 1.0)
    hue = i / iterations
    
    # Convert HSV to RGB (Keep Full Saturation and Brightness at 1.0)
    rgb_color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    
    # Apply the color to our turtle pen
    artist.pencolor(rgb_color)
    
    # Move and turn to form the geometric design
    artist.forward(i * 1.5)
    artist.right(59)
turtle.done()
