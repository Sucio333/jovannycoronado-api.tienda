CREATE DATABASE IF NOT EXISTS tienda_online_db
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'tienda_user'@'localhost'
  IDENTIFIED BY 'CambiaEstaClave_2026!';
CREATE USER IF NOT EXISTS 'tienda_user'@'127.0.0.1'
  IDENTIFIED BY 'CambiaEstaClave_2026!';

GRANT ALL PRIVILEGES ON tienda_online_db.* TO 'tienda_user'@'localhost';
GRANT ALL PRIVILEGES ON tienda_online_db.* TO 'tienda_user'@'127.0.0.1';

FLUSH PRIVILEGES;