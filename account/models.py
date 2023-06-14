from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
#---------------------------------------------------------------------------------------
class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        """
        Crea y guarda un Usuario con el correo electrónico, nombre, tc y contraseña proporcionados.
        """
        if not email:
            raise ValueError('El usuario debe tener una dirección de correo electrónico')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
#---------------------------------------------------------------------------------------
    def create_superuser(self, email, name, tc, password=None):
        """
        Crea y guarda un superusuario con el correo electrónico, nombre, tc y contraseña dados.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
#---------------------------------------------------------------------------------------
#  Modelo de usuario custom
#---------------------------------------------------------------------------------------
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'tc']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "¿El usuario tiene un permiso específico?"
        # Respuesta más simple posible: Sí, siempre
        return self.is_admin

    def has_module_perms(self, app_label):
        "¿El usuario tiene permisos para ver la aplicación `app_label`?"
        # Respuesta más simple posible: Sí, siempre
        return True

    @property
    def is_staff(self):
        "¿Es el usuario un miembro del personal??"
        # La respuesta más simple posible: todos los administradores son staff
        return self.is_admin
#---------------------------------------------------------------------------------------