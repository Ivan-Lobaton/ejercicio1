#Se ha escogido Python para estos ejercicios.

#Pagina de Python: https://www.python.org/

#############################################################################################################################################

"Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje"

#Este es un tipo de comentario que se utiliza unicamente en una linea.

"Este es otro tipo de comentario que al igual que con #, solo se utiliza en una línea."

"""Este tipo de comentarios se coloca automáticamente con Alt + Shift + A en Visual Studio Code.
Este tipo de comentarios pueden tener en bloque, siempre y cuando estén dentro de las comillas."""

'Los comentarios anteriores se pueden usar con comillas simples.'

'''Su funcionamiento es exactamente igual.
Solo cambian el tipo de comillas.'''

#############################################################################################################################################

"Crea una variable (y una constante si el lenguaje lo soporta)."

#Para las variables que contengan números no se necesitan de las comillas.

enteros = 5

flotante = 3.14

complejo = 2 +3j #Los números complejos son números con una parte real y otra imaginaria reflejada con "j".

#Las variables de tipo booleano solo pueden tener 2 valores; true o false.

verdadero = True
falso = False

#Las variables de tipo cadena (Strings) se utilizan para representar datos de textos. Estas se cierran en comillas simples o dobles.

mascota = "Perros"
comida = "Pizza"

#Las variables de tipo lista se utilizan para contener cualquier tipo de dato en corchetes.

numeros = [1, 2, 3, 4, 5]
nombres = ["Frank", "Gabriel", "Alexander"]

#Las variables de tipo tupla son similares a las listas, pero sus datos no pueden cambiar.

decimales = (1.1, 1.2, 1.3, 1.4, 1.5)
frutas = ("Manzana", "Mandarina", "Banana")

#Las variables de tipo conjunto son similares a las listas, pero sus valores son únicos.

numeros_unicos = {7, 9, 11}
frutas_unicas = {"Mango", "Sandia"}

#Las variables de tipo diccionario se utiliza para almacenar pares clave-valor.

persona = {"nombre": "Juan", "años": 18, "ciudad": "Medellin"}

"Además de estas variables, existen otras que también son importantes."

#La variable de tipo None es una variable que no representa ningún valor.

Nada = None

#La variable de tipo carácter es un único valor almacenado en una variable.

char1 = "a"
char2 = "b"
char3 = "c"

"""En Python no hay una manera especifica de declarar una constante
ya que las variables son de tipo dinámico, ósea, puede cambiar, pero
se sigue unas convenciones para declarar constantes, la cual es
utilizar letras mayúsculas para que los programadores comprendan que
esa variable no puede modificarse durante la ejecución del programa."""

PI = 3.1416

#############################################################################################################################################

"Crea variables representando todos los tipos de datos primitivos del lenguaje."

#Datos tipo enteros
numero = 1
año = 2024
negativo = -5

#Datos tipo flotantes
decimal = 0.25
pi = 3.141592

#Datos tipo booleanos
verdadero = True
falso = False

#Datos tipo cadenas (Strings)
hola = "Hola mundo"
docente = "Mario Castañeda del Prepucio"
web = "uniminuto.edu.co"

#############################################################################################################################################

"Imprime por terminal el texto: '¡Hola, [y el nombre de tu lenguaje]!'"

print("¡Hola, Python!")

print(type(numero))
print(type(pi))
print(type(verdadero))
print(type(falso))
print(type(docente))