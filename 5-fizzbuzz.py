def fizzbuzz(n):
    if n%3==0 and n%5==0:
        return "FizzBuzz"
    else:
        if n%3==0:
            return "Fizz"
        if n%5==0:
            return "Buzz"
        else:
            return n
