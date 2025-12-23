# 📊 Personal Expense Tracker – Django Backend API

## 🎯 Project Overview

The **Personal Expense Tracker** is a robust, secure, and scalable backend API built with Django and Django REST Framework (DRF). This RESTful API enables users to manage personal financial data through a comprehensive system for tracking expenses, organizing categories, generating reports, and analyzing spending patterns.

The project follows clean architecture principles, implements proper security measures, and demonstrates professional Django development practices throughout its modular implementation.

## ✨ Features

### 🔐 **Authentication & Security**
- Token-based authentication using Django REST Framework
- Secure user registration with password hashing
- Protected endpoints requiring valid authentication tokens


### 📁 **Category Management**
- Create, read, update, and delete expense categories
- User-specific category ownership
- Unique category names per user
- Default system categories for new users

### 💰 **Transaction Management**
- Full CRUD operations for income and expense transactions
- Transaction categorization with foreign key relationships
- Date-based transaction organization
- Amount validation and data integrity
- User-specific transaction isolation

### 📊 **Reporting & Analytics**
- Monthly expense summaries with total amounts
- Category-wise spending breakdowns
- Date-range based reporting
- Transaction aggregation and analytics


### 🛡️ **Security & Best Practices**
- Django's built-in password hashing
- Token authentication for API access
- Protected endpoints with proper permissions
- Environment variable configuration
- SQL injection prevention through ORM

## 🏗️ **Tech Stack**

| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Core programming language |
| **Django 4.x** | Web framework |
| **Django REST Framework** | API development |
| **MySQL** | Database management |
| **DRF Token Authentication** | Secure API access |
| **Git & GitHub** | Version control |
| **Postman** | API testing & documentation |

## 📁 **Project Structure**

```
expense_tracker/
├── expense_tracker/          # Project configuration
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # Main URL routing
│   └── wsgi.py
│
├── users/                    # Authentication module
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py              # Auth endpoints
│   ├── views.py             # Registration & login
│   └── serializers.py       # User serializers
│
├── categories/               # Category management
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py            # Category model
│   ├── serializers.py       # Category serializers
│   ├── views.py             # Category views
│   └── urls.py              # Category endpoints
│
├── transactions/             # Transaction management
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py            # Transaction model
│   ├── serializers.py       # Transaction serializers
│   ├── views.py             # Transaction views
│   └── urls.py              # Transaction endpoints
│
├── reports/                  # Reporting module
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py             # Report generation
│   └── urls.py              # Report endpoints
│
├── manage.py                 # Django management
├── requirements.txt          # Dependencies
├── .env             # Environment template
├── .gitignore               # Version control exclusions
└── README.md                # This file
```

## 🚀 **Getting Started**

### **Prerequisites**
- Python 3.8 or higher
- MySQL Server
- Git
- pip (Python package manager)

### **Installation**

1. **Clone the repository**
```bash
git clone https://github.com/shlavin/Personal-Expense-Tracker-Project
cd expense-tracker
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration:
# DATABASE_NAME=expense_tracker
# DATABASE_USER=your_username
# DATABASE_PASSWORD=your_password
# DATABASE_HOST=localhost
# DATABASE_PORT=3306
```

5. **Database setup**
```sql
-- In MySQL:
CREATE DATABASE expense_tracker;
```

6. **Apply migrations**
```bash
python manage.py migrate
```

7. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

8. **Run development server**
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## 📚 **API Documentation**

### **Authentication Endpoints**

#### **1. User Registration**
```http
POST /api/register/
Content-Type: application/json

{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword123"
}
```

**Response:**
```json
{
    
    "username": "john_doe",
    "email": "john@example.com",
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

#### **2. User Login**
```http
POST /api/login/
Content-Type: application/json

{
    "username": "john_doe",
    "password": "securepassword123"
}
```

**Response:**
```json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b",
    
    "username": "user registered successfully"
}
```

### **Category Endpoints** (Requires Authentication)
All category endpoints require authentication token in headers:
```http
Authorization: Token your_token_here
```

#### **Get All Categories**
```http
GET /api/categories/
```

#### **Create New Category**
```http
POST /api/categories/
Content-Type: application/json

