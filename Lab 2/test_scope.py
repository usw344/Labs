#Id 11275853
#NSID Muhammad Usman Ahmed
## L02

import scope as scope

# test case 
inputs  = []
expected = []
reason = 'Empty list'

result = scope.find_duplicates(inputs)
if result != expected:
    print('Error in find_duplicates: expected', expected,
          'but obtained', result, '--', reason)


# test case 
inputs  = [1]
expected = []
reason = 'Singleton list'

result = scope.find_duplicates(inputs)
if result != expected:
    print('Error in find_duplicates: expected', expected,
          'but obtained', result, '--', reason)


# test case 
inputs  = [1, 1]
expected = [1]
reason = 'Simplest list with a duplicate'

result = scope.find_duplicates(inputs)
if result != expected:
    print('Error in find_duplicates: expected', expected,
          'but obtained', result, '--', reason)


# test case 
inputs  = [1, 2, 3]
expected = []
reason = 'Longer list with no duplicates'

result = scope.find_duplicates(inputs)
if result != expected:
    print('Error in find_duplicates: expected', expected,
          'but obtained', result, '--', reason)
          


##my test
#test case 3
inputs  = ["dog", "dog", 1,1]
expected = ["dog",1]
reason = 'Different data types'

result = scope.find_duplicates(inputs)
if result != expected:
    print('Error in find_duplicates: expected', expected,
          'but obtained', result, '--', reason)    

#test case 4
inputs  = [["dog", "dog"], [1,1],[1,1]]
expected = [[1,1]]
reason = 'Testing duplicates of lists'

result = scope.find_duplicates(inputs)
if result != expected:
    print('Error in find_duplicates: expected', expected,
          'but obtained', result, '--', reason)


#test case 1
inputs  = [1, 2, 3, 4, 6, 1]
expected = [1]
reason = 'Longer list with duplicates on the end'

result = scope.find_duplicates(inputs)
if result != expected:
    print('Error in find_duplicates: expected', expected,
          'but obtained', result, '--', reason)    

#test case 2
inputs  = [1,1,2,2,4,4,3,3]
expected = [1,2,4,3]
reason = 'Longer list with many duplicates not sorted'

result = scope.find_duplicates(inputs)
if result != expected:
    print('Error in find_duplicates: expected', expected,
          'but obtained', result, '--', reason)    

  


print('*** Test script finished ***')
