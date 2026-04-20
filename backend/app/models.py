from sqlalchemy import Date, DateTime, Float, ForeignKey, Integer, String, UniqueConstraint, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import date, datetime

class Base(DeclarativeBase):
  pass

class Location(Base):
  __tablename__ = "locations"
  __table_args__ = (
    UniqueConstraint("lat", "long", name="uq_location_lat_long"),
  )

  id: Mapped[int] = mapped_column(primary_key=True)
  lat: Mapped[float] = mapped_column(Float)
  long: Mapped[float] = mapped_column(Float)
  station_url: Mapped[str] = mapped_column(String)
  created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

class Forecast(Base):
  __tablename__ = "forecasts"
  __table_args__ = (
    UniqueConstraint("location_id", "day", "hour", name="ug_forecast_loc_day_hour"),
  )

  id: Mapped[int] = mapped_column(primary_key=True)
  location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))
  day: Mapped[date] = mapped_column(Date)
  hour: Mapped[int] = mapped_column(Integer)
  high: Mapped[int] = mapped_column(Integer)
  low: Mapped[int] = mapped_column(Integer)
  created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())