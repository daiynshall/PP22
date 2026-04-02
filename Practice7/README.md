# PhoneBook PostgreSQL App

## Files
- `config.py` - reads database config
- `connect.py` - creates PostgreSQL connection
- `db_init.py` - creates the `phonebook` table
- `phonebook.py` - main console app
- `contacts.csv` - example CSV file
- `database.ini` - ready DB config
- `database.ini.example` - example DB config
- `requirements.txt` - dependency list

## Default PostgreSQL config

The project is prefilled with these default values:

```ini
[postgresql]
host=localhost
database=phonebook_db
user=postgres
password=postgres
port=5432
```

If your local PostgreSQL password is different, edit only the `password` value in `database.ini`.

## Setup

1. Install dependency:
   ```bash
   pip install -r requirements.txt
   ```

2. Create PostgreSQL database:
   ```sql
   CREATE DATABASE phonebook_db;
   ```

3. Make sure your PostgreSQL user is:
   - username: `postgres`
   - password: `postgres`

   If not, update `database.ini`.

## Run

```bash
python phonebook.py
```

## CSV format

```csv
first_name,phone_number
John,87012223344
Alice,87775556677
Bob,87058889900
```
