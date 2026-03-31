import matplotlib.pyplot as plt
import turtle

# --------- AI MODEL ---------
def predict_water_intake(weight, temperature, activity_level):
    base = weight * 0.033
    
    if temperature > 30:
        base += 0.5
    if activity_level == "high":
        base += 0.7
    elif activity_level == "medium":
        base += 0.3
    
    return round(base, 2)

# --------- INPUT ---------
weight = float(input("Enter your weight (kg): "))
temperature = float(input("Enter temperature (°C): "))
activity = input("Activity level (low/medium/high): ").lower()

recommended = predict_water_intake(weight, temperature, activity)

print(f"\nRecommended water intake: {recommended} litres")

# --------- DATA ---------
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
intake = []

print("\nEnter water intake for last 5 days:")
for day in days:
    val = float(input(f"{day}: "))
    intake.append(val)

# --------- GRAPH ---------
plt.plot(days, intake, marker='o')
plt.axhline(y=recommended, linestyle='--')
plt.title("Water Intake Tracking")
plt.xlabel("Days")
plt.ylabel("Litres")
plt.show()

# --------- TURTLE ---------
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(1)

percentage = (intake[-1] / recommended) * 100

t.penup()
t.goto(-100, 0)
t.pendown()
t.write("Today's Progress", font=("Arial", 14, "bold"))

t.penup()
t.goto(-100, -50)
t.pendown()

for i in range(int(percentage)):
    t.forward(2)

t.penup()
t.goto(-100, -80)
t.write(f"{round(percentage,2)}% completed", font=("Arial", 12, "normal"))

turtle.done()