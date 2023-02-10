class Node:
    def __init__(self, dvd_data, next=None):
        self.dvd_data = dvd_data
        self.next = next
        
class DVListType:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def add_dvd(self, dvd_data):
        new_node = Node(dvd_data)
        new_node.next = self.head
        self.head = new_node
        
    def remove_dvd(self, dvd_name):
        current = self.head
        previous = None
        found = False
        while not found:
            if current == None:
                break
            if current.dvd_data.name == dvd_name:
                found = True
            else:
                previous = current
                current = current.next
        if not found:
            return None
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next
        return current.dvd_data
