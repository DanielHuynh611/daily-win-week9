-- Fresh MySQL schema. All generated win feature routes share this owned store.
-- Run against the new application's database, never against another app's database.
CREATE TABLE IF NOT EXISTS users (
  id CHAR(36) NOT NULL,
  email VARCHAR(254) NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at DATETIME NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY uq_users_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS f_99d93461__wins (
  id CHAR(36) NOT NULL,
  user_id CHAR(36) NOT NULL,
  date DATE NOT NULL,
  achievement_text VARCHAR(150) NOT NULL,
  timezone VARCHAR(64) NOT NULL,
  created_at DATETIME NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY uq_win_user_date (user_id, date),
  CONSTRAINT fk_win_user FOREIGN KEY (user_id) REFERENCES users (id),
  CONSTRAINT ck_win_text CHECK (CHAR_LENGTH(TRIM(achievement_text)) BETWEEN 1 AND 150)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
