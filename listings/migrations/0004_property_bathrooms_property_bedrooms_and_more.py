# Generated by Django 4.2.5 on 2023-09-26 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_remove_property_bathrooms_remove_property_bedrooms_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='bathrooms',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='bedrooms',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('house', 'House'), ('apartment', 'Apartment'), ('condo', 'Condo'), ('land', 'Land')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(upload_to='property_photos/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='image1',
            field=models.ImageField(null=True, upload_to='property_photos/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='image2',
            field=models.ImageField(null=True, upload_to='property_photos/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='image3',
            field=models.ImageField(null=True, upload_to='property_photos/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='image4',
            field=models.ImageField(null=True, upload_to='property_photos/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='image5',
            field=models.ImageField(null=True, upload_to='property_photos/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
