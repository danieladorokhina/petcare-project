# PetCare

## Team
- Daniela Dorokhina 
- Olha Bidochka

## About project
PetCare — це невеликий сайт для власників домашніх тварин.  
Користувач може створювати профілі своїх улюбленців і записуватись до ветеринара.  
Ветеринар може переглядати записи і змінювати їхній статус.

## Features
- Реєстрація та логін користувачів (JWT)
- Ролі: користувач, ветеринар, адміністратор
- Додавання, редагування, видалення тварин
- Запис на прийом до ветеринара

## Technologies
- Backend: Django REST Framework  
- Database: SQLite  
- Frontend: HTML, CSS, JavaScript

## How to run 
git clone https://github.com/danieladorokhina/petcare-project
cd petcare-project/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Main endpoints
-	POST /api/accounts/register/ — реєстрація
-	POST /api/accounts/login/ — логін
-	GET/POST /api/pets/ — тварини
-	GET/POST /api/appointments/ — записи
