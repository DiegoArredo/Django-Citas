from django.db import models
import re 
# Create your models here.


class UserManager(models.Manager):

    def validator(self, postData):

        errors = {}

        #LARGO MINIMO NOMBRE
        if len(postData["nombre"]) < 3:
            errors["nombre"] = "Nombre debe tener minimo 3 caracteres!"
        if len(postData["apellido"]) < 3:
            errors["apellido"] = "Apellido debe tener minimo 3 caracteres!"

        #EMAIL 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):       
            errors['email'] = "Direccion de correo no valida!"
        
        #CONTRASEÑAS IGUALES
        if postData["password"] != postData["confirm_pass"]:
            errors["confirm_pass"] = "Las contraseñas no coinciden!"

        #CONTRASEÑA
        PASS_REGEX = re.compile(r'^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$')
        if not PASS_REGEX.match(postData["password"]):
            errors["password"] = f"Contraseña debe incluir:\n-Al menos una letra mayúscula en inglés\n-Al menos una letra minúscula en inglés\n-Al menos un dígito\n-Al menos un personaje especial\n-Mínimo ocho de longitud"

        return errors

    def edit_validator(self,postData):
        errors = {}

        #LARGO MINIMO NOMBRE
        if len(postData["nombre"]) < 3:
            errors["nombre"] = "Nombre debe tener minimo 3 caracteres!"
        if len(postData["apellido"]) < 3:
            errors["apellido"] = "Apellido debe tener minimo 3 caracteres!"
            
        #EMAIL 
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):       
            errors['email'] = "Direccion de correo no valida!"

        return errors
class User(models.Model):

    nombre = models.CharField(max_length=95)
    apellido = models.CharField(max_length=95)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=95)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    #my_likes

    def __repr__(self) -> str:
        return f"Nombre: {self.nombre} Apellido: {self.apellido}  Email: {self.email}"

    def __str__(self) -> str:
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Email: {self.email}"
