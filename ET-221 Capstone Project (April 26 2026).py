class AnalysisStrategy:
    def analyze(self, readings):
        pass


class AverageStrategy(AnalysisStrategy):
    def analyze(self, readings):
        if len(readings) == 0:
            return 0
        return sum(readings) / len(readings)


class MaxStrategy(AnalysisStrategy):
    def analyze(self, readings):
        if len(readings) == 0:
            return 0
        return max(readings)
    
class MinStrategy(AnalysisStrategy):
    def analyze(self, readings):
        if len(readings) == 0:
            return 0
        return min(readings)

class SensorData:
    def __init__(self):
        self.readings = []

    def load_data(self, filename):
        try:
            file = open(filename, 'r')
            for line in file:
                self.readings.append(float(line.strip()))
            file.close()
        except:
            print("Error reading file")

    def run_analysis(self, strategy):
        return strategy.analyze(self.readings)


def main():
    print("Robot Sensor Data Analyzer")

    data = SensorData()
    filename = input("Enter file name: ")

    data.load_data(filename)

    average = data.run_analysis(AverageStrategy())
    maximum = data.run_analysis(MaxStrategy())
    minimum = data.run_analysis(MinStrategy())

    print("Average:", average)
    print("Max:", maximum)
    print("Min:", minimum)


if __name__ == "__main__":
    main()
