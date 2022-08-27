from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Point(Base):
    __tablename__ = "Point"

    id = Column(Integer, primary_key=True, index=True)
    x = Column(Integer)
    y = Column(Integer)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")