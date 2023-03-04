from sklearn.datasets import load_iris
from sklearn.tree import export_text
from sklearn.tree import DecisionTreeClassifier
import joblib

X1 = []
view = []
with open("DecisionTreeFiles/database.txt", 'r') as f:
    for line in f:
        line = line.strip()
        test_list = [int(i) for i in line]
        x = []
        if line[0] == "0":
            x.append("even")
        else:
            x.append("odd")
        if line[1] == "0":
            x.append("bad size")
        else:
            x.append("good size")
        if line[2] == "0":
            x.append("heavy")
        else:
            x.append("light")
        if line[3] == "0":
            x.append("not paid")
        else:
            x.append("paid")
        if line[4] == "0":
            x.append("cannot close bin")
        else:
            x.append("can close")
        if line[5] == "0":
            x.append("no space")
        else:
            x.append("free space")
        if line[6] == "0":
            x.append("paper")
        elif line[6] == "1":
            x.append("plastic")
        elif line[6] == "2":
            x.append("glass")
        else:
            x.append("mixed")
        if line[7] == "0":
            x.append("day")
        else:
            x.append("night")
        view.append(x)
        X1.append(test_list)

f = open("DecisionTreeFiles/learning_set.txt", "w")
for i in view:
    f.write(str(i)+"\n")
f.close()

Y1 = []
with open("DecisionTreeFiles/decissions.txt", 'r') as f:
    for line in f:
        line = line.strip()
        test = int(line)
        Y1.append(test)

dataset = X1
decision = Y1
labels = ['Day','Size','Weight','Bill','Closable','Space on Yard','Type','Time']
model = DecisionTreeClassifier(random_state=0, max_depth=20).fit(dataset, decision)
filename = 'DecisionTreeFiles/decisionTree.sav'
print("Model trained")
print("Decision tree:")
print(export_text(model, feature_names=labels))
joblib.dump(model, filename) 
    
