###-----------------LIST QUESTION------------------------###
'''
Consider a list (list = []). You can perform the following commands:

1.insert i e: Insert integer  at position .
2.print: Print the list.
3.remove e: Delete the first occurrence of integer .
4.append e: Insert integer  at the end of the list.
5.sort: Sort the list.
6.pop: Pop the last element from the list.
7.reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''

# code
if __name__=='__main__':
    n=int(input())
    lst=[]
    for _ in range(n):
        s=input('enter opereation and according wise element').split()
        command=s[0]
        values=s[1:]
        if command != 'print':
            command += '(' + ','.join(values) + ')' #concating values of command eg.command = command(value1,value2,value3...)
                #eval(expression, globals, locals)
            '''The eval() function evaluates the specified expression, if the expression is a legal Python statement,
                it will be executed.

               eval(expression, globals, locals)
            Parameter	Description
            expression	A String, that will be evaluated as Python code
            globals	Optional. A dictionary containing global parameters
            locals	Optional. A dictionary containing local parameters'''
            eval('lst.'+command)#eval function works with string so list lst concatting with command value
        else:
            print(lst)#printing list
