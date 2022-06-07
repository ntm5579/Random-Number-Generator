import time

#returns a random float between 0 and 1
def randomNumber():
    t = time.time() #gets the number of seconds since the epoch of unix time (January 1st, 1970 at 00:00:00 UTC)
    r = float(t % 0.00000000000000000001 * 1000000000000000000000000) #shifts a part of the decimal in the timestamp that is equal to a fraction of a second
    r = r % 1 #truncates the beginning of the decimal
    
    #uses a truncated r to randomly delay the next number generation, allows more time to pass before next number generation
    time.sleep(r % 0.000001)
    return r

#returns a random float between integers rMin and rMax
def randomNumberMinMax(rMin:int, rMax:int):
    #throws an error if the given minimum value is greater than the given maximum value
    if(rMin > rMax):
        raise Exception("rMin must be less than the value of rMax")

    #uses the above function to generate a number between 0 and 1, applies range to that randomly generated number
    r = (randomNumber() * (rMax + 1 - rMin) + rMin)

    return r

if __name__ == "__main__":
    for _ in range(10):
        print(randomNumber())
    print("========================")
    for _ in range(10):
        print(randomNumberMinMax(1,10))