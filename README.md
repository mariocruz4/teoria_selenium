# TEORÍA SELENIUM

En este pequeño repositorio subiré las pruebas que iré haciendo para entender la teoría de Selenium en TripleTen.

## Consideraciones
Para que funcione es necesario crear un archivo *configuration.py*
Dentro del archivo agregar las siguientes dos variables:
email = ("El correo electronic que usaste para registrarte en la página")
password = ("La contraseña que utilizaste")
**NO COPIES Y PEGUES**

## Error encontrado
En el archivo *filling_in_the_input_field.py* se ha detectado un error:
La teoría de TripleTen indica que la prueba debería ser exitosa si la url (una vez que se inicie sesión) sea: "https://around-v1.nm-tripleten-services.com/signin?lng=es", sin embargo, esto es un error, ya que la URL correcta es: "https://around-v1.nm.tripleten-services.com/" solamente.