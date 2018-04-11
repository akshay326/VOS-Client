import requests

BASE_URL = "https://volunteer-computing.firebaseio.com/primality-tests/"
number_url = BASE_URL + "test1/number/.json"
divisors_url = BASE_URL + "test1/sets_checked/.json"


def get_number():
    response = requests.get(number_url)
    n = int(response.text[1:-1])  # excluding ending "
    return n


def get_prime_set(i):
    response = requests.get(BASE_URL+"prime_sets/"+str(i)+"/set/.json")

    if response.status_code == 200:
        unsliced_string = response.text[1:-1]  # excluding ending "
        sliced_string = unsliced_string.split(',')
        n = map(int, sliced_string) # ONLY IN PYTHON 2
        return n
    else:
        raise Exception("Invalid Prime Set Index:"+str(i))


def post_divisor(test_number,divisor):
    data = "{\"found\":\"" + str(divisor) + "\"}"
    response = requests.put(BASE_URL+"test/"+str(test_number)+"/divisor.json" , data=data)

    if response.status_code == 200:
        return True
    else:
        return response.text


def post_number(n):
    n = "{\"0\":\"" + str(n) + "\"}"
    response = requests.put(divisors_url, data=n)
    return response.text


# NOTE We will have a sync problem here
def post_set_checked(test_number,set_number):

    # First get the latest sets
    response = requests.get(BASE_URL+"test/"+str(test_number)+"/sets_checked/set.json")

    if response.status_code != 200:
        raise Exception("get sets_checked failed: " + response.text)

    if response.content != "null":
        checked = response.text[1,-1]  # Remove surrounding "s
        # NOTE Checked may contain set_number - coz of the sync problem
        # But leaving the issue here
        checked += "," + str(set_number)
    else:
        checked = str(set_number)

    body = "{\"set\":\""+checked+"\"}"
    response = requests.put(BASE_URL+"test"+str(test_number)+"/sets_checked/.json", data=body)

    if response.status_code != 200:
        raise Exception("post set failed: "+response.text)


def post_list(l):
    body = "{"

    for i in range(len(l)):
        body += "\"" + str(i) + "\":\"" + str(l[i]) + "\""

        if i+1 is not len(l):
            body += ','
        else:
            body += '}'  # to avoid the last comma

    # print body

    response = requests.put(divisors_url, data=body)
    return response.text
