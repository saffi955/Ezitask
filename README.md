# Ezitask

A Django-based web application for task and attendance management, created as an internship test project for Ezi Technologies.

## Project Overview

Ezitask is a web application built with Django and Django REST Framework that provides features for:
- **Attendance Management**: Track and manage attendance records
- **User Authentication**: Sign up and sign-in functionality
- **User Profiles**: Profile management with profile picture support
- **Task Management**: Manage tasks and activities

## Project Structure

```
Ezitask/
├── ezi task/                      # Main Django project directory
│   ├── attendence/                # Attendance app
│   │   ├── models.py              # Database models for attendance
│   │   ├── views.py               # API views
│   │   ├── serializers.py         # DRF serializers
│   │   ├── urls.py                # URL routing
│   │   ├── admin.py               # Django admin configuration
│   │   ├── apps.py                # App configuration
│   │   └── migrations/            # Database migrations
│   │
│   ├── ezitask/                   # Main project settings
│   │   ├── settings.py            # Django settings
│   │   ├── urls.py                # Main URL configuration
│   │   ├── wsgi.py                # WSGI configuration
│   │   └── asgi.py                # ASGI configuration
│   │
│   ├── templates/                 # HTML templates
│   │   ├── base.html              # Base template
│   │   ├── signin.html            # Sign-in page
│   │   ├── signup.html            # Sign-up page
│   │   └── profile.html           # User profile page
│   │
│   ├── static/                    # Static files
│   │   ├── css/                   # Stylesheets
│   │   ├── js/                    # JavaScript files
│   │   └── images/                # Image assets
│   │
│   ├── media/                     # User-uploaded files
│   │   └── profile_images/        # Profile pictures
│   │
│   ├── manage.py                  # Django management script
│   ├── Pipfile                    # Python dependencies
│   └── Pipfile.lock               # Locked dependencies
│
└── database/
    └── ezitask_database.sql       # Database dump/schema
```

## Technologies Used

- **Backend**: Django, Django REST Framework (DRF)
- **Database**: SQL (database schema included)
- **Frontend**: HTML, CSS, JavaScript
- **Environment Management**: Pipenv

## Installation

### Prerequisites
- Python 3.7+
- Pipenv or pip
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/saffi955/Ezitask.git
   cd Ezitask
   ```

2. **Navigate to the project directory**
   ```bash
   cd "ezi task"
   ```

3. **Install dependencies**
   ```bash
   pipenv install
   ```
   
   Or using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://localhost:8000/`

## Features

### Authentication
- User registration (Sign-up)
- User login (Sign-in)
- Profile management with image upload

### Attendance Management
- Track attendance records
- View attendance history
- REST API endpoints for attendance data

### User Profiles
- Profile customization
- Default profile picture
- Profile editing

## API Endpoints

### Attendance Endpoints
- `GET /api/attendance/` - List all attendance records
- `POST /api/attendance/` - Create attendance record
- `GET /api/attendance/{id}/` - Retrieve specific record
- `PUT /api/attendance/{id}/` - Update record
- `DELETE /api/attendance/{id}/` - Delete record

## Database Setup

To load the database schema:

```bash
# Using MySQL
mysql -u username -p database_name < database/ezitast_database.sql

# Using PostgreSQL
psql -U username -d database_name -f database/ezitast_database.sql
```

## Configuration

Key settings in `ezitask/settings.py`:
- `INSTALLED_APPS`: Includes the `attendence` app and DRF
- `DATABASES`: Configure your database connection
- `MEDIA_URL` & `MEDIA_ROOT`: Configuration for user uploads
- `STATIC_URL` & `STATIC_ROOT`: Configuration for static files

## File Uploads

User profile images are stored in:
```
media/profile_images/
```

Default profile picture is available at:
```
media/profile_images/default_profile_picture.png
```

## Testing

Run tests with:
```bash
python manage.py test
```

## Admin Interface

Access Django admin at `http://localhost:8000/admin/`

Use your superuser credentials to:
- Manage attendance records
- View and manage user accounts
- Configure app settings

## Development

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files
```bash
python manage.py collectstatic
```

## Troubleshooting

### Database Connection Issues
- Verify database credentials in `settings.py`
- Ensure database server is running
- Check database name matches configuration

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Port Already in Use
```bash
python manage.py runserver 8001
```

## Project Notes

- This is an **internship test project** for Ezi Technologies
- The project may be under active development
- Some features may be in beta or not fully implemented

## Future Enhancements

- Enhanced UI/UX improvements
- Additional attendance analytics
- Notification system
- Report generation
- Role-based access control (RBAC)

## License

This project is created as an internship test for Ezi Technologies.

## Contact & Support

For questions or issues, please contact the project maintainer at:
- GitHub: [@saffi955](https://github.com/saffi955)

---

**Last Updated**: March 2023
**Status**: Internship Project
