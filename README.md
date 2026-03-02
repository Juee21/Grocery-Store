# 🛒 Grocery Store - E-commerce Platform

A full-featured, responsive E-commerce application built with **Django 5.2**. This project allows users to browse products, manage a shopping cart, and place orders with automated PDF invoice generation.

## 🚀 Live Demo
**Visit the live site:** [juee.pythonanywhere.com](https://juee.pythonanywhere.com)

## ✨ Features
* **Product Catalog:** Browse products by categories (e.g., Fruits, Dairy, Bakery).
* **Dynamic Shopping Cart:** Add, update, and remove items using Django sessions.
* **Order Management:** Secure checkout process and order tracking.
* **PDF Invoices:** Generates a professional invoice for every completed order.
* **Admin Dashboard:** Full control over categories, products, and order status.
* **Responsive UI:** Mobile-friendly design powered by **Bootstrap 5**.

## 🛠️ Tech Stack
* **Backend:** Python 3.11, Django 5.2
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
* **Database:** SQLite (Development) / PythonAnywhere (Production)
* **Media Handling:** Django File Storage with PythonAnywhere static hosting.

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Juee21/Grocery-Store.git](https://github.com/Juee21/Grocery-Store.git)
   cd Grocery-Store
2. Set up Virtual Environment:

Bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install Requirements:

Bash
pip install -r requirements.txt
Database Setup:

3. Bash
python manage.py migrate
python manage.py createsuperuser

5. Run the Project:

Bash
python manage.py runserver
Open http://127.0.0.1:8000 in your browser.

5. 📂 Folder Structure
shop/ - Product models, views for the catalog, and categories.

cart/ - Logic for managing items in the user session.

orders/ - Checkout logic and PDF generation.

media/ - Product images uploaded by the admin.

static/ - CSS, JS, and global assets.

Developed by Juee ```
