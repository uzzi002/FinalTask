# Django Capstone Project

## Installation

### Using Virtual Environment
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

### Using Docker
1. Build the Docker image:
   ```bash
   docker build -t capstoneeventplanner .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 capstoneeventplanner
   ```

## Notes
- Ensure that your `.env` file or settings for sensitive data (e.g., database, secret key) are not committed to the repository.
