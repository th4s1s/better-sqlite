(Disclaimer: This is a demo for CVE-2024-32002)

---

<!-- [![Contributors][contributors-shield]][contributors-url] -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="images/logo.png" alt="Logo" width="80" height="80">
  <h3 align="center">Better SQLite3</h3>

  <p align="center">
    Better SQLite3 for Python App
    <!-- <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a> -->
  </p>
</div>

[![en](https://img.shields.io/badge/lang-en-green.svg)](https://github.com/th4s1s/better-sqlite/blob/master/README.md)
[![vn](https://img.shields.io/badge/lang-vn-red.svg)](https://github.com/th4s1s/better-sqlite/blob/master/README-VN.md)
[![con](https://img.shields.io/badge/contributors-blue)](https://github.com/th4s1s/better-sqlite/graphs/contributors)



<!-- TABLE OF CONTENTS -->
<!-- <details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details> -->


# Description

The fastest and simplest library for SQLite3 in Python, designed for high performance, ease of use, and robustness. Better-SQLite3 offers an efficient way to handle SQLite databases, making it ideal for applications that require quick database interactions with full transaction support.

## Why Better-SQLite3?

Better-SQLite3 stands out as one of the most optimized libraries for working with SQLite in Python. It's designed to be faster than most existing SQLite libraries, offering advanced features while remaining lightweight and easy to use.

### Key Features:
- **Full Transaction Support**: Ensures data integrity with automatic transaction management.
- **High Performance**: Optimized for fast execution, making it significantly faster than alternatives.
- **User-Defined Functions and Aggregates**: Easily define your own SQLite functions and aggregates.
- **Support for Virtual Tables and Extensions**: Extend the database capabilities beyond the default functionality.
- **64-bit Integers**: Automatically manage large integers when needed without additional configuration.
- **Worker Thread Support**: Efficiently handle large or slow queries using worker threads, ensuring that your application remains responsive.

## Performance Comparison

Below is a comparison of Better-SQLite3 against other popular libraries such as `sqlite` and `sqlite3`. The results demonstrate Better-SQLite3's superior performance in various operations:

|   | Select 1 row (`get()`) | Select 100 rows (`all()`) | Select 100 rows one-by-one (`iterate()`) | Insert 1 row (`run()`) | Insert 100 rows in a transaction |
|---|---|---|---|---|---|
| Better-SQLite3 | 1x | 1x | 1x | 1x | 1x |
| [sqlite](https://www.npmjs.com/package/sqlite) and [sqlite3](https://www.npmjs.com/package/sqlite3) | 11.7x slower | 2.9x slower | 24.4x slower | 2.8x slower | 15.6x slower |

Better-SQLite3 offers unparalleled speed in all operations, outperforming other libraries by a wide margin.

## Installation Guide

### Prerequisites:
Ensure you have Python installed. You can verify by running:

```bash
$ python --version
```

### Installation Steps:
1. **Clone the repository:**

```bash
$ git clone --recursive https://github.com/th4s1s/better-sqlite.git
$ cd better-sqlite
```

2. **Install dependencies:**

```bash
$ pip install -r requirements.txt
```

## Usage Examples

### Example 1: Import a Local Database

You can easily connect to a local SQLite3 database and execute queries using `better-sqlite`:

```python
import better_sqlite as bq

# Connect to the local database
db = bq.Database('mydatabase.db')

# Define a parameter for query
id = 1

# Prepare and execute the SQL query
query = db.prepare('SELECT * FROM users WHERE id = ?').bind(id)
rows = query.execute()

# Process and print the query result
for row in rows:
    print(f'UserID: {row[0]}')
    print(f'Username: {row[1]}')
```

### Example 2: Connect to a Remote DBMS

Better-SQLite3 can also connect to remote databases, allowing you to perform operations on database management systems like PostgreSQL:

```python
import better_sqlite as bq

# Establish connection to the remote DBMS
conn = bq.Connect('database.address:5432', 'username', 'password', 'db_name')
db = bq.Database(conn)

# Define query parameter
id = 1

# Prepare and execute the SQL query
query = db.prepare('SELECT * FROM users WHERE id = ?').bind(id)
rows = query.execute()

# Process and print the query result
for row in rows:
    print(f'UserID: {row[0]}')
    print(f'Username: {row[1]}')
```

---
