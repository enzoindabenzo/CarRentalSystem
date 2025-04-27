# Car Rental System

## 🚗 Overview
The **Car Rental System** is a web-based application that allows users to rent cars, manage bookings, and handle vehicle inventory efficiently. It is designed for businesses that provide car rental services, making it easier to track reservations, customers, and fleet availability.

## 📌 Features
- User authentication (Admin & Customers)
- Search and filter available cars
- Book, edit, or cancel car rentals
- Payment processing integration
- Admin dashboard to manage users, cars, and bookings
- Reports & analytics

## 🛠️ Technologies Used
- **Backend:** Python (Flask/Django)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** MySQL / PostgreSQL
- **Version Control:** Git & GitHub

## 🚀 Installation & Setup
### Prerequisites
Make sure you have the following installed:
- Python 3
- Pip (Python package manager)
- MySQL Server (or compatible database)
- Git

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/enzoindabenzo/CarRentalSystem.git
   cd CarRentalSystem
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database (MySQL example):
   ```bash
   mysql -u root -p -e "CREATE DATABASE car_rental;"
   ```
5. Run migrations (for Django projects):
   ```bash
   python manage.py migrate
   ```
6. Start the development server:
   ```bash
   python app.py  # Flask
   # OR
   python manage.py runserver  # Django
   ```
7. Open your browser and visit: `http://127.0.0.1:5000/` (Flask) or `http://127.0.0.1:8000/` (Django)


## 🏆 Contributors
- **enzoindabenzo** - Developer

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).


