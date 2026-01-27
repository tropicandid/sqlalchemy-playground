from extensions import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text

##TODO: Step 2
# 1. Modify the 'patients' table by adding a column for Address<string> and a column for Phone Number<string>.
# 2. You will need to perform a migration to complete this step
# 3. View your database after to confirm the changes have been applied as desired.
class Patient(db.Model):
    __tablename__ = 'patients'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250))
    birthday: Mapped[str] = mapped_column(String(50))
    address: Mapped[str] = mapped_column(String(500)) #NEW LINE
    phone_number: Mapped[str] = mapped_column(String(15)) #NEW LINE