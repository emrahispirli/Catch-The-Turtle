import turtle
import random
import time

# Ekranı oluştur
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Rastgele Hareket Eden Kaplumbağa")

# Yazıyı yazacak turtle
pen = turtle.Turtle()
pen.shape("turtle")
pen.color("green")
pen.penup()

# Ekranın boyutları
screen_width = screen.window_width()
screen_height = screen.window_height()

# Rastgele hareket fonksiyonu
def random_move():
    # Ekrandaki rastgele koordinatlara git
    x = random.randint(-screen_width // 2, screen_width // 2)
    y = random.randint(-screen_height // 2, screen_height // 2)
    pen.goto(x, y)  # Turtle'ı rastgele koordinata taşır
    screen.ontimer(random_move, 1000)  # 1 saniye sonra tekrar çağır

# İlk hareketi başlat
random_move()

# Pencereyi açık tut
screen.mainloop()
