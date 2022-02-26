# Generated by Django 4.0.2 on 2022-02-26 08:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=22)),
                ('height', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=0)])),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('image1', models.ImageField(upload_to='uploads/%Y/%m/%d')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, max_length=3, null=True)),
                ('summer', models.CharField(blank=True, max_length=3, null=True)),
                ('autumn', models.CharField(blank=True, max_length=3, null=True)),
                ('spring', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('name', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(limit_value=2)], verbose_name='Имя')),
                ('fam', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(limit_value=2)], verbose_name='Фамилия')),
                ('otc', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(limit_value=2)], verbose_name='Отчество')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=128, region=None, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Added',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='new', max_length=20)),
                ('type', models.CharField(default='pass', max_length=4)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('beauty_title', models.CharField(default='пер.', max_length=10)),
                ('title', models.CharField(max_length=255)),
                ('other_titles', models.CharField(blank=True, max_length=255, null=True)),
                ('connect', models.CharField(blank=True, help_text='что соединяет', max_length=255, null=True)),
                ('coords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.coords')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.image')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Level', to='pereval.level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.userprofile')),
            ],
        ),
    ]
