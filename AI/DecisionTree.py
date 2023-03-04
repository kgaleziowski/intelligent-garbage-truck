from sklearn.datasets import load_iris
from sklearn.tree import export_text
from sklearn.tree import DecisionTreeClassifier
import settings
import trash
import joblib

filename = 'DecisionTreeFiles/decisionTree.sav'
class DecisionTree():

    
    def __init__(self):
        self.labels = ['Day','Size','Weight','Bill','Closable','Space on Yard','Type','Time']
        self.decision_tree = joblib.load(filename)

    # Returns 0 or 1
    def make_decision(self, trash, trash_type):

        # Check if day is odd or even
        day = int((settings.current_day // 1) % 2)

        if (settings.current_day % 1) == 0:
            time_of_day = 0
        else:
            time_of_day = 1
            

        # Check if size of trash bin is okay
        if (trash.width <= 30 and trash.length <= 30 and trash.height <= 130):
            size = 1
        else:
            size = 0

        # Check if weight is okay
        if (trash.weight <= 80):
            weight = 1
        else:
            weight = 0

        # Check if bills were paid
        if (trash.bills_paid):
            bill = 1
        else:
            bill = 0

        # Check if bin was closed
        if (trash.bin_closed):
            can = 1
        else:
            can = 0

        # Check if specific trash yard is full
        if (settings.trash_capacity[trash_type] < settings.max_capacity):
            trash_yard = 1
        else:
            trash_yard = 0

        test_data_full = [[day, size, weight, bill, can, trash_yard, trash_type,time_of_day]]

        print("Test on: ")
        print(test_data_full)
        print("Decision:")
        print(self.decision_tree.predict(test_data_full)[0])
        return self.decision_tree.predict(test_data_full)[0]
    
    def print_tree(self):
        print(export_text(self.decision_tree, feature_names=self.labels))
