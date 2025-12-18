📊 Personal Expense Tracker – Django Backend
📌 Project Overview

The Personal Expense Tracker is a backend application built with Django and Django REST Framework (DRF).
It provides a secure RESTful API that allows users to manage personal financial data, including categories, transactions, and reports.

This repository documents the step-by-step development process, with a focus on clean architecture, security, and best practices.

🛠 Tech Stack

Python

Django

Django REST Framework

MySQL

DRF Token Authentication

Git & GitHub

Postman (API Testing)

📁 Project Structure
expense_tracker/
│
├── expense_tracker/     # Project configuration
├── users/               # Authentication & user-related logic
├── categories/          # Category management (Day 2)
├── transactions/        # Transactions management (Day 3)
├── reports/             # Reporting endpoints (Day 4)
│
├── manage.py
├── requirements.txt
└── README.md

🚀 Development Progress
✅ Day 1 – Project Setup & Authentication

Day 1 focused on laying a solid foundation for the backend by setting up the project, configuring the database, and implementing secure user authentication.

🔹 Day 1 Objectives

Set up Django project and core apps

Configure MySQL database connection

Enable Django REST Framework

Implement user registration and login

Add token-based authentication

Establish clean Git commit practices

🔹 Day 1 Activities (Detailed)
1. Project Initialization

Created and activated a Python virtual environment

Installed Django and Django REST Framework

Initialized Django project (expense_tracker)

Verified setup by running the development server

Key concepts learned:

Project vs app separation

Purpose of manage.py

2. Core App Creation

Created modular Django apps to ensure separation of concerns:

users – authentication and authorization

categories – category management (future)

transactions – income and expense tracking (future)

reports – reporting and summaries (future)

All apps were registered in INSTALLED_APPS.

3. Database Configuration

Configured MySQL as the primary database

Used environment variables (.env) for sensitive credentials

Applied initial Django migrations

Key concepts learned:

Django migrations

Why production applications avoid SQLite

4. Django REST Framework Setup

Enabled rest_framework

Enabled rest_framework.authtoken

Configured global token authentication settings

This established the project as an API-first backend.

5. User Registration

Used Django’s built-in User model

Implemented a registration serializer to handle validation and secure password hashing

Created a registration endpoint that:

Validates input

Creates a new user

Generates and returns an authentication token

Security principle applied:
Passwords are never stored in plain text—Django handles hashing internally.

6. User Login with Token Authentication

Implemented login using Django’s authenticate() method

Validated user credentials securely

Returned an existing or newly created token upon successful login

Implemented proper error handling for invalid credentials

7. Dependency Management

Added requirements.txt to track project dependencies

Ensured the project can be easily set up in any environment

🔐 Authentication Overview

Token-based authentication using DRF

Tokens are returned on both registration and login

Tokens will be required for all protected endpoints (from Day 2 onward)

Example header for authenticated requests:

Authorization: Token <user_token>

🧪 API Testing

All Day 1 endpoints were tested using Postman

Verified:

Successful registration

Successful login

Token generation and reuse



🔜 Next Steps
Planned Development:

Day 2: Categories (models, ownership, permissions)

Day 3: Transactions (CRUD, relationships, validation)

Day 4: Reports, aggregation, testing, and final polish

📌 Notes

The project uses Django’s built-in authentication system

No custom user model was required for current scope

Sensitive data is managed via environment variables and excluded from version control

👨‍💻 Author

Shayani Nyambura Kahumu
Backend Developer
Personal Expense Tracker Project