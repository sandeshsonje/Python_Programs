result = ''         # we are taking result as varible
input_stmt = str(input('Enter string having not-bad'))
not_index = input_stmt.find('not')  #find not in string
if not_index != -1:              #if not is found in string
    bad_index = input_stmt.find('bad')  #find bad index in string
    if bad_index != -1 and bad_index > not_index:  #if bad is found and bad is after not
        result = input_stmt[:not_index]  # slicing till 'not'
        result += 'good'                 # replace with 'good'
        result += input_stmt[bad_index + 3:] #concat string with whatever remained
print(result)
