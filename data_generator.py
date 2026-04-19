import pandas as pd
import numpy as np

def generate_data():
    np.random.seed(42)
    n = 1000

    df = pd.DataFrame({
        "age": np.random.randint(22, 60, n),
        "experience": np.random.randint(0, 35, n),
        "salary": np.random.randint(20000, 120000, n),
        "training_hours": np.random.randint(5, 100, n),
        "attendance": np.random.randint(50, 100, n)
    })

    df["performance_score"] = (
        df["experience"] * 0.3 +
        df["training_hours"] * 0.2 +
        df["attendance"] * 0.5
    )

    df["performance"] = pd.cut(
        df["performance_score"],
        bins=[0, 40, 70, 100],
        labels=["Low", "Medium", "High"]
    )

    df.to_csv("data/raw/employees.csv", index=False)
    print("Dataset created!")

if __name__ == "__main__":
    generate_data()