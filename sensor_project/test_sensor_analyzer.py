import pytest
from sensor_analyzer import (SensorData, AverageStrategy, MaxStrategy, MinStrategy, OutlierStrategy)


def test_sensor_data_starts_empty():
    data = SensorData()
    assert data.readings == []


def test_average_strategy_ignores_outliers():
    strategy = AverageStrategy()
    assert strategy.analyze([10, 20, 30, 100]) == 20


def test_average_strategy_ignores_negative_outliers():
    strategy = AverageStrategy()
    assert strategy.analyze([-10, 10, 20, 30]) == 20


def test_average_empty_list():
    strategy = AverageStrategy()
    assert strategy.analyze([]) == 0


def test_max_strategy_ignores_outliers():
    strategy = MaxStrategy()
    assert strategy.analyze([10, 20, 30, 100]) == 30


def test_max_strategy_ignores_negative_outliers():
    strategy = MaxStrategy()
    assert strategy.analyze([-10, 10, 20, 30]) == 30


def test_max_empty_list():
    strategy = MaxStrategy()
    assert strategy.analyze([]) == 0


def test_min_strategy_ignores_negative_outliers():
    strategy = MinStrategy()
    assert strategy.analyze([-10, 10, 20, 30]) == 10


def test_min_empty_list():
    strategy = MinStrategy()
    assert strategy.analyze([]) == 0


def test_outlier_strategy_high_values():
    strategy = OutlierStrategy()
    assert strategy.analyze([10, 20, 30, 100]) == [100]


def test_outlier_strategy_negative_values():
    strategy = OutlierStrategy()
    assert strategy.analyze([-10, 10, 20, 30]) == [-10]


def test_outlier_strategy_multiple_outliers():
    strategy = OutlierStrategy()
    assert strategy.analyze([42, 45, 50, -5, 150, 20000]) == [-5, 150, 20000]


def test_run_analysis_average():
    data = SensorData()
    data.readings = [10, 20, 30, 100]

    result = data.run_analysis(AverageStrategy())

    assert result == 20


def test_load_data_valid_file(tmp_path):
    test_file = tmp_path / "test_data.txt"
    test_file.write_text("10\n20\n30\n")

    data = SensorData()
    result = data.load_data(test_file)

    assert result == True
    assert data.readings == [10.0, 20.0, 30.0]


def test_load_data_invalid_file():
    data = SensorData()
    result = data.load_data("missing_file.txt")

    assert result == False