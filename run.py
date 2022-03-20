import constants as c
import helpers as h

def run():
    primes = h.calculate_primes(start=c.START, finish=c.FINISH)
    print(primes)

if __name__ == "__main__":
    run()