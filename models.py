import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, Float, Integer, JSON, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# 1. Startup Profile Memory
class StartupProfile(Base):
    __tablename__ = 'startup_profile'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    startup_name = Column(String, nullable=False, default="EcoCart")
    industry = Column(String)
    stage = Column(String)
    country = Column(String)
    mission = Column(Text)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# 2. Team Memory
class TeamMemory(Base):
    __tablename__ = 'team_memory'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    role = Column(String)
    skills = Column(JSON)  # e.g., ["Python", "Node.js"]
    availability = Column(String)

# 3. Meeting Memory ⭐
class MeetingMemory(Base):
    __tablename__ = 'meeting_memory'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = Column(DateTime, default=datetime.utcnow)
    discussion = Column(Text)
    decision = Column(Text)
    pending_tasks = Column(JSON)
    problems = Column(Text)
    deadlines = Column(DateTime)

# 4. Competitor Memory
class CompetitorMemory(Base):
    __tablename__ = 'competitor_memory'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, unique=True, nullable=False)
    pricing = Column(String)
    features = Column(JSON)
    pros = Column(Text)
    cons = Column(Text)
    reviews = Column(Text)

# 5. Customer Feedback Memory
class CustomerFeedback(Base):
    __tablename__ = 'customer_feedback'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_name = Column(String)
    feedback_text = Column(Text)
    sentiment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# 6. Investor Memory
class InvestorMemory(Base):
    __tablename__ = 'investor_memory'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    investor_name = Column(String, nullable=False)
    meeting_date = Column(DateTime)
    questions_asked = Column(Text)
    concerns = Column(Text)
    interest_level = Column(String)
    next_follow_up = Column(DateTime)

# 7. Product Roadmap Memory
class ProductRoadmap(Base):
    __tablename__ = 'product_roadmap'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    version = Column(String, nullable=False)
    features = Column(JSON)

# 8. Marketing Memory
class MarketingMemory(Base):
    __tablename__ = 'marketing_memory'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    channel = Column(String, nullable=False)
    views = Column(Integer, default=0)
    clicks = Column(Integer, default=0)
    conversions = Column(Integer, default=0)
    budget = Column(Float, default=0.0)
    recorded_at = Column(DateTime, default=datetime.utcnow)

# 9. Financial Memory
class FinancialMemory(Base):
    __tablename__ = 'financial_memory'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    expenses = Column(Float, default=0.0)
    revenue = Column(Float, default=0.0)
    burn_rate = Column(Float, default=0.0)
    mrr = Column(Float, default=0.0)
    runway = Column(Float, default=0.0)
    recorded_at = Column(DateTime, default=datetime.utcnow)

# 10. Technical Memory
class TechnicalMemory(Base):
    __tablename__ = 'technical_memory'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    architecture = Column(Text)
    apis = Column(JSON)
    bugs = Column(Text)
    tech_stack = Column(JSON)
    deployment = Column(Text)
    updated_at = Column(DateTime, default=datetime.utcnow)