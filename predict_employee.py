import pickle
import numpy as np

# Load model
model = pickle.load(open("models/performance_model.pkl", "rb"))

def predict():
    print("\nEnter Employee Details:")

    age = int(input("Age: "))
    experience = int(input("Experience: "))
    salary = int(input("Salary: "))
    training_hours = int(input("Training Hours: "))
    attendance = int(input("Attendance (%): "))

    input_data = np.array([[age, experience, salary, training_hours, attendance]])

    prediction = model.predict(input_data)

    if prediction[0] == 0:
        print("\n🔴 Low Performer")
    elif prediction[0] == 1:
        print("\n🟡 Medium Performer")
    else:
        print("\n🟢 High Performer")

if __name__ == "__main__":
    predict()