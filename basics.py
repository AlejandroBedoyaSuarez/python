x = 10
y = "10" 
z= 10.4
sum1= x+x
sum2= y+y
#no funciona ya que se debe sumar el mismo tipo de valor
#print(sum1+sum2)
print (type(x) , type(y), type(z))

#Listas
print("Crearemos una lista")
studentGrades= [9.1, 8.8 , 7.5] 
student_grades= [1 , "hello" , [1 , 2 , 4.33]]
print(student_grades)
#Operaciones matemáticas
#La misma lista se repite 3 veces
print(student_grades*3)

#Usaremos range
print("Usaremos Range")
#list(range(número mínimo, número máximo))
studentGrades2= list(range(0, 11 , 2))
print (studentGrades2)