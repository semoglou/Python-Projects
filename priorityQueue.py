import heapq

class PriorityQueue:

    def __init__(self, heap = [], count = 0) :
        self.count = count                           # Αρχικοποιήση του μετρητή σε 0
        self.heap = heap                                # Αρχικοποιήση του σωρού σε κενή λίστα

    def __str__(self):                             
        return str(self.heap)                # Ορισμός Κατάστασης αντικειμένου - μόνο το heap (για ευκολότερη επαλήθευση μέσω print)

    def isEmpty(self):                             
        return len(self.heap) == 0                 # Επιστρέφει True αν η ουρά προτεραιότητας είναι άδεια και False διαφορετικά

    def push(self, item, priority):
        heapq.heappush(self.heap,(item,priority))
        self.count += 1

    def pop(self):                                       
        t = min(self.heap, key = lambda tup: tup[1])           # Ελάχιστο στοιχείο βάση της προτεραιότητας (Του 2ου στοιχείου από κάθε tupple δηλαδή)
        self.heap.remove(t)                                    # Αφαίρεση στοιχείου από την ουρά για να λειτουργεί ως pop
        self.count -= 1
        heapq.heapify(self.heap)
        return t

    def update(self,item,priority):
        flag = 0                                          # Γίνεται flag = 1 αν εντοπιστεί το item στην ουρά 
        p = 0       
        ind = 0
        for i in range(len(self.heap)):
            if item ==  self.heap[i][0]:
                flag = 1
                p = self.heap[i][1]                       # Η προτεραιότητα του item στην ουρά 
                ind = i                                   # Η θέση που βρίσκεται το στοιχείο που πρόκειται να γίνει update
                break
        if flag == 1 :
            if priority < p :                             # Σύγκριση της προτεραίοτητας με το priority που εισάγεται στην update
                self.heap[ind] = (item,priority)
                heapq.heapify(self.heap)
        else:
            heapq.heappush(self.heap,(item,priority))     # Αφού flag=0 το item δεν υπάρχει ήδη στην ουρά και η update λειτουργεί ως push
            self.count += 1

def PQSort(L):
    q = PriorityQueue([],0)                # Αρχικοποιήση μιας ουράς προτεραιότητας q
    M = []
    for i in L:
        q.push('none',i)                   # Εισαγωγή των στοιχείων της λίστας στην q ως προτεραιότητες στοιχείων
    for i in range(len(q.heap)):
        t = q.pop()[1]                     # Εξαγωγή των προτεραιοτήτων(-στοιχείων της λίστας) μέσω της pop που εξασφαλίζει το μικρότερο σε κάθε κλήση
        M.append(t)
    return M


if __name__ == "__main__":                 # Τεστ - Παράδειγμα
    print('\nΠαράδειγμα: \n')
    q = PriorityQueue()
    print('Oυρά q:', q)
    print('Είναι άδεια: ',q.isEmpty())
    print('\nΚάνω Push στην q τα εξής: (task0,0), (task1,2), (task2,3), (task3,5), (task1,1), (task3,4)')
    print('και εμφανίζω την q: \n')
    q.push('task0',0)
    q.push('task1',2)
    q.push('task2',3)
    q.push('task3',5)
    q.push('task1',1)
    q.push('task3',4)
    print(q)
    print('\nΕίναι άδεια: ',q.isEmpty())
    print('\nΚάνω Pop 2 φορές')
    print('εμφανίζω τα στοιχεία που έγιναν popped και στη συνέχεια εμφανίζω τη νέα q: \n')
    u = q.pop()
    v = q.pop()
    print(u,'\n')
    print(v,'\n')
    print(q,'\n')
    print('Εφαρμόζω update(task2,1) και update(task1,0) στην q (περιμένω να αλλάξει)')
    print('Eφαρμόζω επίσης update(task2,5),(task3,6) (δεν γίνεται τίποτα)')
    print('Εφαρμόζω επίσης update(new,100) και γίνεται push')
    q.update('task2',1)
    q.update('task1',0)
    q.update('task2',5)
    q.update('task3',6)
    q.update('new',100)
    print('Εμφάνιση της q: \n')
    print(q)
    print('\nPQSort([9,8,7,1,2,3,5,6,4,10,15,14,13,17,11,12,18,16]) = \n')
    print(PQSort([9,8,7,1,2,3,5,6,4,10,15,14,13,17,11,12,18,16]))