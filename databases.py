from model import Base, User 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_user(name,secret_word):
    """Add a user to the DB."""
    
    user = User(username=name, password_hash=secret_word)
    user.hash_password(password=secret_word)
    #there is a line of code missing here, what else does a user need?
    session.add(user)
    session.commit()

def get_user(username):
    """Find the first user in the DB, by their username."""
    return session.query(User).filter_by(username=username).first()
def food(user, fav_food):
	user.fav_food = fav_food
	session.commit()



from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
def add_pro(price,name,picture_link,description):
    product_object = Product(
        price=price,
        name=name,
        picture_link=picture_link,
        description= description
        )
    session.add(product_object)
    session.commit()

def edit_pro(id,name,description,price,picture_link):
    product_object = session.query(
       Product).filter_by(
       id=id).first()
    product_object.name=name
    product_object.price=price
    product_object.picture_link=picture_link
    product_object.description=description
    session.commit()

def delete_pro(id,name,description,price,picture_link):
    session.query(Product).filter_by(
       name=name).delete()
    session.commit()

def query_all():
    students = session.query(
      Product).all()
   return product


print(query_all())

def query_by_name(name):
    Product = session.query(
       Product).filter_by(
       name=name).first()
    return Product







