def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def multiply_primes():
    total_product = 1
    found_prime = False

    while True:
        user_input = input().strip().lower()
        if user_input == 'n':
            break
        elif user_input == 'y':
            try:
                number = int(input())
                if number < 0:
                    print("NoProceed")
                    return
                if is_prime(number):
                    total_product *= number
                    found_prime = True
            except ValueError:
                print("NoProceed")
                return
        else:
            print("NoProceed")
            return

    if found_prime:
        print(total_product)
    else:
        print(1)

if __name__ == "__main__":
    multiply_primes()