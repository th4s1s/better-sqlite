(Disclaimer: This is a demo for CVE-2024-32002)

---

<!-- [![Contributors][contributors-shield]][contributors-url] -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="logo.png" alt="Logo" width="80" height="80">
  <h3 align="center">Better SQLite3</h3>

  <p align="center">
    Thư Viện SQLite3 Tốt Nhất Cho Ứng Dụng Python
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

## Mô tả 

Thư viện SQLite3 nhanh và đơn giản nhất cho Python, được thiết kế để tối ưu hóa hiệu suất, dễ sử dụng và đảm bảo tính an toàn. Better-SQLite3 cung cấp cách thức hiệu quả để xử lý cơ sở dữ liệu SQLite, lý tưởng cho các ứng dụng yêu cầu tương tác cơ sở dữ liệu nhanh chóng với hỗ trợ giao dịch đầy đủ.

### Tại sao nên sử dụng Better-SQLite3?

Better-SQLite3 nổi bật là một trong những thư viện tối ưu nhất để làm việc với SQLite trong Python. Nó được thiết kế để nhanh hơn hầu hết các thư viện SQLite hiện có, cung cấp các tính năng nâng cao trong khi vẫn giữ trọng lượng nhẹ và dễ sử dụng.

### Các tính năng chính:
- **Hỗ trợ giao dịch đầy đủ**: Đảm bảo tính toàn vẹn dữ liệu với quản lý giao dịch tự động.
- **Hiệu suất cao**: Tối ưu hóa cho việc thực thi nhanh chóng, làm cho nó nhanh hơn đáng kể so với các lựa chọn thay thế.
- **Hỗ trợ hàm do người dùng định nghĩa và tổng hợp**: Dễ dàng định nghĩa các hàm và tổng hợp SQLite của riêng bạn.
- **Hỗ trợ bảng ảo và tiện ích mở rộng**: Mở rộng khả năng cơ sở dữ liệu vượt ra ngoài chức năng mặc định.
- **Hỗ trợ số nguyên 64-bit**: Quản lý tự động các số nguyên lớn khi cần mà không cần cấu hình bổ sung.
- **Hỗ trợ luồng làm việc**: Xử lý hiệu quả các truy vấn lớn hoặc chậm bằng các luồng làm việc, đảm bảo rằng ứng dụng của bạn vẫn phản hồi.

## So sánh hiệu suất

Dưới đây là so sánh của Better-SQLite3 với các thư viện phổ biến khác như `sqlite` và `sqlite3`. Kết quả cho thấy hiệu suất vượt trội của Better-SQLite3 trong nhiều thao tác:

|   | Lấy 1 hàng (`get()`) | Lấy 100 hàng (`all()`) | Lấy 100 hàng từng cái một (`iterate()`) | Thêm 1 hàng (`run()`) | Thêm 100 hàng trong một giao dịch |
|---|---|---|---|---|---|
| Better-SQLite3 | 1x | 1x | 1x | 1x | 1x |
| [sqlite](https://www.npmjs.com/package/sqlite) và [sqlite3](https://www.npmjs.com/package/sqlite3) | Chậm hơn 11.7x | Chậm hơn 2.9x | Chậm hơn 24.4x | Chậm hơn 2.8x | Chậm hơn 15.6x |

Better-SQLite3 mang lại tốc độ vượt trội trong mọi thao tác, vượt xa các thư viện khác.

## Hướng dẫn cài đặt

### Yêu cầu trước:
Đảm bảo rằng bạn đã cài đặt Python. Bạn có thể kiểm tra bằng cách chạy lệnh:

```bash
$ python --version
```

### Các bước cài đặt:
1. **Clone repository:**

```bash
$ git clone --recursive https://github.com/th4s1s/better-sqlite.git
$ cd better-sqlite
```

2. **Cài đặt các thư viện phụ thuộc:**

```bash
$ pip install -r requirements.txt
```

## Ví dụ sử dụng

### Ví dụ 1: Nhập cơ sở dữ liệu cục bộ

Bạn có thể dễ dàng kết nối với cơ sở dữ liệu SQLite3 cục bộ và thực hiện các truy vấn:

```python
import better_sqlite as bq

# Kết nối với cơ sở dữ liệu cục bộ
db = bq.Database('mydatabase.db')

# Xác định tham số cho truy vấn
id = 1

# Chuẩn bị và thực thi truy vấn SQL
query = db.prepare('SELECT * FROM users WHERE id = ?').bind(id)
rows = query.execute()

# Xử lý và in kết quả truy vấn
for row in rows:
    print(f'UserID: {row[0]}')
    print(f'Username: {row[1]}')
```

### Ví dụ 2: Kết nối với DBMS từ xa

Better-SQLite3 cũng có thể kết nối với các cơ sở dữ liệu từ xa, cho phép bạn thực hiện các thao tác trên các hệ thống quản lý cơ sở dữ liệu như PostgreSQL:

```python
import better_sqlite as bq

# Thiết lập kết nối với DBMS từ xa
conn = bq.Connect('database.address:5432', 'username', 'password', 'db_name')
db = bq.Database(conn)

# Xác định tham số cho truy vấn
id = 1

# Chuẩn bị và thực thi truy vấn SQL
query = db.prepare('SELECT * FROM users WHERE id = ?').bind(id)
rows = query.execute()

# Xử lý và in kết quả truy vấn
for row in rows:
    print(f'UserID: {row[0]}')
    print(f'Username: {row[1]}')
```

---
