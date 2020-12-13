import tkinter as tk
from pacientes import *



# from pacientes import *
# FLECHA DE REGRESO
FUENTEFLECHA = ("Calibri bold", 17)
# DNI/EDAD PACIENTE GRABADO
FUENTE21 = ("Bahnschrift SemiBold", 12)
# TITULOS CON FONDO AZUL
FUENTE13 = ("Bahnschrift SemiBold", 13)
# TITULO BOTONOS
FUENTE16 = ("Bahnschrift SemiBold", 15)
# FORMATO (dd/mm/aaa) (g/cm^2)
FUENTE14 = ("Bahnschrift Light", 8)
# PIE DE PAGINA
FUENTEPIE = ("Bahnschrift Light", 10)
# TODOS LOS CUESTIONARIOS
FUENTE1 = ("Bahnschrift Light", 11)
# RESULTADOS Y RECOMENDACIONES
FUENTE11 = ("Bahnschrift Light", 13)
# INGRESE SU CONTRASEÑA
FUENTE17 = ("Bahnschrift Light", 17)
# RAMAS
FUENTE25 = ("Bahnschrift Light", 19)
# BUSCADOR DNI
FUENTE35 = ("Bahnschrift Light", 25)
# TITULO INICIO
FUENTE36 = ("Bahnschrift Light", 40)


class AuquishApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk.iconbitmap(self, default="logo.bmp")
        tk.Tk.wm_title(self, "Tendoux")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.pacientes = Pacientes()
        self.p_actual = Paciente()
        self.frames = {}

        for F in (Login, Ramas, BuscadorDNI, ActualizarRegistroNuevo, MostradorResultados, HistoriaPacienteAntiguo,
                  RegistrarNuevoPaciente):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_pacientes(self):
        return self.pacientes

    def set_paciente(self, paciente):
        self.p_actual = paciente

    def get_paciente(self):
        return self.p_actual


class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="WHITE")

        def verificar_contrasena():
            if my_password.get() == "":
                controller.show_frame(Ramas)
                incorrect_password_label["text"] = " "
                my_password.set("")
            else:
                incorrect_password_label["text"] = "La contraseña que ingresó es incorrecta. Inténtelo de nuevo"

        titulo = tk.Label(self, text="TENDOUX", font=FUENTE36, bg="#5b9fc9")
        titulo.pack(pady=75, padx=40, ipadx=350, ipady=10)

        password_label = tk.Label(self, text="Ingrese su contraseña", bg="white", fg="black", font=FUENTE17)
        password_label.pack(ipady=10)

        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self, textvariable=my_password, width=22, font=FUENTE1, show="*", bg="white")
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7, pady=20)

        enter_button = tk.Button(self, text="ACEPTAR", command=verificar_contrasena, relief="groove", borderwidth=2,
                                 width=15, height=1, font=FUENTE17, fg="black")
        enter_button.pack(pady=40)

        incorrect_password_label = tk.Label(self, text=" ", bg="white", anchor="n", fg="red", font=FUENTE1)
        incorrect_password_label.pack(fill="both", expand=True)


class Ramas(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

        #   columnas---------------------------------------------------------------------------------------------------
        columna0 = tk.Label(self, bg="white").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="white").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="white").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="white").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="white").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="white").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="white").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="white").grid(row=0, column=7, ipadx=80)

        row1 = tk.Label(self, bg="white").grid(row=1, column=7, sticky="nsew", ipadx=80, ipady=80)

        Boton1 = tk.Button(self, text="Pacientes registrados", font=FUENTE25, bg="#5b9fc9", fg="white", anchor="center",
                           relief="groove", borderwidth=2, command=lambda: controller.show_frame(BuscadorDNI))
        Boton1.grid(row=2, column=1, columnspan=4, sticky="NSEW", ipady=10)

        row3 = tk.Label(self, bg="white").grid(row=3, column=7, sticky="nsew", ipadx=80, ipady=50)

        Boton2 = tk.Button(self, text="Registrar nuevo paciente", font=FUENTE25, bg="#5b9fc9", fg="white",
                           anchor="center", relief="groove", borderwidth=2,
                           command=lambda: controller.show_frame(RegistrarNuevoPaciente))
        Boton2.grid(row=4, column=1, columnspan=4, sticky="NSEW", ipady=11)


