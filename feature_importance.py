import matplotlib.pyplot as plt
import pandas as pd

def plot_feature_importance(model, X):
    importance = model.feature_importances_

    feature_df = pd.DataFrame({
        "Feature": X.columns,
        "Importance": importance
    }).sort_values(by="Importance", ascending=False)

    print("\nFeature Importance:\n")
    print(feature_df)

    plt.figure(figsize=(8,5))
    plt.barh(feature_df["Feature"], feature_df["Importance"])
    plt.gca().invert_yaxis()
    plt.title("Feature Importance - Employee Performance")
    plt.show()