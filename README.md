Overview:
The Robot Sensor Data Analyzer is a Python program designed to read and analyze robot sensor data from a text file. The program loads sensor readings, detects outliers, and calculates statistical values such as average, maximum, and minimum readings. Outliers are excluded from the statistical calculations to improve the accuracy of the results.



Features:
Reads sensor data from a text file
Stores sensor readings in a list

Calculates:
Average reading
Maximum reading
Minimum reading

Detects outliers:
Ignores outliers during calculations
Handles invalid files and bad data
Includes automated unit tests using pytest



Design Concepts Demonstrated:
Object-Oriented Programming
The program uses classes such as:
SensorData
AverageStrategy
MaxStrategy
MinStrategy
OutlierStrategy
Strategy Pattern
Different analysis methods are separated into strategy classes, making the code easier to maintain and expand


Modular Design:
The program is divided into multiple functions and classes instead of one large block of code

Exception Handling:
The program handles:
Missing files
Invalid data
Empty input

Unit Testing:
Pytest is used to automatically test the functionality of the program.



Required Files:
sensor_analyzer.py
test_sensor_analyzer.py
data.txt (sample sensor data)

Optional Files:
test.txt
test2.txt
Any other added txt files.



How to Run the Program:
Open a terminal in the project folder and run:
python sensor_analyzer.py

When prompted, enter the sensor data file name:
data.txt (or whatever txt file you want to pull data from)



How to Run Unit Tests:
Run the following command in the terminal:
python -m pytest
