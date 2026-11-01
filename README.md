# Student Management System

A RESTful API built with **Python, FastAPI, and PostgreSQL** to manage student records with secure user authentication and user-specific data access.

## Features

- User registration and login
- Secure password hashing
- JWT-based authentication
- Create, read, update, and delete student records (CRUD)
- User-specific student data ownership
- PostgreSQL database integration
- SQLAlchemy ORM
- Pydantic request validation
- Database migrations using Alembic
- CORS configuration for frontend integration
- Interactive API documentation with Swagger UI

## Technologies Used

| Category | Technology |
|---|---|
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Data Validation | Pydantic |
| Authentication | JWT, OAuth2 |
| Password Hashing | pwdlib |
| Migrations | Alembic |
| Server | Uvicorn |
| Version Control | Git, GitHub |

## Project Structure

```text
student-management-system/
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
│
├── app/
│   ├── routers/
│   │   ├── student.py
│   │   └── user.py
│   │
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── utils.py
│   └── oauth2.py
│
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/KartikeyaBainubelli/student-management-system.git
cd student-management-system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
URL=your_postgresql_connection_string
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Replace the placeholder values with your own configuration. Never commit your `.env` file.

### 5. Apply database migrations

```bash
alembic upgrade head
```

### 6. Start the application

```bash
uvicorn app.main:app --reload
```

### 7. Open API documentation

Visit:

http://127.0.0.1:8000/docs

---

**GitHub Repository:** [Student Management System](https://github.com/KartikeyaBainubelli/student-management-system)








## API Endpoints

### User Endpoints

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| POST | `/users/` | Register a new user | Not required |
| POST | `/users/login` | Login and obtain JWT access token | Not required |

### Student Endpoints

| Method | Endpoint | Description | Authentication |
|---|---|---|---|
| GET | `/students/` | Retrieve all students belonging to the logged-in user | Required |
| POST | `/students/` | Create a new student record | Required |
| GET | `/students/{id}` | Retrieve a specific student | Required |
| PUT | `/students/{id}` | Update a student record | Required |
| DELETE | `/students/{id}` | Delete a student record | Required |

### Authentication Workflow

1. Register a new account using `/users/`.
2. Login through `/users/login` using your email and password.
3. Receive a JWT access token.
4. Click **Authorize** in Swagger UI.
5. Enter your credentials through the OAuth2 login form to authorize requests.
6. Access protected student endpoints using your token.

**Note:** Each authenticated user can access and manage only their own student records.