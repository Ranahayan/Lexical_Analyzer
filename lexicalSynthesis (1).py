#!/usr/bin/env python
# coding: utf-8

# In[23]:

import csv
transition_table = list(csv.reader(open('C:/Users/haier/Desktop/Samesters/5th_Semester/CC/Lexical_analyzer/Transition_table_new_1.csv
')))

for lst in transition_table:
    for value in lst:
        state=value
        print(state,end=" ")
    print()    

ros_of_transition_table=len(transition_table);
cols_of_transition_table=len(transition_table[0])


# In[24]:


def is_token(token):
    present=0
    if token == '-1':
            return 0
    else:
        for num in range(ros_of_transition_table):
             if token == transition_table[num][1]:
                    present = 1 
                    return present 


# In[25]:


def check_ch(ch):
    to_returned=0
    if ch == ' ':
        to_returned = 'Space'
    elif ch >= 'A' and ch <= 'Z' or ch >= 'a' and ch <= 'z':
        to_returned = 'Letter'
    elif ch >= '0' and ch <= '9':
        to_returned = 'Digit'
    elif ch == '\t':
        to_returned = 'Tab'
    elif ch == '\n':
        to_returned = 'New line'
    else:
        to_returned = ch 
    return to_returned     


# In[26]:


def get_column_index(ch):
    not_present=0
    ch=check_ch(ch)
    for num in range(cols_of_transition_table):
        not_present+=1
        if ch == transition_table[0][num]:
            break  
    return not_present 


# In[27]:


tokans_list = []
no_of_char=0
with open("C:/Users/haier/Desktop/Samesters/5th_Semester/CC/Lexical_analyzer/lexical_input.txt") as f:
    line_no = 1
    tokan_no = 0
    for line in f:
        no_of_char += len(line)
        x = line.find("{")
        y = line.find("}")
        if x != -1 and y != -1:
            line=line[:x]+line[y+1:]
        line_no += 1
        line_length = len(line)
        back_pointer = 0
        forward_pointer = 0
        state = 0
        col = 0
        colon_no = 1
        lexeme = ""
        while forward_pointer < line_length:
            input_ch = line[forward_pointer]
            lexeme += input_ch
            col = get_column_index(input_ch)
            col -= 1
            state = transition_table[state+1][col]
            state = int(state)
            var2 = transition_table[state+1][1]
            var3 = transition_table[state+1][2]
            forward_pointer += 1
            if is_token(var2) == 1:
#                 print(var2,end=" ")
                if var3 == '-1':
                    forward_pointer -= 1
                    temp_len = len(lexeme)
                    lexeme = lexeme [:temp_len-1]
                    
                lexeme = lexeme.strip()
                tokan_no = transition_table[state+1][3]
#                 print(tokan_no,end=" ")
                tokans_list.append({'Lexeme':lexeme, 'Token_No':tokan_no, 'Token_Type':var2, 'Line_No':line_no, 'Column_No':colon_no})
                state = 0
                colon_no = forward_pointer+2
#                 print(lexeme)
                lexeme = ""
                


# In[33]:



class Node_to_add(object):
    def __init__(self, Value, Token_no):
        self.val = Value
        self.left_node = None
        self.right_node = None
        self.height = 1
        self.token_no = Token_no
class avl_tree(object):
    def get_height(self, root_node):
        if not root_node:
            return 0
        return root_node.height
 
    def get_balance(self, root_node):
        if not root_node:
            return 0
        return self.get_height(root_node.left_node) - self.get_height(root_node.right_node)
 
    def left_rotate(self, node):
        temp1 = node.right_node
        temp2 = temp1.left_node
        temp1.left_node = node
        node.right_node = temp2
        node.height = 1 + max(self.get_height(node.left_node),self.get_height(node.right_node))
        temp1.height = 1 + max(self.get_height(temp1.left_node),self.get_height(temp1.right_node))
        return temp1

    def right_rotate(self, node):
        temp3 = node.left_node
        temp4 = temp3.right_node
        temp3.right_node = node
        node.left_node = temp4
        node.height = 1 + max(self.get_height(node.left_node),self.get_height(node.right_node))
        temp3.height = 1 + max(self.get_height(temp3.left_node),self.get_height(temp3.right_node))
        return temp3

    def insert_node(self, root_node, Value, token_no):
        if not root_node:
            return Node_to_add(Value,token_no)
        elif Value < root_node.val:
            root_node.left_node = self.insert_node(root_node.left_node, Value, token_no)
        else:
            root_node.right_node = self.insert_node(root_node.right_node, Value, token_no)
        root_node.height = 1 + max(self.get_height(root_node.left_node),self.get_height(root_node.right_node))
        balance = self.get_balance(root_node)
        if balance > 1 and Value < root_node.left_node.val:
            return self.right_rotate(root_node)
        if balance < -1 and Value > root_node.right_node.val:
            return self.left_rotate(root_node)
        if balance > 1 and Value > root_node.left_node.val:
            root_node.left_node = self.left_rotate(root_node.left_node)
            return self.right_rotate(root_node)
        if balance < -1 and Value < root_node.right_node.val:
            root_node.right_node = self.right_rotate(root_node.right_node)
            return self.left_rotate(root_node)
        return root_node

    def pre_order_traversal(self, root_node):
        if not root_node:
            return
        print("{0} ".format(root_node.val)," " ,root_node.token_no, end="")
        self.pre_order_traversal(root_node.left_node)
        self.pre_order_traversal(root_node.right_node)

    def search_node(self,root_node, value, x):
        if root_node is None:
            return False
        elif root_node.val == value:
            tokans_list[x]['Token_No']=root_node.token_no
            return True
        elif root_node.val < value:
            return self.search_node(root_node.right_node, value, x)
        return self.search_node(root_node.left_node, value, x)
        return False

keyword_tree = avl_tree()
Root = None
 
Root = keyword_tree.insert_node(Root, 'AND', 121)
Root = keyword_tree.insert_node(Root, 'ARRAY', 122)
Root = keyword_tree.insert_node(Root, 'BEGIN', 123)
Root = keyword_tree.insert_node(Root, 'DIV', 124)
Root = keyword_tree.insert_node(Root, 'DO', 122)
Root = keyword_tree.insert_node(Root, 'ELSE', 126)
Root = keyword_tree.insert_node(Root, 'END', 127)
Root = keyword_tree.insert_node(Root, 'FUNCTION', 128)
Root = keyword_tree.insert_node(Root, 'IF', 129)
Root = keyword_tree.insert_node(Root, 'INTEGER', 130)
Root = keyword_tree.insert_node(Root, 'MOD', 131)
Root = keyword_tree.insert_node(Root, 'NOT', 132)
Root = keyword_tree.insert_node(Root, 'OF', 133)
Root = keyword_tree.insert_node(Root, 'OR', 134)
Root = keyword_tree.insert_node(Root, 'PROCEDURE',135)
Root = keyword_tree.insert_node(Root, 'PROGRAM', 136)
Root = keyword_tree.insert_node(Root, 'REAL', 137)
Root = keyword_tree.insert_node(Root, 'READLN',138)
Root = keyword_tree.insert_node(Root, 'THEN',139)
Root = keyword_tree.insert_node(Root, 'VAR', 140)
Root = keyword_tree.insert_node(Root, 'WHILE', 141)
Root = keyword_tree.insert_node(Root, 'WRITELN', 142)

for x in range(len(tokans_list)):
    if keyword_tree.search_node(Root,tokans_list[x]['Lexeme'], x) == True:
        tokans_list[x]['Token_Type'] = 'keyword'
    
# sir my output is complete but formatting of 
    
print("------------------------------------------------------------------------------------------")
print("{:<15} {:<15} {:<20} {:<15} {:<10}".format("Lexeme", 'Token No', 'Token Type', 'Line No', 'Column No'))
print("------------------------------------------------------------------------------------------")
for x in range(len(tokans_list)):
    print("{:<15} {:<15} {:<20} {:<15} {:<10}".format(tokans_list[x]['Lexeme'], tokans_list[x]['Token_No'],  tokans_list[x]['Token_Type'], tokans_list[x]['Line_No'], tokans_list[x]['Column_No']))

no_of_keyword=0
no_of_identifiers=0
for x in range(len(tokans_list)):
    if tokans_list[x]['Token_Type'] == 'keyword':
        no_of_keyword+=1
    elif tokans_list[x]['Token_Type'] == 'Identifier, ID':
        no_of_identifiers+=1

print("\n------------------------------------------------------------------------------------------")
print("No of tokens: ",len(tokans_list))
print("No of character processed: ",no_of_char)
print("No of Keyword: ",no_of_keyword)
print("No of Identifiers: ",no_of_identifiers)    


# In[29]:


no_of_keyword=0
no_of_identifiers=0
for x in range(len(tokans_list)):
    if tokans_list[x]['Token_Type'] == 'keyword':
        no_of_keyword+=1
    elif tokans_list[x]['Token_Type'] == 'Identifier, ID':
        no_of_identifiers+=1

print("No of tokens: ",len(tokans_list))
print("No of character processed: ",no_of_char)
print("No of Keyword: ",no_of_keyword)
print("No of Identifiers: ",no_of_identifiers)


# In[ ]:


# C:/Users/haier/Desktop/Samesters/5th_Semester/CC/Lexical_analyzer/Transition_table_new_1.csv
# C:/Users/haier/Downloads/Transition_table_new_1.csv

