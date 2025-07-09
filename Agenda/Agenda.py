class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        if nombre in self.contactos:
            raise ValueError("El contacto ya existe.")
        self.contactos[nombre] = telefono

    def buscar_contacto(self, nombre):
        return self.contactos.get(nombre, None)

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
        else:
            raise ValueError("El contacto no existe.")

