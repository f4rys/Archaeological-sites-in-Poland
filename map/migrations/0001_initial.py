from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Excavations',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('INSPIRE_ID', models.TextField(max_length=255)),
                ('CHRONOLOGIA', models.TextField(max_length=255)),
                ('FUNKCJA', models.TextField(max_length=255)),
                ('MIEJSCOWOSC', models.TextField(max_length=255)),
                ('LINK', models.TextField(max_length=255)),
            ],
        ),
    ]
