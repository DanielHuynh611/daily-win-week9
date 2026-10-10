CREATE TABLE `f_99d93461__wins` (
  `id` CHAR(36) NOT NULL,
  `date` DATE NOT NULL,
  `achievement_text` VARCHAR(150) NOT NULL,
  `created_at` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `f_aca07cc7__entry_local_dates` (
  `id` CHAR(36) NOT NULL,
  `entry_id` CHAR(36) NOT NULL,
  `local_date` DATE NOT NULL,
  `created_at_utc` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `f_86a57805__achievements` (
  `id` CHAR(36) NOT NULL,
  `achievement_text` VARCHAR(150) NOT NULL,
  `recorded_date` DATE NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `f_86f08838__daily_win_entries` (
  `id` CHAR(36) NOT NULL,
  `entry_date` DATE NOT NULL,
  `achievement_text` VARCHAR(150) NOT NULL,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_entry_date` (`entry_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- No database tables are required for feature: capability_save_button_5553765f


-- No database tables are required for feature: capability_single_screen_interface_20b1b421


-- No database tables are required for feature: capability_non_empty_validation_c7515c58


CREATE TABLE `f_2a9520cb__achievements` (
  `id` CHAR(36) NOT NULL,
  `text` VARCHAR(150) NOT NULL,
  `date` DATE NOT NULL,
  `created_at` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- No database tables are required for feature: capability_current_date_display_67c458ab


CREATE TABLE `f_00baa1bc__daily_wins` (
  `id` CHAR(36) NOT NULL,
  `entry_date` DATE NOT NULL,
  `achievement_text` VARCHAR(150) NOT NULL,
  `created_at` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- No database tables are required for feature: capability_confirmation_message_23ce028f


CREATE TABLE `f_76537cc2__microcopy_strings` (
  `id` CHAR(36) NOT NULL,
  `key` VARCHAR(100) NOT NULL,
  `text_content` VARCHAR(500) NOT NULL,
  `context` VARCHAR(200),
  `is_active` TINYINT(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;