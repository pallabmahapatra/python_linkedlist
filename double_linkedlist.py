
class Node:
    '''
    each object of this class has three memory chambers: 
    prev: holds the address of previous node.
    next : hold the address of next node.
    data: holds the data itself.
    '''
    def __init__(self,data,prev,next):
        self.prev = prev
        self.data = data
        self.next = next


class Dlist:
    def __init__(self):
        self.head = None
        self.last = None
        self.total_nodes = None
    
    def create_list(self,n):
        '''
        creates n nodes of double liked list, takes n as argument
        '''
        
        for i in range(1,n+1):
            
            newnode = Node(data=i*10, prev=None, next=None)
            #print("value of i {}".format(i))
            if self.head == None:
                self.head = newnode
                self.last = newnode
                #print(f'new node created with id {id(newnnode)} \n newnode data {newnnode.data}')
            elif self.head != None:
                cursor = self.head
                while(cursor.next != None):
                    cursor = cursor.next
                cursor.next = newnode
                newnode.prev = cursor
                self.last = newnode
                del cursor
            else:
                print("something went wrong.....")



    def front_traverse(self):
        print("forward walk....")
        cursor = self.head
        while(cursor != None):
           print(cursor.data)
           cursor = cursor.next
        

    def back_traverse(self):
        print("backward walk ...")
        cursor = self.last
        while(cursor != None):
            print(cursor.data)
            cursor = cursor.prev
        del cursor

    def insert_at_n_position(self,position,data):
        '''
        inserts a new node at n position. this function takes position and data as arguments.
        '''
        cursor  = self.head
        newnode = Node(data=data,prev=None,next=None)
        if position == 1:
            newnode.next = cursor
            cursor.prev = newnode
            cursor = newnode
            self.head = cursor
            del cursor
        
        elif position != 1:
            count = 1
            while (count+1 < position):
                cursor = cursor.next
                count += 1
            newnode.next = cursor.next
            newnode.prev = cursor
            cursor.next = newnode
            del cursor
            
        else: print(f"{position} is a invalid postion...") 



if __name__ == '__main__':

    # create n nodes
    # n = input("Enter the number of nodes that you want to create: ")
    # n = int(n)
    n = 10

    obj_Dlist = Dlist()
    obj_Dlist.create_list(n)
    
    #obj_Dlist.back_traverse()
    obj_Dlist.insert_at_n_position(5,5555)
    obj_Dlist.front_traverse()