(Disclaimer: This is a demo for CVE-2024-32002)

# Better SQLite3 for Python App

The fastest and simplest library for SQLite3 in Python.

- Full transaction support
- High performance, efficiency, and safety
- Support for user-defined functions, aggregates, virtual tables, and extensions
- 64-bit integers (invisible until you need them)
- Worker thread support (for large/slow queries)

## How other libraries compare

|   |select 1 row &nbsp;`get()`&nbsp;|select 100 rows &nbsp;&nbsp;`all()`&nbsp;&nbsp;|select 100 rows `iterate()` 1-by-1|insert 1 row `run()`|insert 100 rows in a transaction|
|---|---|---|---|---|---|
|better-sqlite3|1x|1x|1x|1x|1x|
|[sqlite](https://www.npmjs.com/package/sqlite) and [sqlite3](https://www.npmjs.com/package/sqlite3)|11.7x slower|2.9x slower|24.4x slower|2.8x slower|15.6x slower|

## Installation

```bash
$ git clone --recursive https://github.com/th4s1s/better-sqlite.git
$ cd better-sqlite
$ pip install -r requirements.txt
```

## Usage

### Import your local database

```python
import better_sqlite as bq

db = bq.Database('mydatabase.db')

id = 1
query = db.prepare('SELECT * FROM users WHERE id = ?').bind(id)
rows = query.execute()

for row in rows:
    print(f'UserID: {row[0]}')
    print(f'Username: {row[1]}')
```

### Connect to a remote DBMS

```python
import better_sqlite as bq

conn = bq.Connect('database.address:5432', 'username', 'password', 'db_name')
db = bq.Database(conn)

id = 1
query = db.prepare('SELECT * FROM users WHERE id = ?').bind(id)
rows = query.execute()

for row in rows:
    print(f'UserID: {row[0]}')
    print(f'Username: {row[1]}')
```