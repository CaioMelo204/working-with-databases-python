from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String, Numeric, create_engine, select

class Base(DeclarativeBase):
    pass

class Investment(Base):
    __tablename__ = 'investment'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(5, 2))
    
    def __repr__(self):
        return f'Investment(id={self.id}, coin={self.coin}, currency={self.currency}, amount={self.amount})'
    
engine = create_engine("sqlite:///demo.db")
Base.metadata.create_all(engine)

bitcoin = Investment(coin='bitcoin', amount=20.0, currency='USD')
dodgecoin = Investment(coin='dodgecoin', amount=100.0, currency='GBP')
etherium = Investment(coin='etherium', amount=1000.0, currency='BRL')

# with Session(engine) as session:
#    session.add(bitcoin)
#    session.add(dodgecoin)
#    session.add(etherium)
#    session.commit()

#with Session(engine) as session:
#    stmt = select(Investment).where(Investment.coin == 'bitcoin')
#    investment = session.execute(stmt).scalar_one() #only one or error
#    print(investment)
#    
#    investment = session.get(Investment, 2) # all or NONE
#    print(investment)
    
#    stmt = select(Investment).where(Investment.amount > 5) # All or NONE
#    investments = session.execute(stmt).scalars().all()
#    print(investments)

# with Session(engine) as session:
#     bitcoin = session.get(Investment, 1)
#     print(bitcoin)
    
    # Update the column
    # bitcoin.amount = 12345.12345
    # session.commit()
    
    # Delete the row
    # session.delete(bitcoin)
    # session.commit()