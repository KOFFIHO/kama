# Generated by Django 4.0.4 on 2022-09-16 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_de_produit', models.CharField(max_length=100)),
                ('poids', models.CharField(max_length=50)),
                ('quantite', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('prix', models.IntegerField()),
                ('imageProduit1', models.ImageField(upload_to='img1')),
                ('imageProduit2', models.ImageField(blank=True, null=True, upload_to='img2')),
            ],
        ),
    ]