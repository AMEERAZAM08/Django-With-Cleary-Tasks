from fastapi import FastAPI
import uvicorn
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
from pydantic import BaseModel
import  time
# Creating FastAPI instance
app = FastAPI()
# Creating class to define the request body
# and the type hints of each attribute

class request_body(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float
 
# Loading Iris Dataset
iris = load_iris()
 
# Getting our Features and Targets
X = iris.data
Y = iris.target
 
# Creating and Fitting our Model
clf = GaussianNB()
clf.fit(X,Y)
 
# Creating an Endpoint to receive the data
# to make prediction on.
def predict(sepal_length,sepal_width,petal_length,petal_width):
    # Making the data in a form suitable for prediction
    test_data = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width

    ]]
    print(test_data)
    # Predicting the Class
    class_idx = clf.predict(test_data)[0]
    time.sleep(5)
    # Return the Result
    return { 'class' : iris.target_names[class_idx]}