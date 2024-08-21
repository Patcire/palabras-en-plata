from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

User = settings.AUTH_USER_MODEL

#USUARIO

class UserManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Introduce una dirección de correo electrónico')
        if not username:
            raise ValueError('Introduce un nombre de usuario')
        if not password:
            raise ValueError('Introduce una contraseña')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_passworrd(password)
        user.save(using=self._db)
        return user
    
    def create_admin(self, email, username, password=None):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=30,
        unique=True
    )
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=200, default=None)
    is_admin = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)
    is_active = models.BooleanField(default = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    objects = UserManager()


#PUBLICACIÓN

class Post(models.Model):

    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    publish_date = models.DateField()
    
    #Sería necesario guardar la fecha de modificación? => Alternativa: Actualizar fecha de publicación (?)
    #mod_date = models.DateField()
       
    body_text = models.TextField()

    #Depende de como se trate el dibujo
    #draw = models.ImageField()

    img = models.ImageField()

    def __str__(self):
        return self.post_id


    

