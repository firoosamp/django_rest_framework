# Library API

## Setup

1. Clone the repository
2. Create virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Create superuser: `python manage.py createsuperuser`
6. Run server: `python manage.py runserver`

## API Endpoints

- `/api/authors/` - CRUD authors
- `/api/books/` - CRUD books (staff-only for create/update/delete)
- `/api/borrowers/` - Borrow books (authenticated users only)
- `/api/token/` - Get JWT token
- `/api/token/refresh/` - Refresh JWT token
- `/swagger/` - API documentation

### Example: Borrow a book
```json
POST /api/borrowers/
{
    "book": 1
}
