swimming_time = float(input("Enter the swimming time:"))
cycling_time = float(input("Enter the cycling time:"))
running_time = float(input("Enter the running time:"))

total_time = swimming_time + cycling_time + running_time

if total_time <= 100:
    print("You receive provincial colours.")
elif total_time <= 105:
    print("You receive provincial half colours.")
elif total_time <= 110:
    print("You receive provincial scroll.")
else:
    print("You receive no award.")

print(total_time)
