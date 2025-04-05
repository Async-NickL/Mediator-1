import psycopg2
from werkzeug.security import check_password_hash, generate_password_hash

conn=psycopg2.connect("postgresql://midd_owner:npg_lAmbJFE9GTh1@ep-rough-bread-a1hcwdyh-pooler.ap-southeast-1.aws.neon.tech/midd?sslmode=require")

cur=conn.cursor()


# Insert a test supervisor user
password = generate_password_hash("ADMIN")
try:
    cur.execute("""
        INSERT INTO admin_info(ausername, apass, apost)
        VALUES('ADMIN', %s, 'supervisor')
    """, (password,))
except psycopg2.errors.UniqueViolation:
    print("Supervisor user already exists")
    conn.rollback()

conn.commit()
cur.close()
conn.close()

print("All tables created successfully!")
