from playsound import playsound

class QueueBank:
    def __init__(self):
        self.queue = []
        self.Business_Queue = 0
        self.Personal_Queue = 0
        self.table1 = None
        self.table2 = None

    def size(self):
        return len(self.queue)

    def parent(self,index):
        return (index-1)//2

    def left(self,index):
        return (index * 2 )+ 1

    def right(self,index):
        return (index * 2 )+ 2

    def swap(self,index1 , index2):
        temp = self.queue[index1]
        self.queue[index1] = self.queue[index2]
        self.queue[index2] = temp

    def push_up(self,index):
        if index > 0 and index < self.size() :
            idxParent = self.parent(index)
            if self.queue[index] < self.queue[idxParent]:
                self.swap(index,idxParent)
                self.push_up(idxParent)

    def add(self,new_data):
        self.queue.append(new_data)
        self.push_up(self.size()-1)

    def child_valid(self,index):
        return self.left(index) < self.size()

    def Smallest_child(self,index):
        idxLeft = self.left(index)
        idxRight = self.right(index)

        if idxRight < self.size():
            if self.queue[idxLeft] < self.queue[idxRight]:
                return idxLeft
            else :
                return idxRight
        else:
            return idxLeft

    def push_down(self,index):
        if self.child_valid(index):
            idxSmall = self.Smallest_child(index)
            if self.queue[idxSmall] < self.queue[index] :
                self.swap(index,idxSmall)
                self.push_down(idxSmall)

    def remove(self):
        if self.size() > 0:
            value = self.queue[0]
            if self.size() > 1 :
                self.queue[0] = self.queue[self.size()-1]
            self.queue.pop(self.size()-1)
            self.push_down(0)
            return value

#---------------------------------------------------------------------------------------------------------

    def add_queue(self,Type):
        if Type == "B" :
            self.Business_Queue += 1
            Business = f"B{self.Business_Queue:03d}"
            self.add(Business)
        elif Type == "P" :
            self.Personal_Queue += 1
            Personal = f"P{self.Personal_Queue:03d}"
            self.add(Personal)


    def next(self):
        if self.size() > 0 :
            print(self.queue[0], end=" ")
        else:
            print("None", end=" ")

    def call(self,table):
        if table == "1":
            if self.size() < 0:
                print("Calling Failed")
            else:
                self.table1 = self.remove()
                print("=====================================")
                print("\t\tPERPUS DIMARI BANK")
                print("=====================================")
                print("-------------------------------------", end="\n")
                print("|\tTable 1\t|\tTable 2\t|\tNext\t|")
                print("|-----------|-----------|-----------|", end="\n")
                print("|\t", self.table1, "\t|", end=" "), print("\t", self.table2, "\t|", end=" "), print("\t",end=" "), \
                self.next(), print("\t|", end="\n")
                print("-------------------------------------", end="\n")
                playsound("sound/soundBell.wav")
                playsound("sound/queue_number.wav")
                for char in self.table1:
                    playsound("sound/" + char + ".wav")
                playsound("sound/going_to.wav")
                playsound("sound/table_1.wav")
                playsound("sound/soundBell_tutup.wav")

        else:
            if self.size() < 0:
                print("Calling Failed")
            else:
                self.table2 = self.remove()
                print("=====================================")
                print("\t\tPERPUS DIMARI BANK")
                print("=====================================")
                print("-------------------------------------", end="\n")
                print("|\tTable 1\t|\tTable 2\t|\tNext\t|")
                print("|-----------|-----------|-----------|", end="\n")
                print("|\t", self.table1, "\t|", end=" "), print("\t", self.table2, "\t|", end=" "), print("\t",end=" "), self.next(), \
                print("\t|", end="\n")
                print("-------------------------------------", end="\n")
                playsound("sound/soundBell.wav")
                playsound("sound/queue_number.wav")
                for char in self.table2:
                    playsound("sound/" + char + ".wav")
                playsound("sound/going_to.wav")
                playsound("sound/table_2.wav")
                playsound("sound/soundBell_tutup.wav")

    def menu(self):
        while True:
            print("=====================================")
            print("\t\tPERPUS DIMARI BANK")
            print("=====================================")

            print("-------------------------------------", end="\n")
            print("|\tTable 1\t|\tTable 2\t|\tNext\t|")
            print("|-----------|-----------|-----------|", end="\n")
            print("|\t", self.table1, "\t|", end=" "), print("\t", self.table2, "\t|", end=" "), print("\t", end=" "), self.next(), print( "\t|", end="\n")
            print("-------------------------------------", end="\n")

            print("1. Add Business Queue")
            print("2. Add Personal Queue")
            print("3. Table 1 Calling")
            print("4. Table 2 Calling")
            print("5. Quit")
            inputan = input("Option : ")
            print(" ")

            if inputan == "1":
                self.add_queue("B")
            elif inputan == "2":
                self.add_queue("P")
            elif inputan == "3":
                if self.size() == 0:
                    print("Calling failed, please add new queue.")
                    pass
                else :
                    self.call("1")
            elif inputan == "4":
                if self.size() == 0:
                    print("Calling failed, please add new queue.")
                    pass
                else :
                    self.call("2")
            else:
                print("=====================================")
                print("\t\t\tTHANK YOU")
                print("=====================================")
                break

# Create a queue_bank instance
q = QueueBank()
q.menu()
