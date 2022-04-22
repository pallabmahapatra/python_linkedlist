


class Node:
    '''
    Each object of this class has two members: data and next.
    Data holds the data.
    Next hold the next node's address.
    
    '''
    def __init__(self,data, next):
        self.data = data
        self.next = next

class List:
    '''
    1. stores all the operational function.
    2. head holds starting of the node.
    '''
    def __init__(self):
        self.head = None

    def display_all(self):
        cursor = self.head
        while(cursor != None):
            print(cursor.data)
            cursor = cursor.next
        del cursor
    
    def create_list(self,data):
        newnode = Node(data,None)
        if self.head == None:
            self.head = newnode
        else:
            cursor = self.head
            while( cursor.next != None ):
                cursor = cursor.next
            cursor.next = newnode
        
    def insert_front(self,data):
        newnode = Node(data, None)
        newnode.next = self.head
        self.head = newnode
    
    def insert_end(self,data):
        newnode = Node(data,None)
        cursor = self.head
        while(cursor.next != None):
            cursor = cursor.next
        cursor.next = newnode
        del newnode
    
    def insert_at_n_node(self,position,data):
        '''
          1. takes two arguments.
          2. arg1: position at which new data will be placed.
          3. arg2: data in that position.
        '''
        newnode = Node(data,None)
        cursor = self.head
        count = 1
        while( count+1 != position ):
            cursor = cursor.next
            count +=1
        newnode.next = cursor.next
        cursor.next = newnode
    
    def delete_node(self,position):
        '''

        deletes the nodes at nth position
        '''
        if position > 1:
            cursor = self.head
            count = 1
            while(count+1 < position):
                cursor = cursor.next
                count +=1
            temp = cursor.next
            cursor.next = cursor.next.next
            del temp
        
        if position == 1:
            cursor = self.head
            cursor = cursor.next
            self.head = cursor
            del cursor

        
        

    

if __name__ == '__main__':

    list1 = List()
    
    # creating linked list of ten nodes
    for i in range(1,11):
        list1.create_list(i*100)

    # connecting a new node at the begining    
    list1.insert_front(40)

    # connecitng a new node at the end
    list1.insert_end(555)

    # insert after nth node
    list1.insert_at_n_node(5,111)

# displays all the nodes
    print("all nodes before delete....")
    list1.display_all()

#delete a node by postion
    input()
    list1.delete_node(13)
    print("all nodes after delete...")
    list1.display_all()