class ActualizarRegistroNuevo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="WHITE")

        #   columnas------------------------------------------------------------------------------------------------
        columna0 = tk.Label(self, bg="white").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="white").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="white").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="white").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="white").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="white").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="white").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="white").grid(row=0, column=7, ipadx=80)
        #   row1 ---------------------------------------------------------------------------------------------
        row1 = tk.Label(self, bg="white").grid(row=1, column=7, ipadx=80, ipady=10)

        #   NUEVA CONSULTA---------------------------------------------------------------------------------------------
        label = tk.Label(self, text="  NUEVA CONSULTA", font=FUENTE13, background="#5b9fc9", anchor="w",
                         fg="white").grid(row=12, column=1, columnspan=6, sticky="NSEW", )

        row = tk.Label(self, bg="white").grid(row=13, column=7, ipadx=80, ipady=8)

        #   TALLA
        label = tk.Label(self, text=" Talla (cm):", font=FUENTE1, anchor="e", bg="white").grid(row=15, column=1,
                                                                                               columnspan=2,
                                                                                               sticky="nsew")
        talla = tk.StringVar()
        tallaVariable = tk.Entry(self, textvariable=talla, font=FUENTE1, bg="white", width=1)
        tallaVariable.grid(row=15, column=3, sticky="nsew")
        tallaVariable.focus_set()
        #   PESO
        label = tk.Label(self, text=" Peso (kg):", font=FUENTE1, anchor="e", bg="white").grid(row=15, column=4,
                                                                                              columnspan=2,
                                                                                              sticky="nsew")
        peso = tk.StringVar()
        pesoVariable = tk.Entry(self, textvariable=peso, font=FUENTE1, bg="white", width=1)
        pesoVariable.grid(row=15, column=6, sticky="nsew")
        pesoVariable.focus_set()
        #   CAIDAS ANTERIORES
        label = tk.Label(self, text="Número de fracturas luego de los 50 años* :", font=FUENTE1, anchor="e",
                         bg="white").grid(row=17, column=1, columnspan=2, sticky="nsew")
        caidas = tk.StringVar()
        caidasVariable = tk.Entry(self, textvariable=caidas, font=FUENTE1, bg="white", width=1)
        caidasVariable.grid(row=17, column=3, sticky="nsew")
        caidasVariable.focus_set()

        #   FRACTURAS ANTERIORES
        label = tk.Label(self, text="Número de caídas en el último año:", font=FUENTE1, anchor="e", bg="white").grid(
            row=17, column=4, columnspan=2, sticky="nsew")
        fracturas = tk.StringVar()
        fracturasVariables = tk.Entry(self, textvariable=fracturas, font=FUENTE1, bg="white", width=1)
        fracturasVariables.grid(row=17, column=6, sticky="nsew")
        fracturasVariables.focus_set()

        row = tk.Label(self, bg="white").grid(row=20, column=7, ipadx=80, ipady=10)

        #   PADRES FRACTURAS
        label = tk.Label(self, text="¿Padres con fractura de cadera?", font=FUENTE1, anchor="center", bg="#e0e0e0",
                         fg="black").grid(row=21, column=1, columnspan=2, sticky="nsew", ipady=5)
        padresVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=padresVariable, value=1, font=FUENTE1, anchor="center",
                                bg="white").grid(row=22, column=1, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=padresVariable, value=2, font=FUENTE1, anchor="center",
                                bg="white").grid(row=22, column=2, sticky="nsew")

        #   FUMADOR ACTIVO
        label = tk.Label(self, text="¿Fumador activo?", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=21,
                                                                                                          column=3,
                                                                                                          columnspan=2,
                                                                                                          sticky="nsew",
                                                                                                          ipady=5)
        fumadorVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=fumadorVariable, value=1, font=FUENTE1, anchor="center",
                                bg="white").grid(row=22, column=3, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=fumadorVariable, value=2, font=FUENTE1, anchor="center",
                                bg="white").grid(row=22, column=4, sticky="nsew")

        #   ARTRITIS REUMATOIDE
        label = tk.Label(self, text=" ¿Sufre de artritis reumatoide? ", font=FUENTE1, anchor="center",
                         bg="#e0e0e0").grid(row=21, column=5, columnspan=2, sticky="nsew", ipady=5)
        reumatoideVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=reumatoideVariable, value=1, font=FUENTE1, anchor="center",
                                bg="white").grid(row=22, column=5, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=reumatoideVariable, value=2, font=FUENTE1, anchor="center",
                                bg="white").grid(row=22, column=6, sticky="nsew")

        row23 = tk.Label(self, bg="white").grid(row=23, column=7, ipadx=80)

        #   GLUCOCORTICOIDES
        label = tk.Label(self, text="¿Consume glucocorticoides?", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(
            row=25, column=1, columnspan=2, sticky="nsew", ipady=5)
        glucoVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=glucoVariable, value=1, font=FUENTE1, anchor="center",
                                bg="white").grid(row=26, column=1, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=glucoVariable, value=2, font=FUENTE1, anchor="center",
                                bg="white").grid(row=26, column=2, sticky="nsew")

        #   ALCOHOL
        label = tk.Label(self, text="¿Consume alcohol?", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=25,
                                                                                                           column=3,
                                                                                                           columnspan=2,
                                                                                                           sticky="nsew",
                                                                                                           ipady=5)
        alcoholVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=alcoholVariable, value=1, font=FUENTE1, anchor="center",
                                bg="white").grid(row=26, column=3, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=alcoholVariable, value=2, font=FUENTE1, anchor="center",
                                bg="white").grid(row=26, column=4, sticky="nsew")

        #   OSTEOPOROSIS SECUNDARIA
        label = tk.Label(self, text="¿Sufre un trastorno asociado a osteoporosis?**", font=FUENTE1, anchor="center",
                         bg="#e0e0e0").grid(row=25, column=5, columnspan=2, sticky="nsew", ipady=5)
        secundariaVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=secundariaVariable, value=1, font=FUENTE1, anchor="center",
                                bg="white").grid(row=26, column=5, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=secundariaVariable, value=2, font=FUENTE1, anchor="center",
                                bg="white").grid(row=26, column=6, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=27, column=7, ipadx=80, ipady=10)

        # TITULO-------------------------------------------------------------------------------------------------------

        label = tk.Label(self, text="Ingrese datos de densitometría\nósea →", font=FUENTE1, anchor="center",
                         background="white", fg="black").grid(row=29, column=1, columnspan=2, rowspan=4, sticky="nsew")

        # TABLA DATOS DEXA HORIZONTAL------------------------------------------------------------------------------------

        label = tk.Label(self, font=FUENTE1, anchor="center", background="white", fg="black").grid(row=29, column=3,
                                                                                                   sticky="nsew")
        label = tk.Label(self, text="DMO (g/cm²)", font=FUENTE1, anchor="center", background="#e0e0e0",
                         fg="black").grid(row=29, column=4, sticky="nsew")
        label = tk.Label(self, text="T-SCORE", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(
            row=29, column=5, sticky="nsew")
        label = tk.Label(self, text="Z-SCORE", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(
            row=29, column=6, sticky="nsew")

        # TABLA DATOS DEXA VERTICAL-------------------------------------------------------------------------------------

        label = tk.Label(self, text="L1-L4", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(
            row=30, column=3, sticky="nsew")
        label = tk.Label(self, text="Cuello Femoral", font=FUENTE1, anchor="center", background="#e0e0e0",
                         fg="BLACK").grid(row=31, column=3, sticky="nsew")
        label = tk.Label(self, text="Trocánter", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(
            row=32, column=3, sticky="nsew")

        # INGRESO DE DATOS LUMBAR --------------------------------------------------------------------------------------

        l1 = tk.StringVar()
        l2 = tk.StringVar()
        l3 = tk.StringVar()
        lumbar_dmo = tk.Entry(self, textvariable=l1, font=FUENTE1, background="white", fg="black", width=1,
                              justify="center")
        lumbar_dmo.grid(row=30, column=4, sticky="nsew")
        lumbar_dmo.focus_set()

        lumbar_tscore = tk.Entry(self, textvariable=l2, font=FUENTE1, background="white", fg="black", width=1,
                                 justify="center")
        lumbar_tscore.grid(row=30, column=5, sticky="nsew")
        lumbar_tscore.focus_set()

        lumbar_zcore = tk.Entry(self, textvariable=l3, font=FUENTE1, background="WHITE", fg="black", width=1,
                                justify="center")
        lumbar_zcore.grid(row=30, column=6, sticky="nsew")
        lumbar_zcore.focus_set()

        # INGRESO DE DATOS CUELLO --------------------------------------------------------------------------------------

        c1 = tk.StringVar()
        c2 = tk.StringVar()
        c3 = tk.StringVar()

        cuello_dmo = tk.Entry(self, textvariable=c1, font=FUENTE1, background="white", fg="black", width=1,
                              justify="center")
        cuello_dmo.grid(row=31, column=4, sticky="nsew")
        cuello_dmo.focus_set()

        cuello_tscore = tk.Entry(self, textvariable=c2, font=FUENTE1, background="white", fg="black", width=1,
                                 justify="center")
        cuello_tscore.grid(row=31, column=5, sticky="nsew")
        cuello_tscore.focus_set()

        cuello_zcore = tk.Entry(self, textvariable=c3, font=FUENTE1, background="white", fg="black", width=1,
                                justify="center")
        cuello_zcore.grid(row=31, column=6, sticky="nsew")
        cuello_zcore.focus_set()

        # INGRESO DE TROCANTER --------------------------------------------------------------------------------------

        t1 = tk.StringVar()
        t2 = tk.StringVar()
        t3 = tk.StringVar()

        trocanter_dmo = tk.Entry(self, textvariable=t1, font=FUENTE1, background="white", fg="black", width=1,
                                 justify="center")
        trocanter_dmo.grid(row=32, column=4, sticky="nsew")
        trocanter_dmo.focus_set()

        trocanter_tscore = tk.Entry(self, textvariable=t2, font=FUENTE1, background="white", fg="black", width=1,
                                    justify="center")
        trocanter_tscore.grid(row=32, column=5, sticky="nsew")
        trocanter_tscore.focus_set()

        trocanter_zcore = tk.Entry(self, textvariable=t3, font=FUENTE1, background="white", fg="black", width=1,
                                   justify="center")
        trocanter_zcore.grid(row=32, column=6, sticky="nsew")
        trocanter_zcore.focus_set()

        row = tk.Label(self, bg="white").grid(row=33, column=7, ipadx=80, ipady=18)

        def update():
            arr_upd = []
            arr_upd.append(talla.get())
            arr_upd.append(peso.get())
            arr_upd.append(caidas.get())
            arr_upd.append(fracturas.get())
            arr_upd.append(l1.get())
            arr_upd.append(l2.get())
            arr_upd.append(l3.get())
            arr_upd.append(c1.get())
            arr_upd.append(c2.get())
            arr_upd.append(c3.get())
            arr_upd.append(t1.get())
            arr_upd.append(t2.get())
            arr_upd.append(t3.get())

            controller.get_pacientes().update(controller.get_paciente(), arr_upd)
            controller.show_frame(MostradorResultados)

        #   BOTON FINALIZAR-----------------------------------------------------------------------------------------
        button = tk.Button(self, text="REGISTRAR", font=FUENTE16, relief="groove", borderwidth=2, height=1,
                           command=lambda: update())
        button.grid(row=34, column=5, columnspan=2, ipadx=27)

        row = tk.Label(self, bg="white").grid(row=35, column=7, ipadx=80, ipady=5)

        #   PIE DE PAGINA--------------------------------------------------------------------

        pie = tk.Label(self,
                       text="* Excluyendo fracturas de alto impacto. Por ejemplo, no accidentes de carros."
                            "                                                                  \n** Por ejemplo"
                            ", diabetes tipo I, hipertiroidismo no tratado durante largo tiempo, malnutrición "
                            "o hepatopatía crónica.",
                       font=FUENTEPIE, bg="white", anchor="w").grid(row=36, column=1, columnspan=5, sticky="nsew")

        botonRegresar = tk.Button(self, text="←", font=FUENTEFLECHA, relief="groove", borderwidth=2, width=5, height=1,
                                  command=lambda: controller.show_frame(HistoriaPacienteAntiguo), bg="white")
        botonRegresar.place(x=10, y=10)


class MostradorResultados(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="WHITE")

        #   columns----------------------------------------------------------------------------------------------------
        columna0 = tk.Label(self, bg="white").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="white").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="white").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="white").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="white").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="white").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="white").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="white").grid(row=0, column=7, ipadx=80)

        #   row1 ------------------------------------------------------------------------------------------------------
        row = tk.Label(self, bg="white").grid(row=1, column=7, ipadx=80, ipady=15)

        #   RESULTADOS DEL 20/05/2013----------------------------------------------------------------------------
        label = tk.Label(self, text="  RESULTADOS DEL 09/12/2020", font=FUENTE13, background="#5b9fc9", anchor="w",
                         fg="white").grid(row=2, column=1, columnspan=6, sticky="NSEW")
        row = tk.Label(self, bg="white").grid(row=5, column=7, ipadx=80, ipady=0)

        resultado = tk.Label(self, text=" Presiona refresh para obtener los datos actualizados.*", font=FUENTE11,
                             bg="white", anchor="w").grid(row=14, column=1, columnspan=5, sticky="nsew")
        resultado = tk.Label(self, text="    2. Existe un 30% de riesgo de fractura en los próximos"
                                        " 10 años, según su densidad mineral ósea de cuello femoral.**",
                             font=FUENTE11, bg="white", anchor="w").grid(row=15, column=1, columnspan=6, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=16, column=7, ipadx=80, ipady=5)

        #   RECOMENDACIONES----------------------------------------------------------------------------
        label = tk.Label(self, text="  RECOMENDACIONES", font=FUENTE13, background="#5b9fc9", anchor="w",
                         fg="white").grid(row=18, column=1, columnspan=6, sticky="NSEW")
        row = tk.Label(self, bg="white").grid(row=19, column=7, ipadx=80, ipady=0)

        recomendaciones = tk.Label(self, text="    1. Asistir con un médico especializado.", font=FUENTE11,
                                   bg="white", anchor="w").grid(row=21, column=1, columnspan=5, sticky="nsew")
        recomendaciones = tk.Label(self,
                                   text="    2. Ingerir alimentos ricos en vitamina D y calcio, como pescados, lacteos y huevos.",
                                   font=FUENTE11, bg="white", anchor="w").grid(row=22, column=1, columnspan=6,
                                                                               sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=24, column=7, ipadx=80, ipady=5)

        #   DEXA----------------------------------------------------------------------------
        label = tk.Label(self, text="  DATOS DE DENSITOMETRÍA INGRESADOS", font=FUENTE13, background="#5b9fc9",
                         anchor="w", fg="white").grid(row=25, column=1, columnspan=6, sticky="NSEW")
        row = tk.Label(self, bg="white").grid(row=26, column=7, ipadx=80, ipady=8)

        # TABLA DATOS DEXA HORIZONTAL------------------------------------------------------------------------------------

        label = tk.Label(self, font=FUENTE1, anchor="center", background="white", fg="black").grid(row=29, column=2,
                                                                                                   sticky="nsew")
        label = tk.Label(self, text="DMO (g/cm²)", font=FUENTE1, anchor="center", background="#e0e0e0",
                         fg="black").grid(row=29,
                                          column=3,
                                          sticky="nsew")
        label = tk.Label(self, text="T-SCORE", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(
            row=29, column=4, sticky="nsew")
        label = tk.Label(self, text="Z-SCORE", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(
            row=29, column=5, sticky="nsew")

        # TABLA DATOS DEXA VERTICAL-------------------------------------------------------------------------------------


        label = tk.Label(self, text="L1-L4", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(
            row=30, column=2, sticky="nsew")
        label = tk.Label(self, text="Cuello Femoral", font=FUENTE1, anchor="center", background="#e0e0e0",
                         fg="BLACK").grid(row=31, column=2, sticky="nsew")
        label = tk.Label(self, text="Trocánter", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(
            row=32, column=2, sticky="nsew")
        tk.Label(self, bg="white").grid(row=36, column=4, columnspan=2, sticky="nsew")
        def view_update_scores():

            #lectura de densitometria
            t_score = float(controller.get_paciente().cuello[1])
            frac = float(controller.get_paciente().F)
            tk.Label(self, text="  .*", font=FUENTE11,
                     bg="white", anchor="w").grid(row=14, column=1, columnspan=5, sticky="nsew")
            if(t_score<=1 and t_score>-1):
                tk.Label(self, text="   1. Estado oseo es el adecuado*", font=FUENTE11, bg="white",fg="green", anchor="w").grid(row=14, column=1, columnspan=5, sticky="nsew")
            else:
                if(t_score<=-1 and t_score>-2.5):
                    tk.Label(self, text="   1. Osteopenia.*", font=FUENTE11, bg="white",fg="yellow", anchor="w").grid(row=14,column=1, columnspan=5,sticky="nsew")
                else:
                    if(t_score<=-2.5 and frac>=1):
                             tk.Label(self, text="   1. Osteoporosis severa.*", font=FUENTE11, bg="white",fg="red",anchor="w").grid(row=14, column=1, columnspan=5, sticky="nsew")
                    else:
                        if(t_score<=-2.5):
                            tk.Label(self, text="   1.  Osteoporosis.*", font=FUENTE11, bg="white",fg="orange",anchor="w").grid(row=14, column=1, columnspan=5, sticky="nsew")

            #mostrar recomendiciones
            if (t_score <= 1 and t_score > -1):
                tk.Label(self, text="   1. Utilizar alfombras antideslizante y Acomodar cables sueltos que interrumpan el paso.", font=FUENTE11, bg="white", anchor="w").grid(row=21, column=1, columnspan=5, sticky="nsew")
                tk.Label(self,text="2. Instalar pasamanos e iluminar en ambientes recurrentes de casa.\n 3. Ingesta de alimentos que aportan vitamina D ,como lo son los productos lácetos, cerelaes y pescados grasos(salmon,sardinas,atún)",font=FUENTE11, bg="white", anchor="w").grid(row=22, column=1, columnspan=6,sticky="nsew")
            else:
                if(t_score<=-1 and t_score>-2.5):
                    tk.Label(self, text="    1. Ingerir alimentos ricos en vitD y calcio(pescados,lacteos,huevos,etc)",font=FUENTE11, bg="white", anchor="w").grid(row=21, column=1, columnspan=5, sticky="nsew")
                    tk.Label(self, text="    2. Instalar pasamanos e iluminar en ambientes recurrentes de casa.", font=FUENTE11, bg="white", anchor="w").grid(row=22, column=1, columnspan=6, sticky="nsew")
                else:
                    #***cambio de texto***
                    if (t_score<=-2.5 and frac>0):
                            tk.Label(self, text="   1. Ingerir alimentos ricos en vitD y calcio(pescados,lacteos,huevos,etc)\n2. no tome trago", font=FUENTE11, bg="white",anchor="w").grid(row=21, column=1, columnspan=5, sticky="nsew")
                            tk.Label(self,text="    3. Asistir con un médico especializado para mejores recomendaciones",font=FUENTE11, bg="white", anchor="w").grid(row=22, column=1, columnspan=6,sticky="nsew")
                    else:
                        if(t_score<=-2.5):
                            tk.Label(self, text="    1. Salir a caminar de 10-15 min acompañado \n 2.Ingesta de alimentos que aportan vitamina D ,como lo son los productos lácetos, cerelaes y pescados grasos(salmon,sardinas,atún)",font=FUENTE11, bg="white", anchor="w").grid(row=21, column=1, columnspan=5, sticky="nsew")
                            tk.Label(self, text="    3. Ingerir alimentos ricos en vitD y calcio(pescados,lacteos,huevos,etc)",font=FUENTE11, bg="white", anchor="w").grid(row=22, column=1, columnspan=6,sticky="nsew")
                            #tk.Label(self,text="    3. Ingerir alimentos ricos en vitD y calcio(pescados,lacteos,huevos,etc)",font=FUENTE11, bg="pink", anchor="w").grid(row=23, column=1, columnspan=6,sticky="nsew")

            #mostrar prediccion
            prediccion=float(controller.get_paciente().riesgo)
            tk.Label(self, text="    2. Existe un\" "+ str(prediccion) + "\"% de riesgo de fractura en los próximos"
                                " 10 años, según su densidad mineral ósea de cuello femoral.**",
                     font=FUENTE11, bg="white", anchor="w").grid(row=15, column=1, columnspan=6, sticky="nsew")
            # lumbar_dmo =
            tk.Label(self, text=controller.get_paciente().l1_l4[0], font=FUENTE1, background="white", fg="black",
                     width=1,
                     justify="center").grid(
                row=30, column=3, sticky="nsew")
            # lumbar_tscore =
            tk.Label(self, text=controller.get_paciente().l1_l4[1], font=FUENTE1, background="white", fg="black",
                     width=1,
                     justify="center").grid(
                row=30, column=4, sticky="nsew")
            # lumbar_zcore =
            tk.Label(self, text=controller.get_paciente().l1_l4[2], font=FUENTE1, background="WHITE", fg="black",
                     width=1,
                     justify="center").grid(
                row=30, column=5, sticky="nsew")
            # cuello_dmo =
            tk.Label(self, text=controller.get_paciente().cuello[0], font=FUENTE1, background="white", fg="black",
                     width=1,
                     justify="center").grid(
                row=31, column=3, sticky="nsew")
            # cuello_tscore =
            tk.Label(self, text=controller.get_paciente().cuello[1], font=FUENTE1, background="white", fg="black",
                     width=1,
                     justify="center").grid(
                row=31, column=4, sticky="nsew")
            # cuello_zcore =
            tk.Label(self, text=controller.get_paciente().cuello[2], font=FUENTE1, background="white", fg="black",
                     width=1,
                     justify="center").grid(
                row=31, column=5, sticky="nsew")
            # trocanter_dmo =
            tk.Label(self, text=controller.get_paciente().trocanter[0], font=FUENTE1, background="white", fg="black",
                     width=1,
                     justify="center").grid(
                row=32, column=3, sticky="nsew")
            # trocanter_tscore =
            tk.Label(self, text=controller.get_paciente().trocanter[1], font=FUENTE1, background="white", fg="black",
                     width=1,
                     justify="center").grid(
                row=32, column=4, sticky="nsew")
            # trocanter_zcore =
            tk.Label(self, text=controller.get_paciente().trocanter[2], font=FUENTE1, background="white", fg="black",
                     width=1,
                     justify="center").grid(
                row=32, column=5, sticky="nsew")
            # fracturasFragilidad =
            tk.Label(self, text=controller.get_paciente().F, font=FUENTE1, anchor="center", background="#e0e0e0",
                     fg="black").grid(row=35, column=4, columnspan=2, sticky="nsew")

        def guardar_cambios():
            if (controller.get_paciente().guardado == 0):
                controller.get_paciente().guardado = 1
                controller.get_pacientes().save()
            else:
                fracturasFragilidad = tk.Label(self, text="Usted ya guardó los cambios", font=FUENTE1, anchor="center",fg="black").grid(row=36, column=4, columnspan=2, sticky="nsew")

        # INGRESO DE DATOS LUMBAR --------------------------------------------------------------------------------------

        lumbar_dmo = tk.Label(self, text="", font=FUENTE1, background="white", fg="black", width=1,
                              justify="center").grid(
            row=30, column=3, sticky="nsew")
        lumbar_tscore = tk.Label(self, text="", font=FUENTE1, background="white", fg="black", width=1,
                                 justify="center").grid(
            row=30, column=4, sticky="nsew")
        lumbar_zcore = tk.Label(self, text="", font=FUENTE1, background="WHITE", fg="black", width=1,
                                justify="center").grid(
            row=30, column=5, sticky="nsew")

        # INGRESO DE DATOS CUELLO --------------------------------------------------------------------------------------

        cuello_dmo = tk.Label(self, text="", font=FUENTE1, background="white", fg="black", width=1,
                              justify="center").grid(
            row=31, column=3, sticky="nsew")
        cuello_tscore = tk.Label(self, text="", font=FUENTE1, background="white", fg="black", width=1,
                                 justify="center").grid(
            row=31, column=4, sticky="nsew")
        cuello_zcore = tk.Label(self, text="", font=FUENTE1, background="white", fg="black", width=1,
                                justify="center").grid(
            row=31, column=5, sticky="nsew")

        # INGRESO DE TROCANTER --------------------------------------------------------------------------------------

        trocanter_dmo = tk.Label(self, text="", font=FUENTE1, background="white", fg="black", width=1,
                                 justify="center").grid(
            row=32, column=3, sticky="nsew")
        trocanter_tscore = tk.Label(self, text="", font=FUENTE1, background="white", fg="black", width=1,
                                    justify="center").grid(
            row=32, column=4, sticky="nsew")
        trocanter_zcore = tk.Label(self, text="", font=FUENTE1, background="white", fg="black", width=1,
                                   justify="center").grid(
            row=32, column=5, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=33, column=6, ipadx=80, ipady=8)

        # FRACTURAS FRAGILIDAD --------------------------------------------------------------------------------------

        fracturasFragilidad = tk.Label(self, text="Fracturas por fragilidad:", font=FUENTE1, anchor="e",
                                       background="#e0e0e0", fg="black").grid(row=35, column=2, columnspan=2,
                                                                              sticky="nsew")
        fracturasFragilidad = tk.Label(self, text="1", font=FUENTE1, anchor="center", background="#e0e0e0",
                                       fg="black").grid(row=35, column=4, columnspan=2, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=36, column=6, ipadx=80, ipady=30)

        pie = tk.Label(self,
                       text="* Según el menor valor de t-score de su densitometría.\n      ** Basado en © Calculadora de Riesgo de Fractura Garvan.",
                       font=FUENTEPIE, bg="white", anchor="w").grid(row=40, column=1, columnspan=5, sticky="nsew")

        # BOTONES-------------------------
        boton_reload = tk.Button(self, text="Refresh", font=FUENTEFLECHA, relief="groove", borderwidth=2, width=5,
                                 height=1,
                                 command=lambda: view_update_scores(), bg="white")
        boton_reload.grid(row=37, column=5, columnspan=2, ipadx=27, pady=35)

        boton_save = tk.Button(self, text="Guardar", font=FUENTEFLECHA, relief="groove", borderwidth=2,
                               width=5, height=1,
                               command=lambda: guardar_cambios(), bg="white")
        boton_save.grid(row=37, column=2, columnspan=2, ipadx=27, pady=35)

        botonRegresar = tk.Button(self, text="←", font=FUENTEFLECHA, relief="groove", borderwidth=2, width=5, height=1,
                                  command=lambda: controller.show_frame(HistoriaPacienteAntiguo), bg="white")
        botonRegresar.place(x=10, y=10)


class BuscadorDNI(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background="white")

        def search():
            dni = my_dni.get()

            if controller.pacientes.find_paciente(dni):
                controller.set_paciente(controller.pacientes.pacientes[dni])
                controller.get_paciente().guardado = 1
                controller.show_frame(HistoriaPacienteAntiguo)
            else:
                button1 = tk.Button(self, text="BUSCAR", font=FUENTE35, relief="groove", borderwidth=2, height=1,
                                    command=lambda: search())
                button1.grid(row=6, column=5, columnspan=2, ipadx=30)
                label_error = tk.Label(self, text="No existe el usuario ¡Intente de nuevo por favor!", font=FUENTE21,
                                       anchor="center").grid(row=5, column=3, columnspan=6, sticky="NSEW", ipady=5)

        columna0 = tk.Label(self, bg="WHITE").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="WHITE").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="WHITE").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="WHITE").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="WHITE").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="WHITE").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="WHITE").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="WHITE").grid(row=0, column=7, ipadx=80)

        # dni_entry_box = tk.Entry(self, textvariable=my_dni, width=22, font=FUENTE1, show="*", bg="white")
        # dni_entry_box.focus_set()
        # dni_entry_box.pack(ipady=7, pady=20)

        row1 = tk.Label(self, bg="white").grid(row=1, column=7, sticky="nsew", ipadx=80, ipady=50)

        label1 = tk.Label(self, text="Ingrese el DNI del paciente", font=FUENTE35, background="#5b9fc9",
                          anchor="center", fg="white").grid(row=2, column=1, columnspan=6, sticky="NSEW", ipady=10)

        row3 = tk.Label(self, bg="white").grid(row=3, column=7, sticky="nsew", ipadx=80, ipady=17)

        my_dni = tk.StringVar()
        dni_entry_box = tk.Entry(self, textvariable=my_dni, font=FUENTE35, background="white", width=20,
                                 justify="right", fg="black")
        dni_entry_box.grid(row=4, column=1, columnspan=3, sticky="e")
        dni_entry_box.focus_set()

        row4 = tk.Label(self, bg="white").grid(row=5, column=7, sticky="nsew", ipadx=80, ipady=17)

        button1 = tk.Button(self, text="BUSCAR", font=FUENTE35, relief="groove", borderwidth=2, height=1,
                            command=lambda: search())
        button1.grid(row=6, column=5, columnspan=2, ipadx=30)

        botonRegresar = tk.Button(self, text="←", font=FUENTEFLECHA, relief="groove", borderwidth=2, width=5, height=1,
                                  bg="white", command=lambda: controller.show_frame(Ramas))
        botonRegresar.place(x=10, y=10)


