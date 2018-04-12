import requests


# Ping the server. Get a URL to download the data set
def get_prime_set():

    # Get the URL
    URL = requests.get("http://volunteer-os.herokuapp.com/get_working_url")
    URL = URL.text[1:-2]  # exclude ending ""

    # Get the set_number. Embedded in URL itself
    set_number = [int(s) for s in URL.split('/') if s.isdigit()][0]

    # Download the dataset
    response = requests.get(URL)

    if response.status_code == 200:
        unsliced_string = response.text[1:-1]  # exclude ending ""
        sliced_string = unsliced_string.split(',')

        list_of_primes = map(int, sliced_string) # ONLY IN PYTHON 2
        return list_of_primes, set_number
    else:
        raise Exception("Invalid Prime Set Index:"+str(set_number))


# Ping the server. Update whether the given set has a divisor
# or not.
def post_divisor(divisor,set_number):

    # Prepare the JSON data to be posted
    # Divisor = -1 means no divisor
    data = "{\"divisor\":" + str(divisor) + ",\"set_number\":"+str(set_number)+"}"
    headers = {'Content-Type': "application/json"}
    response = requests.put("http://volunteer-os.herokuapp.com/update", data=data, headers=headers)

    if response.status_code == 200:
        return True
    else:
        return response.text
