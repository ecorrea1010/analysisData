import pandas as pd
from sklearn.linear_model import LinearRegression

def getData():
    file = pd.read_csv('../files/data.csv')
    return file.dropna()

def filterData(file):
    return {
        'distance': list(file['distance']),
        'period': list(file['orbital_period']),
        'radius': list(file['radius_multiplier'])
    }

def nextData():
    numberOne = input('Enter a number one: ')
    numberTwo = input('Enter a number two: ')
    try:
        if not numberOne.isnumeric() and numberTwo.isnumeric():
            raise ValueError('Only numbers are allowed')
        predict = [[float(numberOne), float(numberTwo)]]
    except ValueError as ve:
        print(ve)
        predict = False
    return predict

def model(dependent, independent):
    predictionData = nextData()
    linearRegression = LinearRegression()
    linearRegression.fit(independent, dependent)
    print("Training")
    if predictionData:
        predictionModel = linearRegression.predict(predictionData)
        print("The prediction of the model is: ", predictionModel)
    else:
        print('No prediction was made')

def run():
    data = filterData(getData())
    distance = []
    for row in zip(data['distance'], data['period']):
        distance.append([row[0], row[1]])
    model(data['radius'], distance)


if __name__ == '__main__':
    run()
