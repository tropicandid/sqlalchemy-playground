from extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text

##TODO: Step 1
# 1. Create a model with the tablename 'patients'.
# 2. Include columns for ID<int>, Name<string>, Birthday<string>
class Patient(db.Model): #NEW TABLE
    __tablename__ = 'patients'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(500))
    birthday: Mapped[str] = mapped_column(String(100))