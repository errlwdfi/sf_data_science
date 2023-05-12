import numpy as np

number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predict_number = int(input("Predict the number from 1 till 100 "))
    
    if predict_number > number:
        print("The number must be less.")

    elif predict_number < number:
        print("The number must be greater.")

    else:
        print(f"You've predict the number! The number is {number}, in {count} attempts")
        break