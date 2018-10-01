from collections import Iterator

class LinkedChord:
    def __init__(self,chord,key,name):
        self.chord = chord
        self.key = key
        self.name = name
        self.next = None
        self.prev = None
        # self.prediction = f(p,n) #for ML

    def __repr__(self):
        if self.prev is None:
            p = None
        else:
            p = self.prev.name
        if self.next is None:
            n = None
        else:
            n = self.next.name
        return "{0} <- {1} -> {2}".format(p,self.name,n)

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
    def __contains__(self,node):
        """ maybe need fix sometime """
        for iterator in self:
            if iterator.name == node.name:
                return True
    def __iter__(self):
        return LinkedListIterator(self)

    def __len__(self):
        """
        >>> CHORD = dict({'C':'C_chord','D':'D_chord','G7':'DomG7'})
        >>> C_Major = 'C_Major_Scale'
        >>> G_Major = 'G_Major_Scale'
        >>> l = LinkedList()
        >>> len(l)
        0
        >>> n2 = LinkedChord(CHORD['C'],G_Major,'C')
        >>> n3 = LinkedChord(CHORD['D'],G_Major,'D')
        >>> l.append_left(n3)
        >>> len(l)
        1
        >>> l.append_left(n2)
        >>> len(l)
        2
        """
        if self.head == None:
            return 0
        else:
            node = self.head
            length = 1
            while node.next:
                length +=1
                node = node.next
        return length

    def __getitem__(self,index):
        """
        >>> CHORD = dict({'C':'C_chord','D':'D_chord','G7':'DomG7'})
        >>> C_Major = 'C_Major_Scale'
        >>> G_Major = 'G_Major_Scale'
        >>> l = LinkedList()
        >>> n2 = LinkedChord(CHORD['C'],G_Major,'C')
        >>> n3 = LinkedChord(CHORD['D'],G_Major,'D')
        >>> l.append(n3)
        >>> l.append(n2)
        >>> l[0].name
        'D'
        >>> l[1].name
        'C'
        >>> l[-1].name
        'C'
        >>> l[-2].name
        'D'
        """
        if type(index) != int:
            raise TypeError
        if self.head == None:
            raise IndexError

        if index >= 0:
            res = self.head
        else:
            res = self.last
        if index < -1:
            for i in range(-index-1):
                res = res.prev
        else:
            for i in range(index):
                res = res.next
        return res

    def __setitem__(self,index,data):
        """
        Not change pointor to the new one, just simply change the inside data.

        >>> CHORD = dict({'C':'C_chord','D':'D_chord','G7':'DomG7'})
        >>> C_Major = 'C_Major_Scale'
        >>> G_Major = 'G_Major_Scale'
        >>> l = LinkedList()
        >>> n2 = LinkedChord(CHORD['C'],G_Major,'C')
        >>> n3 = LinkedChord(CHORD['D'],G_Major,'D')
        >>> n4 = LinkedChord(CHORD['G7'],G_Major,'G7')
        >>> l.append(n3)
        >>> l.append(n2)
        >>> l[1]
        D <- C -> None
        >>> l[1] = n4
        >>> l[1]
        D <- G7 -> None
        >>> n2
        D <- G7 -> None
        >>> n4
        None <- G7 -> None
        """
        if type(index) != int:
            raise TypeError
        if index < -len(self) or index >= len(self):
            raise IndexError

        if index >= 0:
            res = self.head
        else:
            res = self.last
        if index < -1:
            for i in range(-index-1):
                res = res.prev
        else:
            for i in range(index):
                res = res.next
        res.chord = data.chord
        res.key = data.key
        res.name = data.name
        return res

    def __iadd__(self,data):
        self.append(data)
        return self

    def __reversed__(self):
        return LinkedListReverseIterator(self)

    def __repr__(self):
        return self.display()

    def reverse(self):
        pass
    def index(self,data):
        pass
    def insert(self,index,data):
        pass
    def count(self,data):
        pass
    def remove(self,data):
        pass
    def extend(self,linkedlist):
        pass
    def pop(self):
        pass
    def pop_left(self):
        pass
    def clear(self):
        pass
    def append_left(self,data):
        """
        >>> CHORD = dict({'C':'C_chord','D':'D_chord','G7':'DomG7'})
        >>> C_Major = 'C_Major_Scale'
        >>> G_Major = 'G_Major_Scale'
        >>> l = LinkedList()
        >>> n2 = LinkedChord(CHORD['C'],G_Major,'C')
        >>> n3 = LinkedChord(CHORD['D'],G_Major,'D')
        >>> l.append_left(n3)
        >>> l.append_left(n2)
        >>> l.head.name
        'C'
        >>> l.last.name
        'D'
        >>> n3 = LinkedChord(CHORD['G7'],C_Major,'G7')
        >>> l.append_left(n3)
        >>> l.last.prev.prev.name
        'G7'
        """
        node = data
        if self.head == None:
            self.head = node
            self.last = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node
    def append(self,data):
        node = data
        if self.head == None:
            self.head = node
            self.last = node
        else:
            node.prev = self.last
            node.prev.next = node
            self.last = node
    def display(self):
        """
        >>> CHORD = dict({'C':'C_chord','D':'D_chord','G7':'DomG7'})
        >>> C_Major = 'C_Major_Scale'
        >>> G_Major = 'G_Major_Scale'
        >>> n2 = LinkedChord(CHORD['D'],G_Major,'D')
        >>> n3 = LinkedChord(CHORD['C'],G_Major,'C')
        >>> l = LinkedList()
        >>> l.display()
        ''
        >>> l.append(n2)
        >>> l.append(n3)
        >>> l.display()
        'D - C'
        >>> n2
        None <- D -> C
        >>> n3
        D <- C -> None
        >>> n3 = LinkedChord(CHORD['C'],G_Major,'C')
        >>> l.append(n3)
        >>> l.display()
        'D - C - C'
        >>> n3.prev
        D <- C -> C
        """
        res = ""
        if self.head == None:
            return res
        else:
            node = self.head
            while node != None:
                res += " - {0}".format(node.name)
                node = node.next
        return res[3:]

class LinkedListIterator(Iterator):
    def __init__(self, linkedlist):
        self.node = linkedlist.head

    def __next__(self):
        if self.node == None:
            raise StopIteration
        res = self.node
        self.node = self.node.next
        return res

class LinkedListReverseIterator(Iterator):
    def __init__(self, linkedlist):
        self.node = linkedlist.last

    def __next__(self):
        if self.node == None:
            raise StopIteration
        res = self.node
        self.node = self.node.prev
        return res
