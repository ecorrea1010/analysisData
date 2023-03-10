Analysis of data

# Use python virtual environment
Create:
    Windows:
        py -m venv name_venv
    Unix:
        python3 -m venv name_venv

Activate:
    Windows:
        .\venv\Scripts\activate
    Unix:
        source venv/bin/activate

Deactivate:
    deactivate name_venv

# Use pip
After starting the python environment install the libraries:
pip install -r requirements.txt

# Start linear regression
To start the algorithm, run the following command
    Windows:
        py src/LinearRegression.py
    Unix:
        python3 src/LinearRegression.py

# Start logical regression
To start the algorithm, run the following command
    Windows:
        py src/LogicalRegression.py
    Unix:
        python3 src/LogicalRegression.py

# Start decision trees and classification
To start the algorithm, run the following command
    Windows:
        py src/DecisionTreeClassifier.py
    Unix:
        python3 src/DecisionTreeClassifier.py