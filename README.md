# VOS Client
Try finding divisor of a number using simple division in python. A number is checked against a set of primes from the [Original list of primes](https://primes.utm.edu/lists/small/millions/). There are 40+ such sets. 

## Where's distributed computing in it?
Since brute force division using millions of divisors(upto 10 digits) takes a lot of time, so we distribute brute force division over a set of computers. Each node downloads a list of primes and tries division. If a factor is found, update the results, else repeat the division with a different set of primes.

## Database Structure
primality-tests:  
|-- prime_sets:  
|   |-- 1:  
|   |   |-- set: 2,3,5,....  
|   |-- 2:  
|   |   |-- set: 151321, 151323 .....  
|  
|-- test_count:2  
|  
|-- test*i*:  
|   |-- number:153816723933467683...  
|   |-- divisor: -1  
|   |-- sets_checked: "0,1,2,3,4,5,6"  
|  
|-- test*k*:  
|   |-- number:1414053247  
|   |-- divisor: 37517  
|   |-- sets_checked: "0,1"  

## REST API json end-points
+ Base URL: http://volunteer-os.herokuapp.com
+ URL to get the prime state: http://volunteer-os.herokuapp.com/get_state
+ URL to get working URL: http://volunteer-os.herokuapp.com/get_working_url
+ URL to update DB: http://volunteer-os.herokuapp.com/update
