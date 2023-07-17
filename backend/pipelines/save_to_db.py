from sqlalchemy import create_engine,column,String,Integer,CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base=declarative_base()

class Prediction(Base):
    __tablename__ ='predictions'

    date =column("date",String)
    home =column("home",CHAR)
    away =column("away",CHAR)
    home_odd=column('home_odd',CHAR)
    draw_odd=column('draw_odd',CHAR)
    away_odd=column('away_odd',CHAR)
    prediction=column('prediction',Integer)


    def __init__(self,date,home,away,home_odd,draw_odd,away_odd,prediction)
        self.date=date
        self.home=home
        self.away=away
        self.home_odd=home_odd
        self.draw_odd=draw_odd
        self.away_odd=away_odd
        self.prediction=prediction

    def __rep__(self):
        return f"({self.home} vs {self.away} )"
    

engine=create_engine('sqlite:///predict.db',echo=True)

Base.metadata.create_all(bind=engine)

Session=sessionmaker(bind=engine)
session =Session()
