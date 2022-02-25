from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(models.Model):
    """Карточка пользователя"""
    email = models.EmailField(db_index=True, unique=True)
    name = models.CharField(max_length=32, validators=[MinLengthValidator(limit_value=2)], verbose_name='Имя')
    fam = models.CharField(max_length=32, validators=[MinLengthValidator(limit_value=2)], verbose_name='Фамилия')
    otc = models.CharField(max_length=32, validators=[MinLengthValidator(limit_value=2)], verbose_name='Отчество')
    phone = PhoneNumberField(unique=True, db_index=True)

    def __str__(self):
        return f'{self.name} {self.fam}: {self.email}'


class Added(models.Model):
    """Карточка перевала"""
    STATUS_CHOICES = [
        ('new', 'new'),
        ('pending', 'pending'),
        ('resolved', 'resolved'),
        ('accepted', 'accepted'),
        ('rejected', 'rejected')
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=8, default='new')
    type = models.CharField(max_length=4, default='pass')
    add_time = models.DateTimeField(auto_now_add=True)

    beauty_title = models.CharField(max_length=10, default='пер.')
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, null=True, blank=True)
    connect = models.CharField(max_length=255, null=True, blank=True, help_text='что соединяет')

    coords = models.ForeignKey('Coords', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    images = models.ManyToManyField('Image', related_name='addeds')
    level = models.ForeignKey(
        'Level', on_delete=models.CASCADE, related_name='Level', null=True, blank=True
    )

    def __str__(self):
        return f"{self.title} - {self.status}"


class Level(models.Model):
    """Категория трудности перевала"""
    winter = models.CharField(max_length=3, null=True, blank=True)
    summer = models.CharField(max_length=3, null=True, blank=True)
    autumn = models.CharField(max_length=3, null=True, blank=True)
    spring = models.CharField(max_length=3, null=True, blank=True)


class Image(models.Model):
    """Фото перевала"""
    image = models.ImageField(upload_to='uploads/%Y/%m/%d')


class Coords(models.Model):
    """Координаты перевала"""
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    height = models.SmallIntegerField(validators=[MinValueValidator(limit_value=0)], default=0)

    def __str__(self):
        return f"{self.latitude} {self.longitude}, {self.height}"