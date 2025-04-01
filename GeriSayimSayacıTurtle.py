import turtle
import random

# Ekranı ayarla
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Catch The Turtle")

# Sayaç değişkeni
geriSayımSayacı = 15

# Sayaç yazısı
sayac = turtle.Turtle()
sayac.hideturtle()
sayac.color("white")
sayac.penup()
sayac.goto(150, 150)
sayac.write(f"Süre: {geriSayımSayacı}", align="left", font=("Arial", 16, "bold"))


# Geri sayım fonksiyonu (sleep yerine ontimer kullanıldı)
def countdown():
    global geriSayımSayacı
    if geriSayımSayacı > 0:
        geriSayımSayacı -= 1
        sayac.clear()
        sayac.write(f"Süre: {geriSayımSayacı}", align="left", font=("Arial", 16, "bold"))
        screen.ontimer(countdown, 1000)
    else:
        sayac.clear()
        sayac.write("Süre Bitti!", align="left", font=("Arial", 16, "bold"))

countdown()  # Geri sayımı başlat

# Pencereyi açık tut
screen.mainloop()
