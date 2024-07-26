<img height="100px" src="map\static\img\logo2.png">

# Archaeological sites in Poland

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Leaflet](https://img.shields.io/badge/Leaflet-199900.svg?style=for-the-badge&logo=Leaflet&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Railway](https://img.shields.io/badge/Railway-0B0D0E.svg?style=for-the-badge&logo=Railway&logoColor=white)

[![Django CI](https://github.com/f4rys/Archaeological-sites-in-Poland/actions/workflows/django.yml/badge.svg)](https://github.com/f4rys/Archaeological-sites-in-Poland/actions/workflows/django.yml) [![CodeQL](https://github.com/f4rys/Archaeological-sites-in-Poland/actions/workflows/codeql.yml/badge.svg)](https://github.com/f4rys/Archaeological-sites-in-Poland/actions/workflows/codeql.yml) ![Website](https://img.shields.io/website?url=https%3A%2F%2Fexcavations-in-poland.up.railway.app%2F)

Interactive map of archaeological sites in Poland as provided by dane.gov.pl website. Markers are parsed via the WMS service. Information about every place is stored in the sqlite3 database and loaded upon click on a specific point. The application is hosted via Docker container on Railway.

<div align="center"><img src="preview.jpg"></div>

## Data used
Archaeological sites in Poland provided via <a href="https://dane.gov.pl/pl/dataset/210,rejestr-zabytkow-archeologicznych/resource/56490/table">WMS</a> service and <a href="https://dane.gov.pl/pl/dataset/210,rejestr-zabytkow-archeologicznych/resource/59097/table?page=1&per_page=20&q=&sort=">CSV</a> file and used under the <a href="https://creativecommons.org/licenses/by/4.0/legalcode.pl">CC BY 4.0 license</a>. Maps are provided by <a href="https://osmfoundation.org/">OpenStreetMap Foundation</a> under the <a href="https://opendatacommons.org/licenses/odbl/1-0/">Open Data Commons Open Database License</a>.

## Tech Stack
**Backend:** Python (Django), SQLite3 <br />
**Frontend:** JavaScript (Leaflet.js, Require.js), Bootstrap <br />
**Hosting:** Railway (Docker)

## Run locally

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/f4rys/Archaeological-sites-in-Poland

2. **Create venv and activate it**
3. **Create a .env file in the base folder and fill it in:**
   ```bash
    SECRET_KEY={RANDOM_SECRET_KEY}
    DJANGO_SETTINGS_MODULE=archeological_sites_in_poland.dev_settings # For development
    # For production use: archeological_sites_in_poland.production_settings 
   ```

3. **Install dependencies and prepare database:**
   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py load_data
   ```
4. **Run the server and open it in the browser:**
   ```bash
   python manage.py runserver
   http://127.0.0.1:8000/
   ```

Or just use the Dockerfile.

## Credits
<div>• Icon by <a href="https://www.iconfinder.com/icons/4791027/acropolis_ancient_building_greek_landmark_parthenon_icon">Royyan Wijaya</a> on Iconfinder</div>



