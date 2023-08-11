class Node:
    def __init__(self,data):
        self.Node=data
        self.Freand=None
class linked_list:
    def __init__(self) -> None:
        self.heade=None
    def isEmpty(self:Node):
        return self.heade==None
    def addF(self,data):
        Data=Node(data)
        head=self.heade
        Data.Freand=head
        self.heade=Data
    def addEnd(self,data:Node):
        if  self.isEmpty():
            self.heade=Node(data)
        else:
            current=self.heade
            while current.Freand!= None:
                current= current.Freand
            current.Freand=Node(data)
    def getList(self):
        return self.heade
    def display(self,nodes):
       current=nodes
       if current!= None:
           print(current.Node)
           current=current.Freand
           return self.display(current)
    def delletNode(self,value):
        current= self.heade
        while current != None:
            if current.Node==value  :
                """current.Node=current.Freand.Node
                current.Freand=current.Freand.Freand"""
                current=current.Freand
                self.heade=current
            elif current.Node==value and current.Freand==None:
                current=None
                self.heade=current
                current=None
            else:
                current=current.Freand

'''linked= linked_list()
print(linked.isEmpty())
linked.addEnd(1)
linked.addEnd(2)
linked.addEnd(3)
linked.addF('a')
print(linked.isEmpty())
print(linked.getList().Freand.Freand.Freand.Node)
#linked.display(linked.getList())
#linked.delletNode('a')
linked.display(linked.getList())'''
class Queue:
    def __init__(self):
        self.linkedlst=linked_list()
    def enQueue(self,input):
        self.linkedlst.addEnd(input)
    def deQueue(self):
        if self.linkedlst.getList().Node != None:
            Output=self.linkedlst.getList().Node
            self.linkedlst.delletNode(Output)
            return Output
        return None
    def isEmpty(self):
        return self.linkedlst.getList()==None
    def peekFirst(self):
        return self.linkedlst.getList().Node
    def peekLast(self):
        current=self.linkedlst.getList()
        while current.Freand != None:
            current=current.Freand
        return current.Node
'''Q=Queue()
print(Q.isEmpty())
Q.enQueue(1)
Q.enQueue(2)
Q.enQueue(3)
print(Q.isEmpty())
print(Q.peekFirst())
print(Q.peekLast())
print(Q.deQueue())
print(Q.peekFirst())
Q.deQueue()
Q.deQueue()'''

class graph:
    def __init__(self) -> None:
        self.Graph={}
    def createVertex(self,Name):
        self.Graph.update({Name:linked_list()})
    def addFreands(self,user,freand):
        Frands=list(self.Graph.keys())
        if freand in Frands:
            self.Graph[user].addEnd(freand)
        else:
            print('Sorry freand not found!')
    def printGrapph(self):
        for key,value in self.Graph.items():
            print(f'{key} freands:',end='')
            value.display(value.getList())
    def RemoveVertex(self,user):
        if not user in list(self.Graph.keys()):
            print('Invalid user !!')
        self.Graph.pop(user)
    def BFT(self,v):
        Que=Queue()
        vertex=self.Graph[v].getList()
        Que.enQueue(v)
        vertesies=list(self.Graph.keys())
        while len(vertesies) !=0:
         if Que.isEmpty():
            Que.enQueue(vertesies[0])
                       
         else:
            v=Que.deQueue()
            if v in vertesies:
                    vertex=self.Graph[v].getList()
                    vertesies.remove(v)
                    current=vertex
                    while current != None :
                        if current.Node in vertesies:
                         Que.enQueue(current.Node)
                        current=current.Freand
                    print(v)
    def deleteFreand(self,user,freand):
        self.Graph[user].delletNode(freand)
    def displayFreands(self,user):
        current=self.Graph[user].display(self.Graph[user].getList())
                    
            
        
            
"""gr=graph()
Name_1=input('Enter the name: ')
Name_2=input('Enter the name: ')
Name_3=input('Enter the name: ')
Name_4=input('Enter the Name: ')
gr.createVertex(Name_1)
gr.createVertex(Name_2)
gr.createVertex(Name_3)
gr.createVertex(Name_4)
gr.addFreands(Name_2,Name_1)
gr.addFreands(Name_4,Name_1)
gr.addFreands(Name_1,Name_2)
gr.addFreands(Name_3,Name_2)
gr.addFreands(Name_1,Name_3)
gr.addFreands(Name_2,Name_3)
gr.addFreands(Name_4,Name_3)
gr.addFreands(Name_3,Name_4)
gr.addFreands(Name_2,Name_4)

gr.printGrapph()
gr.BFT(Name_2)
gr.displayFreands(Name_3)
gr.deleteFreand(Name_3,Name_1)
print('--------------------')
gr.displayFreands(Name_3)
gr.RemoveVertex(Name_2)
"""

def main(Platform):
    Option= input('1. Add a user to the platform.\n2. Remove a user from the platform.\n3. Send a friend request to another user.\n4. Remove a friend from your list.\n5. View your list of friends.\n6. View the list of users on the platform.\n7. Exit\n- - - - - - - - - - - - - - -\nEnter a choice:')
    if Option=='1':
        Name=input('Enter the user name: ')
        Platform.createVertex(Name)
        main(Platform)
    elif Option=='2':
        user=input('Enter the user name to delete: ')
        Platform.RemoveVertex(user)
        for key,value in Platform.Graph.items():
           value.delletNode(user)
        main(Platform)
    elif Option=='3':
        Platform.addFreands(input('Enter your user Name: '),input('Enter the freand to add: '))
        main(Platform)
    elif Option=='4':
        Platform.deleteFreand(input('Enter your user Name: '),input('Enter the freand to add: '))
        main(Platform)
    elif Option=='5':
        Platform.displayFreands(input('Enter your user Name: '))
        main(Platform)
    elif Option =='6':
        Platform.BFT(list(Platform.Graph.keys())[0])
        main(Platform)
    elif Option =='7':
        print('Program is turminated')
    else:
        print('Wrong choise!!')
        main(Platform)

Platform=graph()
main(Platform)