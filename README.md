📚 Online Bookstore

An Online Bookstore Web Application built with a dual dashboard system — Admin and User — that allows smooth management of books, categories, and online purchases.
Users can browse and purchase books securely using Stripe Payment Gateway, while admins can manage book inventory efficiently.

🚀 Features
👩‍💼 Admin Dashboard

➕ Add, update, rename, or delete book categories

📖 Add and manage book details (title, price, description, image, etc.)

🧾 View and manage all user orders

🧹 Edit or delete books easily via a clean dashboard interface

👤 User Dashboard

🛒 Browse and buy books with Stripe payment gateway

📦 Track current orders and view order history

🧑‍💻 View / Edit profile

🔒 Change password securely

🧩 Tech Stack
| Category                | Technologies Used                           |
| ----------------------- | ------------------------------------------- |
| **Frontend**            | HTML, CSS, JavaScript, Bootstrap            |
| **Backend**             | Python, Django Framework                    |
| **Database**            | SQLite / PostgreSQL                         |
| **Payment Integration** | Stripe API                                  |
| **Version Control**     | Git & GitHub                                |
| **Deployment**          | Render / Vercel / Railway *(as applicable)* |
🗂️ Folder Structure

obsproject/
│
├── manage.py
├── db.sqlite3
├── .gitignore
├── .env
│
├── obsproject/                # Main project configuration folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Global Django settings
│   ├── urls.py                # Root URL configuration
│   ├── wsgi.py
│   └── __pycache__/
│
├── adminapp/                  # Admin-side application
│   ├── __init__.py
│   ├── admin.py
│   ├── adminappurls.py        # Admin app specific URLs
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   ├── static/                # Admin-specific static files (CSS, JS, Images)
│   └── templates/             # Admin HTML templates
│
├── userapp/                   # User-side application
│   ├── __init__.py
│   ├── admin.py
│   ├── userappurls.py         # User app specific URLs
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── migrations/
│   ├── static/                # User static files
│   └── templates/             # User HTML templates
│
└── myapp/                     # Common/shared application
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── myapp_urls.py          # Common/shared URLs
    ├── tests.py
    ├── views.py
    ├── migrations/
    ├── static/                # Common static assets
    └── templates/             # Common templates

    ⚙️ Installation & Setup

Follow these steps to run the project locally:

1️⃣ Clone the Repository
git clone https://github.com/shaliniyadav09/online-bookstore.git
cd online-bookstore

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate        # For macOS/Linux
venv\Scripts\activate           # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Start Development Server
python manage.py runserver


Now open your browser and go to 👉 http://127.0.0.1:8000

💳 Stripe Payment Setup

Create a Stripe account → https://stripe.com

Get your Publishable and Secret keys from the Stripe dashboard

Add them in your .env or Django settings.py:

STRIPE_PUBLIC_KEY = "your_public_key"
STRIPE_SECRET_KEY = "your_secret_key"


Test payments using Stripe’s demo card:

Card Number: 4242 4242 4242 4242
Expiry: Any future date
CVC: Any 3 digits
🌐 Live Demo

🔗 Live Website: https://online-bookstore.onrender.com

📁 GitHub Repository: https://github.com/shaliniyadav09/online-bookstore

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.
💬 Author

👩‍💻 Shalini Yadav
📧 Connect on LinkedIn

🌟 If you like this project, give it a ⭐ on GitHub!
