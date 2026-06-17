import sys
from fastapi import FastAPI
import uvicorn
#import os

app = FastAPI()
#Define an App
#Instantiate - runs for a instance


@app.get("/") # This is to handle the root/homepage of the site
def root():
    return "The is the Root/Homepage"

@app.get("/add") # This is then exposed to the endusers IE: An endpoint
def add(x, y):
    return x + y

@app.get("/subtract")
def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
    return x ** y   


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=8000)
                
            

    #For local Python 
    """"operation = sys.argv[1]
    x = int(sys.argv[2])
    y = float(sys.argv[3])
    if operation == "add":
        #print(add(x, y))
        #to take the value from the add function results and print in text
        print(f"value={add(x, y)}")
        
    if operation == "subtract":
        #print(add(x, y))
        #to take the value from the add function results and print in text
        print(f"value={add(x, y)}")
    """

#x = 5
#y = 6
#print(add(x, y))


