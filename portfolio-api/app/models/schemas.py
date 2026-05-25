from pydantic import BaseModel, Field
from typing import List, Optional

class SkillCategory(BaseModel):
    category: str
    items: List[str]

class ProjectSchema(BaseModel):
    title: str
    duration: str
    description: List[str]
    technologies: List[str]

class ExperienceSchema(BaseModel):
    role: str
    company: str
    duration: str
    highlights: List[str]

class ProfileDataResponse(BaseModel):
    name: str
    title: str
    contact: dict
    summary: str
    skills: List[SkillCategory]
    experience: List[ExperienceSchema]
    projects: List[ProjectSchema]

class AiAgentQueryRequest(BaseModel):
    query: str = Field(..., description="The interview or technical query for Sushil's AI agent")

class AiAgentQueryResponse(BaseModel):
    answer: str
    context_sources: List[str]