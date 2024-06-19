from Nodo import Nodo

class DirectorioContactos:
    def __init__(self, size : int) -> None:
        self.counter = 0
        self.size = size
        self.table = [None] * self.size
        
    
    def insert(self, key, value):
        """
        Inserta un par clave-valor en la tabla de dispersión
        """
        if not self.search(key):
            if self.counter < self.size:
                index = self.counter
                self.table[index] = Nodo(key, value)
                self.counter += 1
            else:
                print('Imposible de insertar por tamaño insuficiente')
        else:
            print('Imposible de insertar. Ya existe un contacto con ese nombre')
        
    def search(self, key):
        """
        Busca un valor dado su clave
        Retorna None si la clave no existe
        """
        for x in self.table:
            if x:
                if x.key == key:
                    return x.value
        return None
    
    def delete(self, key):
        """
        Elimina un valor dado su clave
        """
        for i in range(len(self.table)):
            if self.table[i]:
                if self.table[i].key == key:
                    self.table[i] = self.table[self.counter-1]
                    self.table[self.counter-1] = None
                    self.counter -= 1
                    return True
        return 
                    
    def __str__(self) -> str:
        string = ""
        for x in self.table:
            if x:
                string += f'\nNombre : {x.key},  Número : {x.value}'
        return string
        
              