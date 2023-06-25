from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
    
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('Author name is required.')
        return name
    
    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if phone_number and len(phone_number) != 10:
            raise ValueError('Phone number must be exactly ten digits.')
        return phone_number

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
    
    @validates('content')
    def validate_content(self, key, content):
        if content and len(content) < 250:
            raise ValueError('Content must be at least 250 characters long.')
        return content
    
    @validates('summary')
    def validate_summary(self, key, summary):
        if summary and len(summary) > 250:
            raise ValueError('Summary must be at most 250 characters long.')
        return summary

    @validates('category')
    def validate_category(self, key, category):
        if category and category not in ['Technology', 'Science', 'Arts']:
            raise ValueError('Invalid category.')
        elif not category:
            raise ValueError('Category is required.')
        return category

    @validates('title')
    def validate_title(self, key, title):
        if title and 'clickbait' in title.lower():
            raise ValueError('Title contains clickbait.')
        return title
    
    
