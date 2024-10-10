# Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, 
# що користувач повинен мати можливість вказати рівень рекурсії.

import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("skyblue")
    window.title("Koch Curve")
    window.setup(width=800, height=800)

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()
    t.color("white")

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

# Виклик функції для введення користувачем рівня рекурсії
def main():
    while True:
        user_input = input("Введіть рівень рекурсії (число): ")

        if not user_input.isdigit():
            print("Будь ласка, введіть ціле число.")
            continue

        order = int(user_input)
        draw_koch_curve(order)

        break

if __name__ == "__main__":
    main()
