import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class PlacementBackend:
    def __init__(self):
        data = {
            "CGPA": [7.8, 8.0, 9.8, 4.9, 9.7],
            "DSA": [50, 20, 80, 60, 40],
            "Aptitude": [20, 80, 70, 60, 50],
            "Placed": [0, 1, 1, 0, 1]
        }

        self.df = pd.DataFrame(data)

        X = self.df[["CGPA", "DSA", "Aptitude"]]
        y = self.df["Placed"]

        self.model = RandomForestClassifier()
        self.model.fit(X, y)

    def predict_result(self, cgpa, dsa, aptitude):
        result = self.model.predict([[cgpa, dsa, aptitude]])

        text = ""

        if result[0] == 0:
            text += "Low chance of placement\n\nSuggestions:\n"

            if cgpa < 7.5:
                text += "- Improve CGPA\n"
            if dsa < 50:
                text += "- Solve more DSA problems\n"
            if aptitude < 70:
                text += "- Practice aptitude questions\n"

            text += "- Work on projects and communication"

        else:
            text = "High chance of placement\n\nNext Focus:\n"
            text += "- Start mock interviews\n"
            text += "- Improve resume\n"
            text += "- Practice HR questions\n"
            text += "- Focus on company coding rounds"

        return text