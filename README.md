# Daily Win

Week 9 Zorentia application. Flask, vanilla JavaScript and SQLAlchemy Core/MySQL.
The original generated screens, orange/dark styling and sidebar are retained.
Register an email and password (8–128 characters), then save one win of up to
150 characters per local calendar day. Records belong to your account.

## Run locally

From the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
openssl rand -hex 32
```

Create a dedicated MySQL database and user. For example, run these statements
inside the MySQL client as an administrator, replacing the password:

```sql
CREATE DATABASE daily_win CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'dailywin'@'localhost' IDENTIFIED BY 'YOUR_DATABASE_PASSWORD';
GRANT ALL PRIVILEGES ON daily_win.* TO 'dailywin'@'localhost';
```

Edit `.env`:

```dotenv
DATABASE_URL=mysql+mysqlconnector://dailywin:YOUR_DATABASE_PASSWORD@localhost:3306/daily_win
JWT_SECRET=PASTE_THE_RANDOM_VALUE_FROM_OPENSSL
JWT_ISSUER=zorentia-app
COOKIE_SECURE=false
```

URL-encode special characters in the database password when placing it in
`DATABASE_URL`. Then:

```bash
flask --app 'fullstack:create_app()' init-db
flask --app 'fullstack:create_app()' run --debug
```

Open http://127.0.0.1:5000/register. MySQL stores accounts and wins persistently.
`init-db` creates missing tables and preserves existing records. It is not a
migration for an already deployed copy of the original generated schema.
Use a fresh database for this repaired version.

Tests use isolated SQLite databases, including a file-backed restart check:

```bash
python -m pytest -q
```

## AWS EC2

The supplied configurations assume a **separate EC2 instance** and repository
directory `/home/ubuntu/daily-win-week9`. Install MySQL, Python venv, Git,
Nginx and Certbot using the deployment guide, then:

```bash
git clone https://github.com/DanielHuynh611/daily-win-week9.git
cd daily-win-week9
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
nano .env
chmod 600 .env
```

Create the dedicated MySQL database/user as above. Set the real database
credentials, a random `JWT_SECRET`, and `COOKIE_SECURE=true` in `.env`.
A secure cookie requires HTTPS; use `false` only for local or temporary HTTP testing.

```bash
flask --app 'fullstack:create_app()' init-db
flask --app 'fullstack:create_app()' routes
python -m pytest -q
sudo cp deploy/daily-win.service /etc/systemd/system/daily-win.service
sudo systemctl daemon-reload
sudo systemctl enable --now daily-win
curl http://127.0.0.1:8000/health
sudo cp deploy/nginx.conf /etc/nginx/sites-available/daily-win
sudo ln -s /etc/nginx/sites-available/daily-win /etc/nginx/sites-enabled/daily-win
sudo nginx -t
sudo systemctl reload nginx
```

In Namecheap add an A record with Host `daily-win`, Value equal to the new
instance's Elastic IP, and TTL Automatic. Keep the existing `@` and `www`
records and existing application intact. Allow HTTP/HTTPS in the security group.
After the subdomain resolves to the instance:

```bash
sudo certbot --nginx -d daily-win.track-my-habit.me
curl https://daily-win.track-my-habit.me/health
sudo certbot renew --dry-run
```

Test registration, saving, refreshing and signing back in at the public HTTPS URL.
For another hostname or repository directory, update the supplied deployment
files before installing them. If sharing an EC2 instance, give the new app a
separate database, systemd/Nginx configuration and a free Gunicorn port.

To update this app later:

```bash
cd /home/ubuntu/daily-win-week9
git pull --ff-only origin main
source .venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart daily-win
sudo systemctl status daily-win --no-pager
curl https://daily-win.track-my-habit.me/health
```
