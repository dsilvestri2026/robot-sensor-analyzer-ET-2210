class AnalysisStrategy:
    """
    Base class for all analysis strategies.
    """

    def analyze(self, readings):
        pass


class OutlierStrategy(AnalysisStrategy):
    """
    Detects unusually high or invalid sensor readings.
    """

    def analyze(self, readings):
        outliers = []

        if len(readings) == 0:
            return outliers

        sorted_readings = sorted(readings)
        middle = len(sorted_readings) // 2

        # Find median
        if len(sorted_readings) % 2 == 0:
            median = (sorted_readings[middle - 1] + sorted_readings[middle]) / 2
        else:
            median = sorted_readings[middle]

        for value in readings:

            # Negative readings are automatically outliers
            if value < 0:
                outliers.append(value)

            # Extremely large readings are outliers
            elif value > median * 2.0:
                outliers.append(value)

        return outliers
    

class AverageStrategy(AnalysisStrategy):
    """
    Calculates the average sensor reading, filtering out outliers.
    """

    def analyze(self, readings):
        if len(readings) == 0:
            return 0

        outliers = OutlierStrategy().analyze(readings)

        filtered = []
        for value in readings:
            if value not in outliers:
                filtered.append(value)

        if len(filtered) == 0:
            return 0

        return sum(filtered) / len(filtered)


class MaxStrategy(AnalysisStrategy):
    """
    Finds the maximum sensor reading, filtering out outliers.
    """

    def analyze(self, readings):
        if len(readings) == 0:
            return 0

        outliers = OutlierStrategy().analyze(readings)

        filtered = []

        for value in readings:
            if value not in outliers:
                filtered.append(value)

        if len(filtered) == 0:
            return 0

        return max(filtered)
    
class MinStrategy(AnalysisStrategy):
    """
    Finds the minimum sensor reading, filtering out outliers.
    """

    def analyze(self, readings):
        if len(readings) == 0:
            return 0

        outliers = OutlierStrategy().analyze(readings)

        filtered = []

        for value in readings:
            if value not in outliers:
                filtered.append(value)

        if len(filtered) == 0:
            return 0

        return min(filtered)

    
class SensorData:
    """
    Stores and analyzes robot sensor readings.
    """

    def __init__(self):
        self.readings = []

    def load_data(self, filename):

        try:
            with open(filename, "r") as file:

                for line in file:
                    line = line.strip()

                    if line != "":
                        self.readings.append(float(line))

            return True

        except FileNotFoundError:
            print("\nError: File not found.")
            return False

        except ValueError:
            print("\nError: Invalid data detected in file.")
            return False

    def run_analysis(self, strategy):
        return strategy.analyze(self.readings)
    

def print_results(label, value):
    """
    Prints formatted analysis results.
    """

    if isinstance(value, float):
        print(f"{label:<20}: {value:.2f}")
    else:
        print(f"{label:<20}: {value}")


def main():

    print("================================")
    print("   Robot Sensor Data Analyzer")
    print("================================")

    data = SensorData()

    filename = input("\nEnter sensor data file: ")

    if data.load_data(filename):

        outliers = data.run_analysis(OutlierStrategy())
        average = data.run_analysis(AverageStrategy())
        maximum = data.run_analysis(MaxStrategy())
        minimum = data.run_analysis(MinStrategy())

        print("\nAnalysis Results")
        print("--------------------------------")

        print_results("Total Readings", len(data.readings))
        print_results("Average", average)
        print_results("Maximum", maximum)
        print_results("Minimum", minimum)
        print_results("Outliers", outliers)

        print("\nAnalysis complete.")


if __name__ == "__main__":
    main()