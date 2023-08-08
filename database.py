from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

link = create_engine('mysql+mysqldb://root:tupassword@localhost:3306/datos_app_contextos')
Sesion = sessionmaker(link)
sesion = Sesion()

