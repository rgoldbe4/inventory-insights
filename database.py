from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Database
Base = declarative_base()
postgres_engine = create_engine("postgresql+psycopg2://zeqficdoiljlhd:3ed187c22819aadda23612afc4aaba722687b87946061b7877a4761abfc75a41@ec2-52-44-31-100.compute-1.amazonaws.com:5432/d17vgsv82f604a", echo=True)
Session = sessionmaker(bind=postgres_engine)
