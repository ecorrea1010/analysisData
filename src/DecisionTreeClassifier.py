import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def getData():
    file = pd.read_csv('files/HotelReservations.csv')
    return file.dropna()

def processData(fileData):
    independent = []
    numerOfAdults = list(fileData['no_of_adults'])
    numberOfChildren = list(fileData['no_of_children'])
    numberOfWeekendNight = list(fileData['no_of_weekend_nights'])
    numberOfWeekNights = list(fileData['no_of_week_nights'])
    dependent = list(fileData['required_car_parking_space'])
    for row in zip(numerOfAdults,numberOfChildren,numberOfWeekendNight,numberOfWeekNights):
        independent.append([row[0], row[1], row[2], row[3]])
    return {
        'independent': independent,
        'dependent': dependent
    }

def separateData(data):
    print('total data', len(data['independent']))
    independentTraining, independentTest, dependentTraining, dependentTest = train_test_split(data['independent'], data['dependent'], test_size = 0.20, random_state = 7)
    print('Amount of data for training', len(independentTraining))
    print('Amount of data for prediction', len(independentTest))
    return {
        'independentTraining': independentTraining,
        'independentTest': independentTest,
        'dependentTraining': dependentTraining,
        'dependentTest': dependentTest
    }

def model(data):
    decisionTreeClassifier = DecisionTreeClassifier()
    decisionTreeClassifier.fit(data['independentTraining'], data['dependentTraining'])
    print('Training!!!')
    prediction = decisionTreeClassifier.predict(data['independentTest'])
    accuracy = accuracy_score(data['dependentTest'], prediction)
    return {
        'prediction': prediction,
        'accuracy': accuracy
    }

def setModelMessages(data):
    message = 'The model prediction is \n' + str(data['prediction'])
    message += '\n'
    message += 'The total number of predictions was ' + str(len(data['prediction']))
    message += '\n'
    accuracyRound = round(data['accuracy'], 2)
    effectiveness = accuracyRound * 100
    message += 'The efficiency of the model was: ' + str(effectiveness) + '%'
    print(message)

def run():
    print('Welcome to decision trees and classification')
    data = processData(getData())
    separate = separateData(data)
    dataModel = model(separate)
    setModelMessages(dataModel)

if __name__ == '__main__':
    run()