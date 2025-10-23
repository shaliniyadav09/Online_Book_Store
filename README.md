# Online Bookstore Project (OBS Project)

A full-featured **Online Bookstore** built with **Django**. This project includes both **Admin** and **User** dashboards, enabling book management, order tracking, user management, and seamless payment via **Stripe**.

---

## 📁 Folder Structure
obsproject/
├── manage.py
├── db.sqlite3
├── .gitignore
├── .env
├── obsproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
├── adminapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── adminappurls.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   └── templates/
├── userapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── userappurls.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   ├── static/
│   └── templates/
└── myapp/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── myapp_urls.py
    ├── tests.py
    ├── views.py
    ├── migrations/
    ├── static/
    └── templates/


## ⚙️ Features

### Admin Dashboard
- Add, update, rename, and delete **book categories** and **book details**.
- Manage **orders** and view **order history**.
- Complete control over the bookstore inventory.

### User Dashboard
- **View and edit profile** information.
- **Change password** securely.
- Browse and **buy books**.
- **Stripe payment gateway integration** for safe and smooth transactions.
- View order history.

### Common Features
- Responsive design for desktop and mobile.
- Shared templates and static files for consistency.
- Modular Django app structure for scalability.

---

## 💻 Technologies Used
- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap (optional)  
- **Database:** SQLite  
- **Payment Integration:** Stripe  

---

## 🚀 Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/obsproject.git
cd obsproject

Create virtual environment

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Configure environment variables

Rename .env.example to .env and add your Stripe API keys and Django secret key.

Run migrations

python manage.py makemigrations
python manage.py migrate


Create superuser

python manage.py createsuperuser


Start the development server

python manage.py runserver


Visit http://127.0.0.1:8000/ to access the application.

