from rest_client import get_number, post_list, get_prime_set,post_divisor, post_set_checked
from big_math import is_prime,primes_till
from math import sqrt


def main():
    # n = get_number()
    # print is_prime(n)
    # print int(sqrt(n))
    # print post_number(198633430462262799518572423085184617894807243284012597667430400)
    # print post_list(get_sieve_list(n,till=1000))
    # print primes_till(198633430462262799518572423085184617894807243284012597667430400)

    n = 15116439142247041
    test_number = 2

    for set_number in range(1,4):
        prime_set = get_prime_set(set_number)

        found = False
        for i in prime_set:
            if n%i == 0:
                post_divisor(test_number=test_number,divisor=i)
                print "Divisor "+str(i) +" found for n= "+str(n)
                found = True
                break

        if not found:
            post_set_checked(test_number=test_number,set_number=set_number)
            print "Set "+str(set_number)+" Checked"


if __name__ == '__main__':
    main()
