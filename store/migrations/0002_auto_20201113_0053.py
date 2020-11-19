# Generated by Django 3.1.1 on 2020-11-13 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('is_pickup', models.BooleanField(default=False)),
                ('order_no', models.CharField(max_length=10)),
                ('cusomter_name', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('geolocation', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
            ],
        ),
    ]
