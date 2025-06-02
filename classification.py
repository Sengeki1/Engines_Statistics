from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

class Classifier:
    def __init__(self, input, output):
        self.input_train, self.input_test, self.output_train, self.output_test = train_test_split(
            input, 
            output, 
            train_size=0.6, 
            test_size=0.4
            )
        self.rf = make_pipeline(
            OneHotEncoder(handle_unknown="ignore"),
            RandomForestClassifier()
        )
        self.output_predict = []

    def train(self):
        self.rf.fit(self.input_train, self.output_train)

    def predict(self):
        self.output_predict = self.rf.predict(self.input_test)

        counter_unity = 0
        counter_unreal = 0
        for i in range(len(self.output_predict)):
            if (self.output_predict[i] == "Unity"): counter_unity += 1
            else: counter_unreal += 1
        
        text = "In the Next few Years the Dominante Game Engine will be"
        if (counter_unity > counter_unreal):
            print(f"{text} Unity.")
        else: print(f"{text} Unreal.")

    def accuracy(self):
        print(f"{accuracy_score(self.output_test, self.output_predict) * 100}% accuracy score.")