class node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class linklist():

    def __init__(self):
        self.head=None

    def insertEnd(self,data):
        if self.head is None:
            self.head = node(data)
            print"self.head.data",self.head.data
            return
        curr =self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data)
        #print"self.head.data",self.head.data

    def insertBegin(self, data):
        #self.head = node(data, self.head)
        temp = node(data)
        temp.next = self.head
        self.head = temp

    def insertmid(self, data, index):
        if self.head is None:
            self.head = node(data)
            return
        curr = self.head
        i = 0
        #print"dfgh",curr.next.next.data 
        while curr.next:
            print"i:",i
            i+=1
            if i==index:
                temp = node(data)
                temp.next = curr.next
                curr.next = temp
                return
            curr = curr.next

    def deletemid(self,index):
        i=0
        curr= self.head
        while curr.next:
            i+=1
            if i==index:
                curr.next = curr.next.next
                return
            curr = curr.next

    def reverselst(self):
        p=[2, 1, 4, 3]
        curr = self.head
        prev = None
        while curr:
            nextnode = curr.next
            temp = curr
            curr.next = prev
            prev = temp
            curr = nextnode
        self.head = prev

    def printLinklist(self):
        nodes = []
        curr = self.head
        while curr:
           nodes.append(curr.data)
           curr = curr.next
        return nodes

lst=linklist()
while True:
    print"type 0 to exit"
    print"type 1 to display the linklist"
    print"type 2 for insert a node in the end of the linklist"
    print"type 3 for insert a node in the Beginning of the linklist"
    print"type 4 for insert a node in the kth position of the linklist"
    print"type 5 for delete a node from the kth position of the linklist"
    print"type 6 for to reverse the linklist"

    obtion = input("Enter the Obtions:")

    if obtion == 0:
        import sys
        sys.exit()
    if obtion == 1:
        print "lst: ",lst.printLinklist()
    if obtion == 2:
        nodeVal = input("Enter the Value of the nodes:")
        lst.insertEnd(nodeVal)
    if obtion == 3:
        nodeVal = input("Enter the Value of the nodes:")
        print "lst: ",lst.insertBegin(nodeVal)
    if obtion == 4:
        nodeVal = input("Enter the Value of the nodes:")
        ind = input("Enter the Index:")
        lst.insertmid(nodeVal,ind)
    if obtion == 5:
        ind = input("Enter the Index:")
        lst.deletemid(ind)
    if obtion == 6:
        lst.reverselst()
