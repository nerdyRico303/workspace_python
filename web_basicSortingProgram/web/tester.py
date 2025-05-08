import requests
import time

from tqdm import tqdm

# Target URL
url = 'http://127.0.0.1:5000'  

# Empty parameters
data = {'symbol': [], 'start_date': [], 'end_date': []}
# Initialize total response time
total_response_time = 0

# Send 100 POST requests
for i in range(100):
    start_time = time.time()  # Record the start time of the request
    response = requests.post(url, data=data)  # Send a POST request
    end_time = time.time()  # Record the end time of the request

    # Calculate the response time for a single request and accumulate it to the total response time
    total_response_time += (end_time - start_time)

    # Print the average response time
    print(f'{i}:Average Response Time: {total_response_time / (i+1):.4f} seconds')