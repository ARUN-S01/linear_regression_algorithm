# CODED BY  ☞ﾟヮﾟ☞ ARUN ☜ﾟヮﾟ☜

import pandas as pd
from math import pow

def get_headers(dataframe):
    return dataframe.columns.values
def cal_mean(readings):
    readings_total = sum(readings)
    number_of_readings = len(readings)
    mean = readings_total/float(number_of_readings)
    return mean

def cal_variance(readings):
    readings_mean = cal_mean(readings)
    mean_difference_squared_readings = [pow((reading - readings_mean),2) for reading in readings]
    variance = sum(mean_difference_squared_readings)
    return variance / float(len(readings) - 1)

def cal_covariance(readings_1, readings_2):
    readings_1_mean = cal_mean(readings_1)
    readings_2_mean = cal_mean(readings_2)
    readings_size = len(readings_1)
    for i in xrange(0,readings_size):
        covariance += (readings_1[i] - readings_1_mean)*(readings_2[i] - readings_2_mean)
    return covariance / float(readings_size - 1)
def predict_target_value(x , w0 ,w1):
    return w0 + w1 *x

def cal_rmse(actual_readings, predicted_readings):
    square_error_total = 0.0
    total_readings = len(actual_readings)
    for i in xrange(0, total_readings):
        error = predicted_readings[i] - actual_readings[i]
        square_error_total += pow(error, 2)
    rmse = square_error_total / float(total_readings)
    return rmse

def cal_simple_linear_regression_coefficient(x_readings, y_readings):
    w1 = cal_covariance(x_readings, y_readings)/ float(cal_variance(x_readings))
    w0 = cal_mean(y_readings) - (w1*cal_mean(x_readings))
    return w0 , w1

def simple_linear_regression(dataset):
    #seperation
    dataset_headers = get_headers(dataset)
    print("dataset headers :" , dataset_headers)
    #mean calculation 
    square_feet_mean = cal_mean(dataset[dataset_headers[0]])
    price_mean = cal_mean(dataset[dataset_headers[1]])
    #variance calculation
    square_feet_variance = cal_variance(dataset[dataset_headers[0]])
    price_variance = cal_variance(dataset[dataset_headers[1]])
    #last calculation 
    covariance_of_price_and_square_feet = dataset.cov()[dataset_headers[0]][dataset_headers[1]]
    w1 = covariance_of_price_and_square_feet / float(square_feet_variance)
    w0 = price_mean - (w1* square_feet_mean)
    #print the output
    print(w1)
    print(w0)
    unknown = int(input("Enter the unkown value :"))
    y = w0 + w1 * float(unknown)
    print(y)


if __name__ == "__main__":
    pop = pd.read_csv("train.csv")
    simple_linear_regression(pop)

