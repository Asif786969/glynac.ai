# Employee API

A Flask RESTful API to manage synthetic employee data with PostgreSQL.

## Setup

1. Create virtualenv & activate it
2. Install dependencies: `pip install -r requirements.txt`
3. Set up PostgreSQL database and update `.env`
4. Run migrations:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
5. Start the server: `python run.py`
