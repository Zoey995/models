import sqlflow_models
from tests.base import BaseTestCases

import tensorflow as tf
import numpy as np
np.random.seed(22)
import unittest


class TestRNNBasedTimeSeriesModel(BaseTestCases.BaseTest):
    def setUp(self):
        # We use sin data plus perturbation to simulate time series data
        time_series_data = np.sin(np.arange(56)) + np.random.normal(0, 0.01, 56)
        x = np.array(time_series_data).reshape(8, 7)
        y = np.array(np.arange(8).reshape(8, 1))
        self.features = {"col1": x}
        self.label = y
        self.n_in = 7
        self.n_out = 1
        # time_window=n_in, num_features=n_out
        feature_columns = [tf.feature_column.numeric_column(key, shape=(self.n_in, self.n_out)) for key in self.features]
        self.model = sqlflow_models.RNNBasedTimeSeriesModel(
            feature_columns=feature_columns, 
            stack_units=[50, 50], 
            n_in=self.n_in,
            n_out=self.n_out,
            model_type='rnn')
        self.model_class = sqlflow_models.RNNBasedTimeSeriesModel

class TestLSTMBasedTimeSeriesModel(BaseTestCases.BaseTest):
    def setUp(self):
        # We use sin data plus perturbation to simulate time series data
        time_series_data = np.sin(np.arange(56)) + np.random.normal(0, 0.01, 56)
        x = np.array(time_series_data).reshape(8, 7)
        y = np.array(np.arange(8).reshape(8, 1))
        self.features = {"col1": x}
        self.label = y
        self.n_in = 7
        self.n_out = 1
        # time_window=n_in, num_features=n_out
        feature_columns = [tf.feature_column.numeric_column(key, shape=(self.n_in, self.n_out)) for key in self.features]
        self.model = sqlflow_models.RNNBasedTimeSeriesModel(
            feature_columns=feature_columns, 
            stack_units=[50, 50], 
            n_in=self.n_in,
            n_out=self.n_out,
            model_type='lstm')
        self.model_class = sqlflow_models.RNNBasedTimeSeriesModel

class TestGRUBasedTimeSeriesModel(BaseTestCases.BaseTest):
    def setUp(self):
        # We use sin data plus perturbation to simulate time series data
        time_series_data = np.sin(np.arange(56)) + np.random.normal(0, 0.01, 56)
        x = np.array(time_series_data).reshape(8, 7)
        y = np.array(np.arange(8).reshape(8, 1))
        self.features = {"col1": x}
        self.label = y
        self.n_in = 7
        self.n_out = 1
        # time_window=n_in, num_features=n_out
        feature_columns = [tf.feature_column.numeric_column(key, shape=(self.n_in, self.n_out)) for key in self.features]
        self.model = sqlflow_models.RNNBasedTimeSeriesModel(
            feature_columns=feature_columns, 
            stack_units=[50, 50], 
            n_in=self.n_in,
            n_out=self.n_out,
            model_type='gru')
        self.model_class = sqlflow_models.RNNBasedTimeSeriesModel


if __name__ == '__main__':
    unittest.main()

