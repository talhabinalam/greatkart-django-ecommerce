# GreatKart - Django eCommerce Platform

GreatKart is a comprehensive eCommerce platform built using Django. Designed with scalability and flexibility in mind, it enables businesses to efficiently showcase and manage their products, categories, and customer interactions. With features like a secure payment gateway, dynamic product display, and user-friendly admin management, GreatKart delivers a robust solution for online retail.

---

## 🚀 Live Demo
[Visit Live Demo](https://sonet.pythonanywhere.com/)

---

## Features

### 🛍️ User Features
- **Dynamic Product Display**: Browse featured and category-specific products on an intuitive home page.
- **User Accounts**: Secure registration and login system for customers to manage their profiles, orders, and wishlist.
- **Shopping Cart**: Easily add, update, or remove items from the cart. Tax calculations and grand total displayed dynamically.
- **Checkout**: Seamless checkout process with PayPal integration for secure transactions.
- **Search and Filters**: Find products quickly using the search bar and category filters.

### 🛠️ Admin Features
- **Product Management**: Add, edit, and delete products with support for variations (e.g., size, color).
- **Order Management**: Track and manage orders efficiently via the admin dashboard.
- **Category Management**: Create and organize product categories to improve product discoverability.
- **User Management**: Manage customer accounts and profiles directly from the admin panel.

### 🌟 Additional Features
- **PayPal Integration**: Secure and seamless online payment processing.
- **Responsive Design**: Ensures the website works perfectly across desktops, tablets, and mobile devices.
- **Pagination**: Django-powered pagination for smooth navigation through product listings.
- **Alerts and Notifications**: Dynamic alerts for login errors, cart updates, and checkout actions using Bootstrap styling.

---

## 🛠️ Technologies Used
- **Backend**: Django, SQLite (development), PostgreSQL (production).
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap.
- **Third-Party Libraries**: Font Awesome for icons, jQuery for enhanced interactivity.
- **Payment Gateway**: PayPal for secure payment processing.

---

## 📖 Installation Guide

### Prerequisites
- Django 4.x or higher
- SQLite or PostgreSQL

---

1. Clone the repository:
   ```bash
   https://github.com/talhabinalam/greatkart-django-ecommerce.git
   ```
2. Navigate to the project directory:
   ```bash
   cd greatkart-django-ecommerce
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```bash
   python manage.py runserver
   ```
8. Access the application:
   - Application: https://sonet.pythonanywhere.com/
   - Admin Panel: https://sonet.pythonanywhere.com/secureadmin/

## Requirements

The `requirements.txt` file contains all necessary Python packages. Major dependencies include:
* **Django**: Framework for building the application.
* **Bootstrap**: Integrated for styling and responsive design in templates.

## Overview
![image](https://github.com/user-attachments/assets/38c5adb0-0500-4ad8-b2ee-e8af7071ec78)
