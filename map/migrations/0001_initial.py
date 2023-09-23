from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Excavations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('INSPIRE_ID', models.TextField(max_length=255)),
                ('FORMA_OCHRONY', models.TextField(max_length=255)),
                ('DOKLADNOSC_POLOZENIA', models.TextField(max_length=255)),
                ('NAZWA', models.TextField(max_length=255)),
                ('OBSZAR_AZP', models.TextField(max_length=255)),
                ('NR_STANOWISKA_OBSZAR', models.TextField(max_length=255)),
                ('CHRONOLOGIA', models.TextField(max_length=255)),
                ('FUNKCJA', models.TextField(max_length=255)),
                ('WYKAZ_DOKUMENTOW', models.TextField(max_length=255)),
                ('DATA_WPISU', models.TextField(max_length=255)),
                ('WOJEWODZTWO', models.TextField(max_length=255)),
                ('POWIAT', models.TextField(max_length=255)),
                ('GMINA', models.TextField(max_length=255)),
                ('MIEJSCOWOSC', models.TextField(max_length=255)),
                ('LINK', models.TextField(max_length=255)),
            ],
        ),
    ]
