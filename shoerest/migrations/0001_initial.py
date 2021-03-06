# Generated by Django 3.0 on 2019-12-06 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ShoeColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(choices=[('RED', 'Red'), ('ORG', 'Orange'), ('YLW', 'Yellow'), ('GRN', 'Green'), ('BLU', 'Blue'), ('IND', 'Indigo'), ('VLT', 'Violet'), ('WHT', 'White'), ('BLK', 'Black')], default='RED', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(choices=[('SNK', 'Sneaker'), ('BOOT', 'Boot'), ('SNDL', 'Sandal'), ('DRS', 'Dress'), ('OTHR', 'Other')], default='SNK', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=50)),
                ('fasten_type', models.CharField(max_length=50)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoerest.ShoeColor')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoerest.Manufacturer')),
                ('shoe_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoerest.ShoeType')),
            ],
        ),
    ]
