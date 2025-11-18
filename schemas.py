"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# -------- App Schemas --------

class Event(BaseModel):
    """
    Local events (e.g., food festivals, markets, local concerts)
    Collection: "event"
    """
    title: str = Field(..., description="Event name")
    description: Optional[str] = Field(None, description="Short description")
    category: str = Field("Food Festival", description="Category, e.g., Food Festival, Market")
    city: str = Field(..., description="City or town")
    venue: Optional[str] = Field(None, description="Venue name")
    date: datetime = Field(..., description="Event start date/time (ISO)")
    price: float = Field(0, ge=0, description="Ticket price per person")
    capacity: int = Field(0, ge=0, description="Total capacity")
    image_url: Optional[str] = Field(None, description="Cover image")

class Booking(BaseModel):
    """
    Bookings for events
    Collection: "booking"
    """
    event_id: str = Field(..., description="Target event _id as string")
    name: str = Field(..., description="Guest full name")
    email: str = Field(..., description="Guest email")
    quantity: int = Field(..., ge=1, le=10, description="Number of tickets")

# Example schemas (kept for reference)
class User(BaseModel):
    name: str
    email: str
    address: str
    age: Optional[int] = None
    is_active: bool = True

class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category: str
    in_stock: bool = True
