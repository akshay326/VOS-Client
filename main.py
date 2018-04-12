from rest_client import get_prime_set,post_divisor


def main():

    '''
    Leave This
    # n = get_number()
    # print is_prime(n)
    # print int(sqrt(n))
    # print post_list(get_sieve_list(n,till=1000))
    # print primes_till(198633430462262799518572423085184617894807243284012597667430400)
    '''

    # This is the prime number we are testing. Its same for all
    n = 15116439142247041

    # Keep on looping and checking
    while True:

        # The server decides which sets to be checked
        prime_set, set_number = get_prime_set()

        found = False
        for i in prime_set:
            if n%i == 0:
                post_divisor(divisor=i,set_number=set_number)
                print("Divisor "+str(i) +" found for n= "+str(n))
                found = True
                break

        if not found:
            post_divisor(divisor=-1,set_number=set_number)
            print("\nSet "+str(set_number)+" Checked")


if __name__ == '__main__':
    main()
