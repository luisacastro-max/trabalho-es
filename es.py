class PersonalArray:
    SIZE = 5
    insertPosition = 0
    elements = [None] * SIZE

    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return self.insertPosition
        
    def isMemoryFull(self):
        return self.insertPosition == len(self.elements)
    
    def append(self, newElement):
        if self.isMemoryFull():
            self.updateMemory()
        self.elements[self.insertPosition] = newElement
        self.insertPosition += 1
    

    def updateMemory(self):
        newArray = [None] * (self.size() + self.SIZE)
        for position in range(self.insertPosition):  
            newArray[position] = self.elements[position]
        self.elements = newArray
    
    def clear(self):
        self.elements = [None] * self.SIZE  
        self.insertPosition = 0
    
    def remove(self):
        if not self.isEmpty():
            self.elements[self.insertPosition - 1] = None
            self.insertPosition -= 1
    
    def removePosition(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return ""
        removedElement = self.elements[position]
        index = position
        while index < self.insertPosition - 1:  
            self.elements[index] = self.elements[index+1]
            index += 1
        self.insertPosition -= 1
        return removedElement
        
    def insertAt(self, position, newElement):
        if position < 0 or position > self.insertPosition:
            print("Posição inválida!")
            return
        if self.isMemoryFull():
            self.updateMemory()
        index = self.insertPosition - 1
        while index >= position:  
            self.elements[index + 1] = self.elements[index]
            index -= 1
        self.elements[position] = newElement
        self.insertPosition += 1   
        
    
    def elementAt(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return None
        return self.elements[position]
    



        

class PersonalStack:
    list = PersonalArray()
    
    def push(self, newElement):
        self.list.insertAt(0, newElement)
    
    def pop(self):
        return self.list.removePosition(0)

class PersonalQueue:
    list = PersonalArray()
    
    def enqueue(self, newElement):
        self.list.insertAt(0, newElement)
    
    def dequeue(self):
        return self.list.removePosition(self.list.size() - 1)
    
def eh_palindromo(palavra):
    stack = PersonalStack()
    palavra = palavra.lower()  
    
    for letra in palavra:
        stack.push(letra)
    
    for letra in palavra:
        if stack.pop() != letra:
            return (palavra, False) 
    return (palavra, True)  
resultados = [
    eh_palindromo("arara"),
    eh_palindromo("casa"),
    eh_palindromo("Reviver"),
    eh_palindromo("Python"),
    eh_palindromo("ovo")
]
for palavra, eh_pali in resultados:
    print(f"'{palavra}': {'É palíndromo!' if eh_pali else 'Não é palíndromo.'}")

    

queue = PersonalQueue();
		


