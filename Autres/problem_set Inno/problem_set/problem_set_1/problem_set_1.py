# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently 
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold 
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which 
#    should be 10
#
# Your test function should run assertion checks and throw an 
# AssertionError for each of the 5 incorrect Queues. Pressing 
# submit will tell you how many you successfully catch so far.


from queue_test import *

def test():
    ###Your code here.
    
    #-1- reduce the value of a
    q = Queue(2)
    a = q.enqueue(999) 
    assert a 
    val = q.dequeue()
    assert val == 999
    
    #-2- enqueue i to q
    q = Queue(10)
    for i in range(9):
        a = q.enqueue(i) 
        assert a 
    
    #-3- check if q is empty
    q= Queue(10)
    a = q.dequeue()
    
    assert q.empty()
    
    
    
    
    #-4- dequeue q 
    q = Queue(11)
    for i in range(11):
        b = q.dequeue() 
        a = q.empty()
        assert a
        val = q.enqueue(i)
    
    # -5- enqueue 0
    q = Queue(5)
    for i in range(4):
        val = q.enqueue(i)
        assert val 
    a = q.full()
    assert a == False
    
test()

