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
    #test to enqueue an element to q
    q = Queue(1)
    number_add = q.enqueue(1)
    assert number_add
    
    #test to dequeue q
    q = Queue(2)
    for i in range(2):
        enqueue_element = q.enqueue(i)
    for i in range(2):
        dequeue_element = q.dequeue()
        assert dequeue_element = i
    
    #check that q is full and not empty
    q = Queue(3)
    for i in range(3):
        enqueue_element = q.enqueue(i)
    assert q.full() and not q.empty()
    
    #check that q is empty and not full
    q = Queue(5)
    for i in range(5):
        enqueue_element = q.enqueue(i)
    for i in range(5):
        dequeue_element = q.dequeue()
    assert q.empty() and not q.full()
    
    #check that q is neither empty nor full
    q = Queue(4)
    enqueue_element = q.enqueue(660)
    assert not q.empty() and not q.full()
    
test()
    
    



