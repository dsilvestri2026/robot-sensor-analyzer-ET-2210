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
    

class OutlierStrategy(AnalysisStrategy):
    def analyze(self, readings):
        outliers = []

        if len(readings) == 0:
            return outliers

        average = sum(readings) / len(readings)

        for value in readings:
            if value > average * 1.5 or value < average * 0.5:
                outliers.append(value)

        return outliers

class SensorData:
    def __init__(self):
        self.readings = []

    def load_data(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    if line.strip() != "":
                        self.readings.append(float(line.strip()))
            return True

        except FileNotFoundError:
            print("Error: File not found.")
            return False

        except ValueError:
            print("Error: File contains invalid data.")
            return False

    def run_analysis(self, strategy):
        return strategy.analyze(self.readings)


def main():
    print("Robot Sensor Data Analyzer")
    print("--------------------------")

    data = SensorData()
    filename = input("Enter file name: ")

    if data.load_data(filename):
        average = data.run_analysis(AverageStrategy())
        maximum = data.run_analysis(MaxStrategy())
        minimum = data.run_analysis(MinStrategy())
        outliers = data.run_analysis(OutlierStrategy())

        print("\nAnalysis Results")
        print("----------------")
        print(f"Number of readings: {len(data.readings)}")
        print(f"Average reading: {average:.2f}")
        print(f"Maximum reading: {maximum:.2f}")
        print(f"Minimum reading: {minimum:.2f}")
        print(f"Outliers detected: {outliers}")


if __name__ == "__main__":
    main()