from byotest_ci import *

usd_coins = {100 : 20, 50 : 20, 25 : 20, 10 : 20, 5 : 20, 1 :20}
eur_coins = {100 : 20, 50 : 20, 20 : 20, 10 : 20, 5 : 20, 2 : 20 , 1 : 20}

def get_change(amount, coins=eur_coins):
    
    change = []
    for coin in sorted(coins, reverse=True):
        
        while coin <= amount and coins[coin] > 0:
            amount -= coin
            change.append(coin)
            coins[coin] -= 1
    if  amount > 0:
        return "Impossible"
    return change        

test_are_equal(get_change(11, {5: 1, 1: 10}),[5,1,1,1,1,1,1])
test_are_equal(get_change(11, {5: 1, 1: 2}),"Impossible")

# coin = 5 and then while 1 time
# coin = 1 and then while 6 times
# if the there is a difference between the sum of the change and original amount return Impossibile
# coin = 5 and then while 2 times
# coin = 1 and then while 1 time

test_are_equal(get_change(0),[])
test_are_equal(get_change(1),[1])
test_are_equal(get_change(2),[2])
test_are_equal(get_change(5),[5])
test_are_equal(get_change(10),[10])
test_are_equal(get_change(20),[20])
test_are_equal(get_change(50),[50])
test_are_equal(get_change(100),[100])
test_are_equal(get_change(3),[2,1])
test_are_equal(get_change(7),[5,2])
test_are_equal(get_change(9),[5,2,2])
test_are_equal(get_change(35, usd_coins),[25,10])

print ("All test pass!")
