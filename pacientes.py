import os
import math as m
import io

class Pacientes:
    ruta = "bd.txt"
    pacientes = {}

    def __init__(self):
        if os.stat(self.ruta).st_size != 0:
            self.load()

    def load(self):
        with io.open(self.ruta, 'r', encoding='utf8') as f:
            for line in f:
                auxp= []
                paciente = line.split(" ")
                apellido=paciente[2] + " " + paciente[3]
                for i in range(len(paciente)):
                    if i ==3:
                        continue
                    else:
                        if i==2:
                            auxp.append(apellido)
                            continue
                    auxp.append(paciente[i])
                print(auxp)
                aux = Paciente()
                aux.cargar(auxp)

            self.pacientes.update({paciente[0]: aux})
        f.close()

    def save(self):
        with io.open(self.ruta, 'w', encoding='utf8') as f:
             f.seek(0)
             for key in self.pacientes:
                f.write(self.pacientes[key].dni)
                f.write(" ")
                f.write(self.pacientes[key].N)
                f.write(" ")
                f.write(self.pacientes[key].apellido)
                f.write(" ")
                f.write(self.pacientes[key].sexo)
                f.write(" ")
                f.write(self.pacientes[key].E)
                f.write(" ")
                f.write(self.pacientes[key].F)
                f.write(" ")
                f.write(self.pacientes[key].C)
                f.write(" ")
                f.write(self.pacientes[key].ciudad)
                f.write(" ")
                f.write(self.pacientes[key].departamento)
                f.write(" ")
                f.write(self.pacientes[key].f_nacimiento)
                f.write(" ")
                f.write(self.pacientes[key].talla)
                f.write(" ")
                f.write(self.pacientes[key].peso)
                f.write(" ")
                f.write(self.pacientes[key].l1_l4[0])
                f.write(" ")
                f.write(self.pacientes[key].l1_l4[1])
                f.write(" ")
                f.write(self.pacientes[key].l1_l4[2])
                f.write(" ")
                f.write(self.pacientes[key].cuello[0])
                f.write(" ")
                f.write(self.pacientes[key].cuello[1])
                f.write(" ")
                f.write(self.pacientes[key].cuello[2])
                f.write(" ")
                f.write(self.pacientes[key].trocanter[0])
                f.write(" ")
                f.write(self.pacientes[key].trocanter[1])
                f.write(" ")
                f.write(self.pacientes[key].trocanter[2])
             f.write("\n")
             f.close()

    def find_paciente(self, dni):
        if dni in self.pacientes:
            return True
        return False

    def add_paciente(self, dni, arr_caracteristicas):
        paciente = Paciente()
        paciente.cargar(arr_caracteristicas)
        self.pacientes.update({dni: paciente})

    def update(self, paciente, arr):
        dni = paciente.dni
        paciente.update(arr)
        elem = {dni: paciente}
        self.pacientes.update(elem)


class Paciente:
    # DMO      T-Score        Z-Score
    l1_l4 = []
    cuello = []
    trocanter = []

    logeado = 0
    guardado = 0
    # DNI
    dni = ""
    # Nombre
    N = ""
    # Apellido
    apellido = ""
    sexo = "Mujer"
    # edad
    E = ""
    # Fracturas
    F = ""
    # Caidas
    C = ""
    # ciudad
    ciudad = ""
    # departamento
    departamento = ""
    # F.nacimiento
    f_nacimiento = ""
    # Talla
    talla = ""
    # PEso kg
    peso = ""

    S = 0.999896685
    a = 0.107
    b = -1.007
    c = 0.599
    d = 0.211
    riesgo = 0.1


    def update(self, arr):
        self.talla = arr[0]
        self.peso = arr[1]
        self.C = arr[2]
        self.F = arr[3]
        self.l1_l4.clear()
        self.cuello.clear()
        self.trocanter.clear()
        self.l1_l4.append(arr[4])
        self.l1_l4.append(arr[5])
        self.l1_l4.append(arr[6])
        self.cuello.append(arr[7])
        self.cuello.append(arr[8])
        self.cuello.append(arr[9])
        self.trocanter.append(arr[10])
        self.trocanter.append(arr[11])
        self.trocanter.append(arr[12])

    def cargar(self, arr_caracteristicas):
        self.l1_l4.clear()
        self.cuello.clear()
        self.trocanter.clear()
        self.dni = arr_caracteristicas[0]
        self.N = arr_caracteristicas[1]
        self.apellido = arr_caracteristicas[2]
        self.sexo = arr_caracteristicas[3]
        self.E = arr_caracteristicas[4]
        self.F = arr_caracteristicas[5]
        self.C = arr_caracteristicas[6]
        self.ciudad = arr_caracteristicas[7]
        self.departamento = arr_caracteristicas[8]
        self.f_nacimiento = arr_caracteristicas[9]
        self.talla = arr_caracteristicas[10]
        self.peso = arr_caracteristicas[11]
        l1_1 = str(arr_caracteristicas[12])
        self.l1_l4.append(l1_1)
        l1_2 = str(arr_caracteristicas[13])
        self.l1_l4.append(l1_2)
        l1_3 = str(arr_caracteristicas[14])
        self.l1_l4.append(l1_3)
        cue1 = str(arr_caracteristicas[15])
        self.cuello.append(cue1)
        cue2 = str(arr_caracteristicas[16])
        self.cuello.append(cue2)
        cue3 = str(arr_caracteristicas[17])
        self.cuello.append(cue3)
        t1 = str(arr_caracteristicas[18])
        self.trocanter.append(t1)
        t2 = str(arr_caracteristicas[19])
        self.trocanter.append(t2)
        t3 = str(arr_caracteristicas[20])
        self.trocanter.append(t3)

        # Generando constantes
        if arr_caracteristicas[2] == "H":
            self.a = 0.107
            self.b = -1.007
            self.c = 0.599
            self.d = 0.211
            self.S = 0.999997778
            self.sexo = "H"


        else:
            if arr_caracteristicas[2] == "M":
                self.a = 0.0507
                self.b = 0.8127
                self.c = -0.8417
                self.d = 0.3614
                self.S = 0.999793070
                self.sexo = "M"
        self.calculate_scores()
    def calculate_scores(self):
      self.riesgo = (1.0 - (self.S ** (m.exp(( (self.a * float(self.E)) + (self.b * float(self.cuello[1])) + (self.c * float(self.F)) + (self.d * float(self.C))))))*100)

    # self.calculate_riesgo( self.S,self.a,float(self.E),self.b,float(self.T),self.c,float(self.F),self.d,float(self.C) )



    def show_stats(self):
        print("DNI: ", self.dni)
        print("Nombre: ", self.N)
        print("Apellido: ", self.apellido)
        print("Sexo: ", self.sexo)
        print("Edad: ", self.E)
        print("Fracturas: ", self.F)
        print("Caidas: ", self.C)
        print("Ciudad: ", self.ciudad)
        print("Departamento: ", self.departamento)
        print("f_nacimiento: ", self.f_nacimiento)
        print("talla: ", self.talla)
        print("Peso: ", self.peso)
        print("l1_l4 1: ", self.l1_l4[0], " l1_l4 2: ", self.l1_l4[1], " l1_l4 3: ", self.l1_l4[2])
        print("cuello 1: ", self.cuello[0], " cuello 1: ", self.cuello[1], " cuello 3: ", self.cuello[2])
        print("tronco 1: ", self.trocanter[0], "tronco 2: ", self.trocanter[1], "tronco 3: ", self.trocanter[2])


