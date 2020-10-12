# Generated by Django 2.2.16 on 2020-10-12 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Город')),
                ('translit', models.CharField(max_length=50, unique=True, verbose_name='Транслит')),
            ],
        ),
        migrations.CreateModel(
            name='User2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(blank=True, max_length=40, null=True, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Имя')),
                ('gender', models.CharField(blank=True, choices=[('M', 'мужской'), ('F', 'женский')], max_length=1, null=True, verbose_name='Пол')),
                ('dt_created', models.DateField(auto_now_add=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('town', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Town', verbose_name='Город')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrivateMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300, verbose_name='Текст сообщения')),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
                ('status', models.CharField(choices=[('send', 'Отправлено'), ('recd', 'Получено'), ('read', 'Прочитано')], default='send', max_length=10)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipients', to='accounts.User2', verbose_name='Получатель')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senders', to='accounts.User2', verbose_name='Отправитель')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ManyToManyField(to='accounts.User2')),
            ],
        ),
    ]