class HistoriaPacienteAntiguo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")

        #   columns---------------------------------------------------------------------------------------------------
        columna0 = tk.Label(self, bg="white").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="white").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="white").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="white").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="white").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="white").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="white").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="white").grid(row=0, column=7, ipadx=80)

        #   row1 ------------------------------------------------------------------------------------------------------
        row1 = tk.Label(self, bg="white").grid(row=1, column=7, ipadx=80, ipady=0)

        #   APELLIDOS Y NOMBRES DEL PACIENTE---------------------------------------------------------------------------
        label1 = tk.Label(self, text="  PACIENTE", font=FUENTE13, background="#5b9fc9",
                          anchor="w", fg="white").grid(row=2, column=1, columnspan=6, sticky="NSEW", )

        row3 = tk.Label(self, bg="white").grid(row=3, column=7, ipadx=80, ipady=0)

        nombreNuevoPaciente = tk.Label(self, text=" ", font=FUENTE25, bg="white", width=1).grid(row=4,
                                                                                                column=1,
                                                                                                columnspan=3,
                                                                                                sticky="NSEW")

        row5 = tk.Label(self, bg="white").grid(row=5, column=7, ipadx=80, ipady=0)

        #   DATOS PERSONALES-------------------------------------------------------------------------------------------
        label2 = tk.Label(self, text="  DATOS PERSONALES", font=FUENTE13, background="#5b9fc9", anchor="w", fg="white")
        label2.grid(row=6, column=1, columnspan=6, sticky="NSEW", )

        row7 = tk.Label(self, bg="white").grid(row=7, column=7, ipadx=80)

        #   DNI
        label3 = tk.Label(self, text="DNI: ", font=FUENTE21, anchor="e", bg="white").grid(row=8, column=1,
                                                                                          sticky="nsew")
        dniNuevoPaciente = tk.Label(self, text="", font=FUENTE1, bg="white", width=1).grid(row=8, column=2,
                                                                                           sticky="nsew")

        #   EDAD
        label4 = tk.Label(self, text="Edad: ", font=FUENTE21, anchor="e", bg="white").grid(row=8, column=3,
                                                                                           sticky="nsew")
        nacimientoNuevoPaciente = tk.Label(self, text="", font=FUENTE1, bg="white", width=1).grid(row=8, column=4,
                                                                                                  sticky="nsew")

        #  SEXO
        label7 = tk.Label(self, text="Sexo:", font=FUENTE21, anchor="e", background="white").grid(row=8, column=5,
                                                                                                  sticky="nsew")
        sexo = tk.Label(self, text="", font=FUENTE1, bg="white", width=1).grid(row=8, column=6, sticky="nsew")

        row11 = tk.Label(self, bg="white").grid(row=11, column=7, ipadx=80)

        #   ANTECEDENTES--------------------------------------------------------------------------------------------
        label9 = tk.Label(self, text="  HISTORIAL DE CONSULTAS", font=FUENTE13, background="#5b9fc9", anchor="w",
                          fg="white")
        label9.grid(row=12, column=1, columnspan=6, sticky="NSEW", )

        row19 = tk.Label(self, bg="white").grid(row=19, column=7, ipadx=80)

        #   DNI
        tabla1 = tk.Label(self, text="F. examen", font=FUENTE1, anchor="center", background="#e0e0e0").grid(
            row=20, column=1, sticky="nsew")
        tabla2 = tk.Label(self, text="ESTADO ÓSEO", font=FUENTE1, anchor="center", background="#e0e0e0").grid(
            row=20, column=5, sticky="nsew")
        tabla3 = tk.Label(self, text="T-score Lumbar", font=FUENTE1, anchor="center", background="#e0e0e0").grid(
            row=20, column=2, sticky="nsew")
        tabla4 = tk.Label(self, text="T-score Cuello F.", font=FUENTE1, anchor="center", background="#e0e0e0").grid(
            row=20, column=3, sticky="nsew")
        tabla5 = tk.Label(self, text="DMO Cuello F.(g/cm^3 )", font=FUENTE1, anchor="center", background="#e0e0e0").grid(
            row=20, column=4, sticky="nsew")
        tabla6 = tk.Label(self, text="RESULTADOS", font=FUENTE1, anchor="center", background="#e0e0e0").grid(row=20,
                                                                                                             column=6,
                                                                                                             sticky="nsew")

        #   Formato 1---
        fechaVariable1 = tk.Label(self, text="", font=FUENTE1, bg="white", width=1, relief="solid", borderwidth=1)
        fechaVariable1.grid(row=21, column=1, sticky="nsew")

        estadoVariable1 = tk.Label(self, text="-", font=FUENTE1, bg="white", width=1, relief="solid",
                                   borderwidth=1)
        estadoVariable1.grid(row=21, column=5, sticky="nsew")

        dmolumbarVariable = tk.Label(self, text="-", font=FUENTE1, bg="white", width=1, relief="solid",borderwidth=1)
        dmolumbarVariable.grid(row=21, column=2, sticky="nsew")

        dmocuelloVariable = tk.Label(self, text="-", font=FUENTE1, bg="white", width=1, relief="solid",borderwidth=1)
        dmocuelloVariable.grid(row=21, column=3, sticky="nsew")

        imcVariable = tk.Label(self, text="-", font=FUENTE1, bg="white", width=1, relief="solid",borderwidth=1)
        imcVariable.grid(row=21, column=4, sticky="nsew")

        detalleVariable1 = tk.Button(self, text="Detalle...", font=FUENTE1, bg="white", width=1, relief="solid",
                                     borderwidth=1, command=lambda: controller.show_frame(MostradorResultados))
        detalleVariable1.grid(row=21, column=6, sticky="nsew")

        # Custom Functions
        def update_labels():
            print("Final:")

            controller.get_paciente().show_stats()
            # name
            tk.Label(self, text=controller.get_paciente().apellido + " " + controller.get_paciente().N, font=FUENTE25,
                     bg="white", width=1).grid(row=4, column=1, columnspan=3, sticky="NSEW")
            # dni
            tk.Label(self, text=controller.get_paciente().dni, font=FUENTE1, bg="white", width=1).grid(row=8, column=2,
                                                                                                       sticky="nsew")
            # edad
            tk.Label(self, text=controller.get_paciente().E, font=FUENTE1, bg="white", width=1).grid(row=8, column=4,
                                                                                                     sticky="nsew")
            # sexo
            tk.Label(self, text=controller.get_paciente().sexo, font=FUENTE1, bg="white", width=1).grid(row=8, column=6,
                                                                                                        sticky="nsew")
            # FEcha_nac
            tk.Label(self, text='05/11/20', font=FUENTE1, bg="white", width=1,
                     relief="solid", borderwidth=1).grid(row=21, column=1, sticky="nsew")
            # resultado_osteoporosis
            t_score_1 = float(controller.get_paciente().cuello[1])
            frac_1 = float(controller.get_paciente().F)
            if (t_score_1 <= 1 and t_score_1 > -1):
                tk.Label(self, text='sin osteoporosis', font=FUENTE1, bg="white", width=1, relief="solid", borderwidth=1).grid(row=21, column=5, sticky="nsew")
            else:
                if (t_score_1 <= -1 and t_score_1 > -2.5):
                    tk.Label(self, text='osteopenia', font=FUENTE1, bg="white", width=1,relief="solid", borderwidth=1).grid(row=21, column=5, sticky="nsew")
                else:
                    if (t_score_1 <= -2.5 and frac_1 >= 1):
                        tk.Label(self, text='osteoporosis grave', font=FUENTE1, bg="white", width=1, relief="solid", borderwidth=1).grid(row=21, column=5, sticky="nsew")
                    else:
                        if (t_score_1 <= -2.5):
                            tk.Label(self, text='osteoporosis', font=FUENTE1, bg="white",width=1, relief="solid", borderwidth=1).grid(row=21, column=5, sticky="nsew")

         #c    # T-score L1_L4

            tk.Label(self, text=controller.get_paciente().l1_l4[1], font=FUENTE1, bg="white", width=1, relief="solid",borderwidth=1).grid(row=21, column=2, sticky="nsew")

         #a   # T-score Cuello femoral

            tk.Label(self, text=controller.get_paciente().cuello[1], font=FUENTE1, bg="white", width=1, relief="solid",borderwidth=1).grid(row=21, column=3, sticky="nsew")

        #b # DMO Cuello femoral

            tk.Label(self, text=controller.get_paciente().cuello[0], font=FUENTE1, bg="white", width=1, relief="solid",borderwidth=1).grid(row=21, column=4, sticky="nsew")

        #   BOTON PARA update STATS
        button1 = tk.Button(self, text='Refresh', font=FUENTEFLECHA, relief="groove", borderwidth=2, height=1,
                            command=lambda: update_labels())
        button1.grid(row=39, column=2, columnspan=2, ipadx=27, pady=35)

        #   BOTON FINALIZAR----------------------------------------------------------------------------------------
        button1 = tk.Button(self, text="ACTUALIZAR DATOS", font=FUENTE16, relief="groove", borderwidth=2, height=1,
                            command=lambda: controller.show_frame(ActualizarRegistroNuevo))
        button1.grid(row=39, column=5, columnspan=2, ipadx=27, pady=35)

        botonRegresar = tk.Button(self, text="←", font=FUENTEFLECHA, relief="groove", borderwidth=2, width=5, height=1,
                                  command=lambda: controller.show_frame(Ramas), bg="white")
        botonRegresar.place(x=10, y=10)


