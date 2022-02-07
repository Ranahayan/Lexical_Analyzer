#!/usr/bin/env python
# coding: utf-8

# In[13]:


stack=[]

def push(item):
    stack.append(item)

def pop():
    item=stack.pop()
    return int(item)

def isInOperatorList(operator):
    if operator=='+' or operator=='-' or operator=='*' or operator=='/':
        return 1
    else:
        return 0

def solution(operation,input_number1,input_number2):
    if operation=='+':
        return input_number1+input_number2
    elif operation=='-':
        return input_number2-input_number1
    elif operation=='*':
        return input_number2*input_number1
    elif operation=='/':
        return int(input_number1/input_number2)

user_expression=input("Please enter a comma separated postfix expression like 2,3,+ :  ")
final_expression = user_expression.split(',')
print("input expression : ",final_expression)

for expr in final_expression:
    if expr.isdigit():
        push(expr)
    elif isInOperatorList(expr):
        number1=pop()
        number2=pop()
        ans=solution(expr,number2,number1)
        push(ans)
print("Answser = ",stack[-1])
        

