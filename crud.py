from typing import Any
from uuid import UUID

from sqlalchemy.orm import Session

from models import (
    CompetitorMemory,
    CustomerFeedback,
    FinancialMemory,
    InvestorMemory,
    MarketingMemory,
    MeetingMemory,
    ProductRoadmap,
    StartupProfile,
    TeamMemory,
    TechnicalMemory,
)


def _create_record(db: Session, model: type, **fields: Any):
    record = model(**fields)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


def _get_record(db: Session, model: type, record_id: UUID):
    return db.get(model, record_id)


def _list_records(db: Session, model: type, skip: int = 0, limit: int = 100):
    return db.query(model).offset(skip).limit(limit).all()


def create_startup_profile(db: Session, **fields: Any) -> StartupProfile:
    return _create_record(db, StartupProfile, **fields)


def get_startup_profile(db: Session, startup_profile_id: UUID) -> StartupProfile | None:
    return _get_record(db, StartupProfile, startup_profile_id)


def list_startup_profiles(
    db: Session, skip: int = 0, limit: int = 100
) -> list[StartupProfile]:
    return _list_records(db, StartupProfile, skip, limit)


def create_team_memory(db: Session, **fields: Any) -> TeamMemory:
    return _create_record(db, TeamMemory, **fields)


def get_team_memory(db: Session, team_memory_id: UUID) -> TeamMemory | None:
    return _get_record(db, TeamMemory, team_memory_id)


def list_team_memories(db: Session, skip: int = 0, limit: int = 100) -> list[TeamMemory]:
    return _list_records(db, TeamMemory, skip, limit)


def create_meeting_memory(db: Session, **fields: Any) -> MeetingMemory:
    return _create_record(db, MeetingMemory, **fields)


def get_meeting_memory(db: Session, meeting_memory_id: UUID) -> MeetingMemory | None:
    return _get_record(db, MeetingMemory, meeting_memory_id)


def list_meeting_memories(
    db: Session, skip: int = 0, limit: int = 100
) -> list[MeetingMemory]:
    return _list_records(db, MeetingMemory, skip, limit)


def create_competitor_memory(db: Session, **fields: Any) -> CompetitorMemory:
    return _create_record(db, CompetitorMemory, **fields)


def get_competitor_memory(
    db: Session, competitor_memory_id: UUID
) -> CompetitorMemory | None:
    return _get_record(db, CompetitorMemory, competitor_memory_id)


def list_competitor_memories(
    db: Session, skip: int = 0, limit: int = 100
) -> list[CompetitorMemory]:
    return _list_records(db, CompetitorMemory, skip, limit)


def create_customer_feedback(db: Session, **fields: Any) -> CustomerFeedback:
    return _create_record(db, CustomerFeedback, **fields)


def get_customer_feedback(
    db: Session, customer_feedback_id: UUID
) -> CustomerFeedback | None:
    return _get_record(db, CustomerFeedback, customer_feedback_id)


def list_customer_feedback(
    db: Session, skip: int = 0, limit: int = 100
) -> list[CustomerFeedback]:
    return _list_records(db, CustomerFeedback, skip, limit)


def create_investor_memory(db: Session, **fields: Any) -> InvestorMemory:
    return _create_record(db, InvestorMemory, **fields)


def get_investor_memory(db: Session, investor_memory_id: UUID) -> InvestorMemory | None:
    return _get_record(db, InvestorMemory, investor_memory_id)


def list_investor_memories(
    db: Session, skip: int = 0, limit: int = 100
) -> list[InvestorMemory]:
    return _list_records(db, InvestorMemory, skip, limit)


def create_product_roadmap(db: Session, **fields: Any) -> ProductRoadmap:
    return _create_record(db, ProductRoadmap, **fields)


def get_product_roadmap(db: Session, product_roadmap_id: UUID) -> ProductRoadmap | None:
    return _get_record(db, ProductRoadmap, product_roadmap_id)


def list_product_roadmaps(
    db: Session, skip: int = 0, limit: int = 100
) -> list[ProductRoadmap]:
    return _list_records(db, ProductRoadmap, skip, limit)


def create_marketing_memory(db: Session, **fields: Any) -> MarketingMemory:
    return _create_record(db, MarketingMemory, **fields)


def get_marketing_memory(
    db: Session, marketing_memory_id: UUID
) -> MarketingMemory | None:
    return _get_record(db, MarketingMemory, marketing_memory_id)


def list_marketing_memories(
    db: Session, skip: int = 0, limit: int = 100
) -> list[MarketingMemory]:
    return _list_records(db, MarketingMemory, skip, limit)


def create_financial_memory(db: Session, **fields: Any) -> FinancialMemory:
    return _create_record(db, FinancialMemory, **fields)


def get_financial_memory(db: Session, financial_memory_id: UUID) -> FinancialMemory | None:
    return _get_record(db, FinancialMemory, financial_memory_id)


def list_financial_memories(
    db: Session, skip: int = 0, limit: int = 100
) -> list[FinancialMemory]:
    return _list_records(db, FinancialMemory, skip, limit)


def create_technical_memory(db: Session, **fields: Any) -> TechnicalMemory:
    return _create_record(db, TechnicalMemory, **fields)


def get_technical_memory(
    db: Session, technical_memory_id: UUID
) -> TechnicalMemory | None:
    return _get_record(db, TechnicalMemory, technical_memory_id)


def list_technical_memories(
    db: Session, skip: int = 0, limit: int = 100
) -> list[TechnicalMemory]:
    return _list_records(db, TechnicalMemory, skip, limit)
