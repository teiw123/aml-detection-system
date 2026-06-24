from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Database setup
engine = create_engine("sqlite:///transactions.db", echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class TransactionLog(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    card_number = Column(String)
    business_id = Column(String)
    kyc = Column(Boolean)
    aml = Column(Boolean)
    status = Column(String)
    fine = Column(Integer)

Base.metadata.create_all(bind=engine)

# FastAPI setup
app = FastAPI()

class Transaction(BaseModel):
    kyc: bool
    aml: bool
    card_number: str
    business_id: str

@app.post("/verify")
def verify_transaction(tx: Transaction):
    # Compliance logic
    if tx.kyc and tx.aml:
        status, fine = "approved", 0
    elif tx.kyc and not tx.aml:
        status, fine = "approved", 200
    else:
        status, fine = "rejected", 0

    # Log to database
    db = SessionLocal()
    log_entry = TransactionLog(
        card_number=tx.card_number,
        business_id=tx.business_id,
        kyc=tx.kyc,
        aml=tx.aml,
        status=status,
        fine=fine
    )
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)
    db.close()

    # Simulate deduction
    if fine > 0:
        # In a real system, this would call the bank’s API
        print(f"Deducted K{fine} from account {tx.business_id}")

    return {"status": status, "fine": fine}
