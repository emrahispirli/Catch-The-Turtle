import turtle
import random

# Ekranı ayarla
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title("Catch The Turtle")

# Kaplumbağa nesnesi
t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()
t.speed(0)

# Skor değişkeni
score = 0

# Skoru gösteren yazı
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(-150, 150)
pen.write(f"Skor: {score}", align="left", font=("Arial", 16, "bold"))

# Sayaç değişkeni
geriSayımSayacı = 15

# Sayaç yazısı
sayac = turtle.Turtle()
sayac.hideturtle()
sayac.color("white")
sayac.penup()
sayac.goto(150, 150)
sayac.write(f"Süre: {geriSayımSayacı}", align="left", font=("Arial", 16, "bold"))

# Kaplumbağayı rastgele bir noktaya taşı
def move_turtle():
    if geriSayımSayacı > 0:  # Süre bitmediyse devam et
        x = random.randint(-250, 250)
        y = random.randint(-150, 150)
        t.goto(x, y)
        screen.ontimer(move_turtle, 1000)  # Her 1 saniyede bir yer değiştir

# Tıklanınca skoru artır
def increase_score(x, y):
    global score
    if geriSayımSayacı > 0:  # Sadece süre bitmeden skor artırılsın
        score += 1
        pen.clear()
        pen.write(f"Skor: {score}", align="left", font=("Arial", 16, "bold"))

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
        t.hideturtle()  # Süre bitince kaplumbağa kaybolur

# Oyun başlangıcı
t.onclick(increase_score)  # Kaplumbağaya tıklanınca skoru artır
move_turtle()  # Kaplumbağayı rastgele hareket ettir
countdown()  # Geri sayımı başlat

# Pencereyi açık tut
screen.mainloop()
