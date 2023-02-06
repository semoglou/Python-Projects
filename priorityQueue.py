import heapq

class PriorityQueue:

    def __init__(self, heap = [], count = 0) :
        self.count = count                           
        self.heap = heap                                

    def __str__(self):                             
        return str(self.heap)                

    def isEmpty(self):                             
        return len(self.heap) == 0                 

    def push(self, item, priority):
        heapq.heappush(self.heap,(item,priority))
        self.count += 1

    def pop(self):                                       
        t = min(self.heap, key = lambda tup: tup[1])           
        self.heap.remove(t)                                    
        self.count -= 1
        heapq.heapify(self.heap)
        return t

    def update(self,item,priority):
        flag = 0                                           
        p = 0       
        ind = 0
        for i in range(len(self.heap)):
            if item ==  self.heap[i][0]:
                flag = 1
                p = self.heap[i][1]                        
                ind = i                                   
                break
        if flag == 1 :
            if priority < p :                             
                self.heap[ind] = (item,priority)
                heapq.heapify(self.heap)
        else:
            heapq.heappush(self.heap,(item,priority))     
            self.count += 1

def PQSort(L):
    q = PriorityQueue([],0)                
    M = []
    for i in L:
        q.push('none',i)                   
    for i in range(len(q.heap)):
        t = q.pop()[1]                     
        M.append(t)
    return M