class RegistrarNuevoPaciente(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="WHITE")

        caracteristicas = []

        #   columnas-------------------------------------------------------------------------
        columna0 = tk.Label(self, bg="white").grid(row=0, column=0, ipadx=80)
        columna1 = tk.Label(self, bg="white").grid(row=0, column=1, ipadx=80)
        columna2 = tk.Label(self, bg="white").grid(row=0, column=2, ipadx=80)
        columna3 = tk.Label(self, bg="white").grid(row=0, column=3, ipadx=80)
        columna4 = tk.Label(self, bg="white").grid(row=0, column=4, ipadx=80)
        columna5 = tk.Label(self, bg="white").grid(row=0, column=5, ipadx=80)
        columna6 = tk.Label(self, bg="white").grid(row=0, column=6, ipadx=80)
        columna7 = tk.Label(self, bg="white").grid(row=0, column=7, ipadx=80)

        #   separador ---------------------------------------------------------------------------------
        fila1 = tk.Label(self, bg="white").grid(row=1, column=7, ipadx=80, ipady=0)

        #   DATOS PERSONALES-------------------------------------------------------------------------------------------
        label = tk.Label(self, text="  DATOS PERSONALES", font=FUENTE13, background="#5b9fc9", anchor="w",
                         fg="white").grid(row=2, column=1, columnspan=6, sticky="NSEW")

        row = tk.Label(self, bg="white").grid(row=3, column=7, ipadx=80)

        #   NOMBRE
        label = tk.Label(self, text="Nombres: ", font=FUENTE1, anchor="e", bg="white").grid(row=5, column=1,
                                                                                            sticky="nsew")
        nombre = tk.StringVar()
        nombreVariable = tk.Entry(self, textvariable=nombre, font=FUENTE1, bg="white", width=1)
        nombreVariable.grid(row=5, column=2, sticky="nsew")
        # nombreVariable.focus_set()

        #   APELLIDO
        label = tk.Label(self, text="Apellidos: ", font=FUENTE1, anchor="e", bg="white").grid(row=5, column=3,
                                                                                              sticky="nsew")
        apellido = tk.StringVar()
        apellidoVariable = tk.Entry(self, textvariable=apellido, font=FUENTE1, bg="white", width=1)
        apellidoVariable.grid(row=5, column=4, sticky="nsew")
        # apellidoVariable.focus_set()

        #   SEXO
        label = tk.Label(self, text="Sexo:", font=FUENTE1, anchor="e", background="white").grid(row=5, column=5,
                                                                                                sticky="nsew")
        sexoVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Masculino", variable=sexoVariable, value=1, font=FUENTE1, anchor="w",
                                bg="white").grid(row=5, column=6, sticky="nsew", padx=5)
        boton2 = tk.Radiobutton(self, text="Femenino", variable=sexoVariable, value=2, font=FUENTE1, anchor="w",
                                bg="white").grid(row=6, column=6, sticky="nsew", padx=5)
        # EDAD
        tk.Label(self, text="Edad: ", font=FUENTE1, anchor="e", bg="white").grid(row=8, column=5,
                                                                                 sticky="nsew")
        edad = tk.StringVar()
        edadVariable = tk.Entry(self, textvariable=edad, font=FUENTE1, bg="white", width=1)
        edadVariable.grid(row=8, column=6, sticky="nsew")

        #   DNI
        label = tk.Label(self, text="DNI: ", font=FUENTE1, anchor="e", bg="white").grid(row=8, column=1, sticky="nsew")
        dni = tk.StringVar()
        dniVariable = tk.Entry(self, textvariable=dni, font=FUENTE1, bg="white", width=1)
        dniVariable.grid(row=8, column=2, sticky="nsew")
        dniVariable.focus_set()

        #   NACIMIENTO
        label = tk.Label(self, text="F. Nacimiento: ", font=FUENTE1, anchor="e", bg="white").grid(row=8, column=3,
                                                                                                  sticky="nsew")
        nacimiento = tk.StringVar()
        nacimientoVariable = tk.Entry(self, textvariable=nacimiento, font=FUENTE1, bg="white", width=1)
        nacimientoVariable.grid(row=8, column=4, sticky="nsew")
        nacimientoVariable.focus_set()

        label = tk.Label(self, text="(DD/MM/AAAA) ", font=FUENTE14, anchor="ne", bg="white").grid(row=9, column=3,
                                                                                                  sticky="nsew")

        #   DEPARTAMENTO
        label = tk.Label(self, text="Departamento: ", font=FUENTE1, anchor="e", bg="white").grid(row=6, column=1,
                                                                                                 sticky="nsew")
        departamento = tk.StringVar()
        departamentoVariable = tk.Entry(self, textvariable=departamento, font=FUENTE1, bg="white", width=1)
        departamentoVariable.grid(row=6, column=2, sticky="nsew")
        departamentoVariable.focus_set()

        #   CIUDAD
        label = tk.Label(self, text="Ciudad: ", font=FUENTE1, anchor="e", bg="white").grid(row=6, column=3,
                                                                                           sticky="nsew")
        ciudad = tk.StringVar()
        ciudadVariable = tk.Entry(self, textvariable=ciudad, font=FUENTE1, bg="white", width=1)
        ciudadVariable.grid(row=6, column=4, sticky="nsew")
        ciudadVariable.focus_set()

        row10 = tk.Label(self, bg="white").grid(row=10, column=7, ipadx=80)

        #   PRIMERA CONSULTA---------------------------------------------------------------------------------------------
        label = tk.Label(self, text="  PRIMERA CONSULTA", font=FUENTE13, background="#5b9fc9", anchor="w",
                         fg="white").grid(row=12, column=1, columnspan=6, sticky="NSEW", )

        row = tk.Label(self, bg="white").grid(row=13, column=7, ipadx=80)

        #   TALLA
        label = tk.Label(self, text=" Talla (cm):", font=FUENTE1, anchor="e", bg="white").grid(row=15, column=1,
                                                                                               columnspan=2,
                                                                                               sticky="nsew")
        talla = tk.StringVar()
        tallaVariable = tk.Entry(self, textvariable=talla, font=FUENTE1, bg="white", width=1)
        tallaVariable.grid(row=15, column=3, sticky="nsew")
        tallaVariable.focus_set()
        #   PESO
        label = tk.Label(self, text=" Peso (kg):", font=FUENTE1, anchor="e", bg="white").grid(row=15, column=4,
                                                                                              columnspan=2,
                                                                                              sticky="nsew")
        peso = tk.StringVar()
        pesoVariable = tk.Entry(self, textvariable=peso, font=FUENTE1, bg="white", width=1)
        pesoVariable.grid(row=15, column=6, sticky="nsew")
        pesoVariable.focus_set()

        #   CAIDAS ANTERIORES
        label = tk.Label(self, text="Número de fracturas luego de los 50 años* :", font=FUENTE1, anchor="e",
                         bg="white").grid(row=17, column=1, columnspan=2, sticky="nsew")
        caidas = tk.StringVar()
        caidasVariable = tk.Entry(self, textvariable=caidas, font=FUENTE1, bg="white", width=1)
        caidasVariable.grid(row=17, column=3, sticky="nsew")
        caidasVariable.focus_set()
        #   FRACTURAS ANTERIORES
        label = tk.Label(self, text="Número de caídas en el último año:", font=FUENTE1, anchor="e", bg="white").grid(
            row=17, column=4, columnspan=2, sticky="nsew")

        fracturas = tk.StringVar()
        fracturasVariables = tk.Entry(self, textvariable=fracturas, font=FUENTE1, bg="white", width=1)
        fracturasVariables.grid(row=17, column=6, sticky="nsew")
        fracturasVariables.focus_set()

        row = tk.Label(self, bg="white").grid(row=20, column=7, ipadx=80)

        #   PADRES FRACTURAS
        label = tk.Label(self, text="¿Padres con fractura de cadera?", font=FUENTE1, anchor="center", bg="#e0e0e0",
                         fg="black").grid(row=21, column=1, columnspan=2, sticky="nsew", ipady=5)
        padresVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=padresVariable, value=1, font=FUENTE1, anchor="center",
                                bg="white").grid(row=22, column=1, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=padresVariable, value=2, font=FUENTE1, anchor="center",
                                bg="white").grid(row=22, column=2, sticky="nsew")

        #   FUMADOR ACTIVO
        label = tk.Label(self, text="¿Fumador activo?", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=21,
                                                                                                          column=3,
                                                                                                          columnspan=2,
                                                                                                          sticky="nsew",
                                                                                                          ipady=5)
        fumadorVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=fumadorVariable, value=1, font=FUENTE1, anchor="center",
                                bg="white").grid(row=22, column=3, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=fumadorVariable, value=2, font=FUENTE1, anchor="center",
                                bg="white").grid(row=22, column=4, sticky="nsew")

        #   ARTRITIS REUMATOIDE
        label = tk.Label(self, text=" ¿Sufre de artritis reumatoide? ", font=FUENTE1, anchor="center",
                         bg="#e0e0e0").grid(row=21, column=5, columnspan=2, sticky="nsew", ipady=5)
        reumatoideVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=reumatoideVariable, value=1, font=FUENTE1, anchor="center",
                                bg="white").grid(row=22, column=5, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=reumatoideVariable, value=2, font=FUENTE1, anchor="center",
                                bg="white").grid(row=22, column=6, sticky="nsew")

        row23 = tk.Label(self, bg="white").grid(row=23, column=7, ipadx=80)

        #   GLUCOCORTICOIDES
        label = tk.Label(self, text="¿Consume glucocorticoides?", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(
            row=25, column=1, columnspan=2, sticky="nsew", ipady=5)
        glucoVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=glucoVariable, value=1, font=FUENTE1, anchor="center",
                                bg="white").grid(row=26, column=1, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=glucoVariable, value=2, font=FUENTE1, anchor="center",
                                bg="white").grid(row=26, column=2, sticky="nsew")

        #   ALCOHOL _---corregido-----
        label = tk.Label(self, text="¿Consume alcohol diariamente?", font=FUENTE1, anchor="center", bg="#e0e0e0").grid(row=25,
                                                                                                           column=3,
                                                                                                           columnspan=2,
                                                                                                           sticky="nsew",
                                                                                                           ipady=5)
        alcoholVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=alcoholVariable, value=1, font=FUENTE1, anchor="center",
                                bg="white").grid(row=26, column=3, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=alcoholVariable, value=2, font=FUENTE1, anchor="center",
                                bg="white").grid(row=26, column=4, sticky="nsew")

        #   OSTEOPOROSIS SECUNDARIA
        label = tk.Label(self, text="¿Sufre un trastorno asociado a osteoporosis?**", font=FUENTE1, anchor="center",
                         bg="#e0e0e0").grid(row=25, column=5, columnspan=2, sticky="nsew", ipady=5)
        secundariaVariable = tk.IntVar()
        boton1 = tk.Radiobutton(self, text="Sí", variable=secundariaVariable, value=1, font=FUENTE1, anchor="center",
                                bg="white").grid(row=26, column=5, sticky="nsew")
        boton2 = tk.Radiobutton(self, text="No", variable=secundariaVariable, value=2, font=FUENTE1, anchor="center",
                                bg="white").grid(row=26, column=6, sticky="nsew")

        row = tk.Label(self, bg="white").grid(row=27, column=7, ipadx=80)

        # TITULO-------------------------------------------------------------------------------------------------------

        label = tk.Label(self, text="Ingrese datos de densitometría\nósea →", font=FUENTE1, anchor="center",
                         background="white", fg="black").grid(row=29, column=1, columnspan=2, rowspan=4, sticky="nsew")

        # TABLA DATOS DEXA HORIZONTAL------------------------------------------------------------------------------------

        label = tk.Label(self, font=FUENTE1, anchor="center", background="white", fg="black").grid(row=29, column=3,
                                                                                                   sticky="nsew")
        label = tk.Label(self, text="DMO (g/cm²)", font=FUENTE1, anchor="center", background="#e0e0e0",
                         fg="black").grid(row=29, column=4, sticky="nsew")
        label = tk.Label(self, text="T-SCORE", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(
            row=29, column=5, sticky="nsew")
        label = tk.Label(self, text="Z-SCORE", font=FUENTE1, anchor="center", background="#e0e0e0", fg="black").grid(
            row=29, column=6, sticky="nsew")

        # TABLA DATOS DEXA VERTICAL-------------------------------------------------------------------------------------

        label = tk.Label(self, text="L1-L4", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(
            row=30, column=3, sticky="nsew")
        label = tk.Label(self, text="Cuello Femoral", font=FUENTE1, anchor="center", background="#e0e0e0",
                         fg="BLACK").grid(row=31, column=3, sticky="nsew")
        label = tk.Label(self, text="Trocánter", font=FUENTE1, anchor="center", background="#e0e0e0", fg="BLACK").grid(
            row=32, column=3, sticky="nsew")

        # INGRESO DE DATOS LUMBAR --------------------------------------------------------------------------------------

        l1 = tk.StringVar()
        l2 = tk.StringVar()
        l3 = tk.StringVar()
        lumbar_dmo = tk.Entry(self, textvariable=l1, font=FUENTE1, background="white", fg="black", width=1,
                              justify="center")
        lumbar_dmo.grid(row=30, column=4, sticky="nsew")
        lumbar_dmo.focus_set()

        lumbar_tscore = tk.Entry(self, textvariable=l2, font=FUENTE1, background="white", fg="black", width=1,
                                 justify="center")
        lumbar_tscore.grid(row=30, column=5, sticky="nsew")
        lumbar_tscore.focus_set()

        lumbar_zcore = tk.Entry(self, textvariable=l3, font=FUENTE1, background="WHITE", fg="black", width=1,
                                justify="center")
        lumbar_zcore.grid(row=30, column=6, sticky="nsew")
        lumbar_zcore.focus_set()

        # INGRESO DE DATOS CUELLO --------------------------------------------------------------------------------------

        c1 = tk.StringVar()
        c2 = tk.StringVar()
        c3 = tk.StringVar()

        cuello_dmo = tk.Entry(self, textvariable=c1, font=FUENTE1, background="white", fg="black", width=1,
                              justify="center")
        cuello_dmo.grid(row=31, column=4, sticky="nsew")
        cuello_dmo.focus_set()

        cuello_tscore = tk.Entry(self, textvariable=c2, font=FUENTE1, background="white", fg="black", width=1,
                                 justify="center")
        cuello_tscore.grid(row=31, column=5, sticky="nsew")
        cuello_tscore.focus_set()

        cuello_zcore = tk.Entry(self, textvariable=c3, font=FUENTE1, background="white", fg="black", width=1,
                                justify="center")
        cuello_zcore.grid(row=31, column=6, sticky="nsew")
        cuello_zcore.focus_set()

        # INGRESO DE TROCANTER --------------------------------------------------------------------------------------

        t1 = tk.StringVar()
        t2 = tk.StringVar()
        t3 = tk.StringVar()

        trocanter_dmo = tk.Entry(self, textvariable=t1, font=FUENTE1, background="white", fg="black", width=1,
                                 justify="center")
        trocanter_dmo.grid(row=32, column=4, sticky="nsew")
        trocanter_dmo.focus_set()

        trocanter_tscore = tk.Entry(self, textvariable=t2, font=FUENTE1, background="white", fg="black", width=1,
                                    justify="center")
        trocanter_tscore.grid(row=32, column=5, sticky="nsew")
        trocanter_tscore.focus_set()

        trocanter_zcore = tk.Entry(self, textvariable=t3, font=FUENTE1, background="white", fg="black", width=1,
                                   justify="center")
        trocanter_zcore.grid(row=32, column=6, sticky="nsew")
        trocanter_zcore.focus_set()

        def values():
            paciente = Paciente()
            # Setteando el vector de caracteristicas
            if int(sexoVariable.get()) == 1:
                sex = "H"
            else:
                sex = "M"

            caracteristicas.clear()
            caracteristicas.append(dni.get())
            caracteristicas.append(nombre.get())
            caracteristicas.append(apellido.get())
            caracteristicas.append(sex)
            caracteristicas.append(edad.get())
            caracteristicas.append(fracturas.get())
            caracteristicas.append(caidas.get())
            caracteristicas.append(ciudad.get())
            caracteristicas.append(departamento.get())
            caracteristicas.append(nacimiento.get())
            caracteristicas.append(talla.get())
            caracteristicas.append(peso.get())

            caracteristicas.append(l1.get())
            caracteristicas.append(l2.get())
            caracteristicas.append(l3.get())

            caracteristicas.append(c1.get())
            caracteristicas.append(c2.get())
            caracteristicas.append(c3.get())

            caracteristicas.append(t1.get())
            caracteristicas.append(t2.get())
            caracteristicas.append(t3.get())

            controller.get_pacientes().add_paciente(dni.get(), caracteristicas)
            paciente.cargar(caracteristicas)

            controller.set_paciente(paciente)
            # p = tk.StringVar("Hola")
            # print(p,",",p.get())
            controller.get_paciente().show_stats()
            controller.show_frame(MostradorResultados)

        row = tk.Label(self, bg="white").grid(row=33, column=7, ipadx=80, ipady=7)

        #   PIE---------------------------------------------------------------------------------------------------------
        # NO TOCAR-----------------------------------------------------------------------------------------------------
        pie = tk.Label(self,
                       text="* Excluyendo fracturas de alto impacto. Por ejemplo, no accidentes de carro"
                            "s.                                                                  \n** Por ejemplo, di"
                            "abetes tipo I, hipertiroidismo no tratado durante largo tiempo, malnutrición o hepatopatía "
                            "crónica.",
                       font=FUENTEPIE, bg="white", anchor="w").grid(row=35, column=1, columnspan=5, sticky="nsew")

        #   BOTON FINALIZAR-----------------------------------------------------------------------------------------
        button = tk.Button(self, text="REGISTRAR", font=FUENTE16, relief="groove", borderwidth=2, height=1,
                           command=lambda: values())
        button.grid(row=34, column=5, columnspan=2, ipadx=27)

        row = tk.Label(self, bg="white").grid(row=36, column=7, ipadx=80, ipady=4)

        # --------------------------------------------------------------

        botonRegresar = tk.Button(self, text="←", font=FUENTEFLECHA, relief="groove", borderwidth=2, width=5, height=1,
                                  bg="white", command=lambda: controller.show_frame(Ramas))
        botonRegresar.place(x=10, y=10)
