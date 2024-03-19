## Database setup

1. Install the mysql database according to your system (for windows follow [this](https://www.w3schools.com/mysql/mysql_install_windows.asp) link.)
2. Set everything up (including adding `'C:\Program Files\MySQL\MySQL Server 8.0\bin'` to the path enviromental variables)
3. Connect to the `mysql` bash using `mysql -u root -p <set-password>` command and create a `spdb` database using `CREATE DATABASE spdb;` command.
4. Set up your `.env` file with the variables:
   - `DB_HOST="localhost"`
   - `DB_USER="root"`
   - `DB_PASSWORD="<your-password>"`
   - `DB_NAME="spdb"`
5. To test if everything is set up correctly - please execute `python3 ./src/test/scripts/db_connectivity_test.py`
