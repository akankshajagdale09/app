import turtle

def draw_art():
    # Setup window coordinates and background
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("#0D0D11")  # Deep spiritual dark background
    screen.title("Radha Krishna Pure Python Art")
    
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.hideturtle()
    
    # 1. DRAW BACKDROP GLOW (Sudarshan / Aura)
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.color("#FFD700")  # Metallic Gold
    t.width(1)
    for _ in range(36):
        t.circle(180)
        t.left(10)
        
    # 2. DRAW KRISHNA'S FLUTE (Bansuri)
    t.penup()
    t.goto(-180, -20)
    t.setheading(15)  # Tilt the flute slightly upward
    t.pendown()
    t.color("#D4AF37")  # Gold color
    t.begin_fill()
    for _ in range(2):
        t.forward(360)
        t.left(90)
        t.forward(12)
        t.left(90)
    t.end_fill()
    
    # Add holes to the flute
    t.color("#0D0D11")
    for i in range(5):
        t.penup()
        t.goto(-80 + (i * 45), -5)
        t.pendown()
        t.begin_fill()
        t.circle(4)
        t.end_fill()

    # 3. DRAW PEACOCK FEATHER (Mor Pankh)
    t.penup()
    t.goto(120, 20)
    t.setheading(60)
    t.pendown()
    
    # Feather Stem
    t.color("#228B22")  # Forest Green
    t.width(4)
    t.circle(100, 90)
    
    # Inner Eye of the Feather
    t.penup()
    t.goto(50, 140)
    t.pendown()
    t.color("#000080")  # Navy Blue
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
    t.color("#00FFFF")  # Cyan layer
    t.begin_fill()
    t.circle(12)
    t.end_fill()

    # 4. DRAW DIVINE SILHOUETTE PROFILES
    # Krishna Profile Outline
    t.penup()
    t.goto(-60, 150)
    t.setheading(-90)
    t.color("#00BFFF")  # Deep Sky Blue Silhouette
    t.width(5)
    t.pendown()
    t.circle(60, 45)   # Forehead
    t.circle(-15, 50)  # Nose bridge
    t.circle(15, 45)   # Nose tip
    t.forward(10)      # Nose base
    t.circle(-10, 90)  # Lips
    t.forward(15)      # Chin
    
    # Radha Profile Outline
    t.penup()
    t.goto(-110, 110)
    t.setheading(-85)
    t.color("#FF69B4")  # Hot Pink Silhouette
    t.width(5)
    t.pendown()
    t.circle(50, 40)   # Forehead
    t.circle(-12, 45)  # Nose bridge
    t.circle(12, 40)   # Nose tip
    t.forward(8)
    t.circle(-8, 90)   # Lips
    t.forward(12)      # Chin

    # Keep window active
    screen.exitonclick()

if __name__ == "__main__":
    draw_art()
