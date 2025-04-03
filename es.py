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
    
class SistemaAtendimento:
    def __init__(self):
        self.fila_atendimento = PersonalQueue() 
        self.historico_atendimentos = PersonalStack() 

    def chegada_cliente(self, nome_cliente):
       
        self.fila_atendimento.enqueue(nome_cliente)
        print(f"✅ '{nome_cliente}' entrou na fila. Posição: {self.fila_atendimento.list.size()}")

    def atender_cliente(self):
      
        if self.fila_atendimento.list.isEmpty():
            print("⚠️ Fila vazia! Nenhum cliente para atender.")
            return
        
        cliente_atual = self.fila_atendimento.dequeue()
        self.historico_atendimentos.push(cliente_atual)
        print(f"🎉 '{cliente_atual}' foi atendido(a).")

    def desfazer_ultimo_atendimento(self):
 
        if self.historico_atendimentos.list.isEmpty():
            print("⚠️ Histórico vazio! Nada para desfazer.")
            return
        
        cliente_retornado = self.historico_atendimentos.pop()
        self.fila_atendimento.enqueue(cliente_retornado)
        print(f"↩️ '{cliente_retornado}' voltou para a fila.")

    def mostrar_fila(self):
      
        if self.fila_atendimento.list.isEmpty():
            print("📭 Fila vazia.")
            return
        
        print("\n📋 Fila de Atendimento:")
        for i in range(self.fila_atendimento.list.size()):
            print(f"{i+1}º: {self.fila_atendimento.list.elementAt(i)}")

    def mostrar_historico(self):
      
        if self.historico_atendimentos.list.isEmpty():
            print("📭 Histórico vazio.")
            return
        
        print("\n📜 Histórico de Atendimentos (do mais recente):")
        for i in range(self.historico_atendimentos.list.size()):
            print(f"→ {self.historico_atendimentos.list.elementAt(i)}")

if __name__ == "__main__":
    sistema = SistemaAtendimento()


    sistema.chegada_cliente("João")
    sistema.chegada_cliente("Maria")
    sistema.chegada_cliente("Carlos")

    sistema.mostrar_fila()

    sistema.atender_cliente()
    sistema.atender_cliente()

    sistema.mostrar_historico()

    sistema.desfazer_ultimo_atendimento()

    sistema.mostrar_fila()
    sistema.mostrar_historico()
    

queue = PersonalQueue();
		


