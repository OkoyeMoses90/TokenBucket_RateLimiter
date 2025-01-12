import time

class TokenBucket:
    def __init__ (self, capacity, refillRate):

        """
        Initialize the token bucket
        :param capacity: Maximum number of token the nucket can hold
        :param refillRate: Number of tokens added every second
        """
        self.capacity = capacity #Max capacity of the bucket
        self.tokens = capacity #Current number of tokens in the bucket
        self.refillRate = refillRate #Tokens to be added to the bucket per second
        self.lastRefillTime = time.time() #Time of last refill
    
    def refill(self):
        #Refill the bucket based on elapsed time
        currentTime = time.time()
        elapsedTime = currentTime - self.lastRefillTime
        addedTokens = elapsedTime * self.refillRate
        self.tokens = min(self.capacity, self.tokens + addedTokens) #Ensure max capacity
        self.lastRefillTime = currentTime

    
    def processRequest(self, tokensNeeded = 1):
        self.refill()
        if self.tokens >= tokensNeeded:
            self.tokens -= tokensNeeded
            return True
        return False

if __name__ == "__main__":
    bucket = TokenBucket(capacity = 10, refillRate = 5)
    while True:
        canProcess = bucket.processRequest(tokensNeeded = 1)
        if canProcess:
            print("Request allowed")
        else:
            print("Can't process request")
        time.sleep(0.1)


    

