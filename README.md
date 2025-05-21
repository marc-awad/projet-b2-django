# Leave Management System

A Django-based application for managing leave requests in organizations. This system features a client portal for submitting leave requests and an admin panel for approving or rejecting requests.

## Features

- **Employee Portal**
  - Submit leave requests with specific dates
  - Provide reasons for leave
  - View status of submitted requests

- **Admin Dashboard**
  - Overview of all leave requests
  - Approve or reject requests
  - Filter and search through requests

## Installation

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/marc-awad/projet-b2-django.git
   cd projet-b2-django
   ```

2. Activate the virtual environment:
   ```bash
   .\env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your Resend API key:
   ```
   RESEND_SECRET_KEY = 'YOUR_KEY'
   ```

   You can obtain an API key from [Resend](https://resend.com/)

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000`

## Admin Access

To access the admin panel:
- URL: `http://127.0.0.1:8000/admin`
- Username: `lorenzo`
- Password: `graven123`

## Usage

### For Employees
1. Register or log in to your account
2. Navigate to "New Leave Request"
3. Fill in the leave details (start date, end date, reason)
4. Submit your request
5. Check "My Requests" to track the status

### For Administrators
1. Log in to the admin panel
2. View all leave requests in the dashboard
3. Review request details
4. Approve or reject requests
5. Leave optional feedback for rejected requests

## Technologies

- Django
- Python
- HTML/CSS
- JavaScript
- Resend API (for email notifications)

## Development

To contribute to this project:

1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit a pull request

---

Made with ❤️ as part of B2 Django project - Sup de Vinci