{
    "name": "Groceries",
    
}
```

### **Transaction Endpoints** (Requires Authentication)

#### **Get All Transactions**
```http
GET /api/transactions/
```

#### **Create New Transaction**
```http
POST /api/transactions/
Content-Type: application/json

{
    "amount": 75.50,
    "description": "Weekly grocery shopping",
    "transaction_type": "expense",
    "category": 1,
    "date": "2024-01-15"
}
```

#### **Filter Transactions by Date Range**
```http
GET /api/transactions/?start_date=2024-01-01&end_date=2024-01-31
```

### **Report Endpoints** (Requires Authentication)

#### **Monthly Summary**
```http
GET /api/reports/monthly-summary/?month=1&year=2024
```

**Response:**
```json
{
    "month": 1,
    "year": 2024,
    "total_income": 3000.00,
    "total_expense": 1750.50,
    "balance": 1249.50,
   
}
```



## 🔧 **Development Progress**

### **✅ Day 1 – Project Setup & Authentication**
- Project initialization and virtual environment setup
- Django and DRF configuration
- MySQL database integration
- User registration and login endpoints
- Token-based authentication implementation
- Postman testing setup

### **✅ Day 2 – Category Management**
- Category model with user ownership
- Full CRUD operations for categories
- Unique category names per user constraint
- Default category creation for new users
- API endpoints with proper authentication

### **✅ Day 3 – Transaction Management**
- Transaction model with category relationships
- Income/expense tracking with validation
- Date-based transaction organization
- Complete transaction CRUD operations
- User-specific transaction isolation

### **✅ Day 4 – Reporting Module**
- Monthly expense summaries
- Category-wise spending analytics
- Date-range based reporting
- Data aggregation and calculations
- Report API endpoints

## 🧪 **Testing the API**

### **Using Postman**
1. Import the provided Postman collection
2. Set up environment variables for base URL and tokens
3. Test endpoints in sequence: Register → Login → Categories → Transactions → Reports

### **Manual Testing**
```bash
# Test registration
curl -X POST http://127.0.0.1:8000/api/register/ \
     -H "Content-Type: application/json" \
     -d '{"username":"testuser","email":"test@example.com","password":"testpass123"}'

# Test login and get token
curl -X POST http://127.0.0.1:8000/api/login/ \
     -H "Content-Type: application/json" \
     -d '{"username":"testuser","password":"testpass123"}'

# Test protected endpoint
curl -X GET http://127.0.0.1:8000/api/categories/ \
     -H "Authorization: Token your_token_here"
```

## 🔒 **Security Features**

1. **Password Security**
   - Passwords are hashed using Django's PBKDF2 algorithm
   - Never stored in plain text
   - Minimum length validation

2. **Authentication**
   - Token-based authentication for all protected endpoints
   - Automatic token generation on registration/login
   - Secure token storage and transmission

3. **Data Protection**
   - User data isolation
   - Foreign key constraints
   - Input validation and sanitization
   - SQL injection prevention through Django ORM

4. **Environment Configuration**
   - Sensitive data stored in environment variables
   - Database credentials not hardcoded
   - .gitignore configured to exclude sensitive files

## 📦 **Dependencies**

Key packages used in the project:

```txt
Django==4.2.0
djangorestframework==3.14.0
mysqlclient==2.2.0
python-decouple==3.8
django-cors-headers==4.0.0
```

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 **Author**

**Shayani Nyambura Kahumu**
- Backend Developer
- Personal Expense Tracker Project
- [GitHub Profile](https://github.com/shlavin)
- [LinkedIn Profile](https://www.linkedin.com/in/shayani-kahumu-267983260/)

## 🙏 **Acknowledgments**

- Django and Django REST Framework communities
- MySQL documentation
- All contributors and testers
- Online learning resources that made this project possible

---

**⭐ If you found this project helpful, please give it a star on GitHub!**

**🔗 Repository:** [https://github.com/shlavin/Personal-Expense-Tracker-Project](https://github.com/shlavin/Personal-Expense-Tracker-Project

**🐛 Issues & Feedback:** Please use the GitHub Issues section to report bugs or suggest improvements.

