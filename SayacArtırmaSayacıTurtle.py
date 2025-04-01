import turtle
import time

# Ekranı oluştur
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Geri Sayım")

# Yazıyı yazacak turtle
pen = turtle.Turtle()
#pen.shape("turtle")
pen.hideturtle()
pen.color("white")
pen.penup()


# Ekran boyutlarını al ve sol üst köşeye konumlandır
screen_width = screen.window_width()
screen_height = screen.window_height()
pen.goto(-150, 150)  # Sol üst köşe

# Sayaç
counter = 0
# Sayaç artırma fonksiyonu
def increase_counter(x,y):
    global counter  # Sayaç değişkenini global olarak kullanıyoruz
    counter += 1  # Sayaç 1 artar
    pen.clear()  # Önceki sayacı sil
    pen.goto(-150, 150) # Sol üst köşe
    pen.write(f"Sayaç: {counter}", align="center", font=("Arial", 30, "bold"))
# Ekranda herhangi bir yere tıkladığında increase_counter fonksiyonu çağrılır
screen.onclick(increase_counter)

# Pencereyi açık tut
screen.mainloop()
