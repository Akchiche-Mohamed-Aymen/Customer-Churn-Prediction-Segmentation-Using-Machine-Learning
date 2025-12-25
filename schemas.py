from pydantic import BaseModel, Field
from typing import Optional

class ChurnOne(BaseModel):
    immediate_contact: Optional[str] = Field(
        default="Contact the customer within 24 hours to address concerns.",
        description="Reach out to customer within 24 hours"
    )
    retention_offer: Optional[str] = Field(
        default="Provide a personalized retention offer or discount.",
        description="Special offers or incentives"
    )
    feedback_session: Optional[str] = Field(
        default="Schedule a feedback call to understand dissatisfaction.",
        description="Schedule a feedback call"
    )
    account_review: Optional[str] = Field(
        default="Review recent account activity to identify issues.",
        description="Analyze account activity patterns"
    )
    personalized_service: Optional[str] = Field(
        default="Assign a dedicated account manager if applicable.",
        description="Assign dedicated account manager"
    )
    product_upgrade: Optional[str] = Field(
        default="Offer a trial of premium features to increase value.",
        description="Offer premium services"
    )
class ChurnZero(BaseModel):
    maintain_engagement: Optional[str] = Field(
        default="Maintain regular communication with the customer.",
        description="Continue regular communication"
    )
    loyalty_rewards: Optional[str] = Field(
        default="Reward loyalty with points, discounts, or perks.",
        description="Loyalty program benefits"
    )
    upsell_opportunities: Optional[str] = Field(
        default="Introduce relevant additional products or services.",
        description="Introduce additional products"
    )
    regular_monitoring: Optional[str] = Field(
        default="Continue monitoring engagement and usage patterns.",
        description="Continue tracking engagement"
    )
    value_addition: Optional[str] = Field(
        default="Share useful tips, insights, or educational content.",
        description="Share relevant financial tips"
    )
    vip_treatment: Optional[str] = Field(
        default="Acknowledge and appreciate the customer’s loyalty.",
        description="Acknowledge customer loyalty"
    )
