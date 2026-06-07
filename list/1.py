'''
You are provided with a list of daily temperature readings. An "anomaly" is defined as a temperature that is 
strictly greater than the average of the 3 days immediately preceding it and the 3 days immediately following it. 
Q : Write a function find_anomalies(temps) that returns a list of tuples containing (index, temperature) for every 
anomaly found. temps = [20, 22, 21, 24, 35, 23, 22, 24, 25, 20, 19, 30, 21, 22, 20]
Output: [(4, 35), (11, 30)]
'''

temps = [20, 22, 21, 24, 35, 23, 22, 24, 25, 20, 19, 30, 21, 22, 20]

