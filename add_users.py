from app import db, User  # ייבוא של האפליקציה ושל המודל

# יצירת משתמשים חדשים
user1 = User(name='John Doe', age=30, email='john.doe@example.com')
user2 = User(name='Jane Smith', age=25, email='jane.smith@example.com')

# הוספתם לבסיס הנתונים
db.session.add(user1)
db.session.add(user2)
db.session.commit()

print("Users added successfully!")
