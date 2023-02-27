import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def getData():
    file = pd.read_csv('files/logicalRegression.csv')
    return file.dropna()

def processData(file):
    independent = []
    clumpThickness = list(file['ClumpThickness'])
    uniformityofCellSize = list(file['UniformityofCellSize'])
    uniformityofCellShape = list(file['UniformityofCellShape'])
    marginalAdhesion = list(file['MarginalAdhesion'])
    singleEpithelialCellSize = list(file['SingleEpithelialCellSize'])
    bareNuclei = list(file['BareNuclei'])
    blandChromatin = list(file['BlandChromatin'])
    normalNucleoli = list(file['NormalNucleoli'])
    mitoses = list(file['Mitoses'])
    dependent = list(file['Class'])
    for row in zip(
            clumpThickness,
            uniformityofCellSize,
            uniformityofCellShape,
            marginalAdhesion,
            singleEpithelialCellSize,
            bareNuclei,
            blandChromatin,
            normalNucleoli,
            mitoses
        ):
        independent.append([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]])
    return {
        'independent': independent,
        'dependent': dependent
    }

def separateData(data):
    independentTraining, independentTest, dependentTraining, dependentTest = train_test_split(data['independent'], data['dependent'], test_size = 0.20, random_state = 7)
    return {
        'independentTraining': independentTraining,
        'independentTest': independentTest,
        'dependentTraining': dependentTraining,
        'dependentTest': dependentTest
    }

def model(data):
    logicalRegression = LogisticRegression()
    logicalRegression.fit(data['independentTraining'], data['dependentTraining'])
    prediction = logicalRegression.predict(data['independentTest'])
    accuracy = accuracy_score(data['dependentTest'], prediction)
    return {
        'prediction': prediction,
        'accuracy': accuracy
    }

def setMessages(dataModel):
    message = 'The model prediction is \n' + str(dataModel['prediction'])
    message += '\n'
    accuracyRound = round(dataModel['accuracy'], 2)
    effectiveness = accuracyRound * 100
    message += 'The efficiency of the model was: ' + str(effectiveness) + '%'
    print(message)
    

def run():
    print('Welcome to Logical Regression')
    data = processData(getData())
    separate = separateData(data)
    dataModel = model(separate)
    setMessages(dataModel)

if __name__ == '__main__':
    run()