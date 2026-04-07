# import all the libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

Data={
    "DSA":['50','20','80','60','40'],
    "CGPA":['7.8','8.0','9.8','4.9','9.7'],
    "Aptitude":['20','80','70','60','50'],
    "Placed":['0','1','0','1','1']
}
self.df=pd.DataFrame(Data)
 
df=pd.DataFrame(Data)
X=df["DSA","CGPA","Apptitute"]
Y=df["Placed"]
self.model=RandomForestClassifier()

def predict_result(DSA,CGPA,Aptitude):
    result=self.model.predict([[DSA,CGPA,Aptitude]])
    if result[0]==0:
        text+="Low chance of placement\n\nSuggestions"
    if cgpa < 7.5:
        text+="improve cgpa\n"
    if dsa<200:
        text+="solve more dsa problems\n"
    if aptitude < 70:
        text+="practice apptitude text\n" 
    text+="Work on projects and communication\n "
    else:
text="High chance of placement\n\n Next Focus "
text += "Start mock interviews \n"
text += " improve resume \n"
text += " practice HR questions\n"
text += "Focus on company-specific coding rounds\n"

return text

























  