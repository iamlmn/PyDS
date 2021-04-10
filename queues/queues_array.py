# FIFO Queue with Lists/ Array
class Queues:
    def __init__(self):
        self.QueueList = []

    def __len__(self):
        return len(self.QueueList)
    
    def isempty(self):
        return len(self.QueueList) == 0

    def display(self):
        print(self.QueueList)

    def enqueue(self, element):
        self.QueueList.append(element)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return
        return self.QueueList.pop(0)

    def peek(self):
        return self.QueueList[0]


if __name__ == '__main__':
    Q = Queues()
    Q.enqueue(5)
    Q.enqueue(15)
    Q.enqueue(115)
    Q.display()
    print("Running Dequeue")
    Q.dequeue()
    Q.display()
    print("Quick peek to Queue->", Q.peek())


