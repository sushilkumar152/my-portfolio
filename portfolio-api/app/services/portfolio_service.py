from typing import Dict, Any
from app.dao.profile_dao import ProfileDAO
from app.models.schemas import ProfileDataResponse, AiAgentQueryResponse

class PortfolioService:
    """
    Business Logic Layer. Handles orchestration, data transforming, 
    and simulated Agentic AI processing.
    """
    def __init__(self):
        # Injecting the Data Access Object layer
        self.profile_dao = ProfileDAO()

    def get_complete_profile(self) -> ProfileDataResponse:
        """Orchestrates business logic to retrieve complete structured portfolio data."""
        raw_data = self.profile_dao.get_raw_profile_data()
        return ProfileDataResponse(**raw_data)

    async def orchestrate_ai_agent(self, user_query: str) -> AiAgentQueryResponse:
        """
        Simulates an Agentic AI workflow (RAG) that scans your profile data[cite: 1] 
        and formulates an automated context-aware professional answer.
        """
        query_lower = user_query.lower()
        profile = self.profile_dao.get_raw_profile_data()
        
        # Simulated Agentic Tool Lookup logic
        if "ai" in query_lower or "agent" in query_lower or "bot" in query_lower:
            answer = (
                f"Sushil has deep hands-on expertise with Agentic and Generative AI. "
                f"He recently built an 'AI Agent for Development' that optimized unit testing using pytest "
                f"and reduced manual review efforts by 80%. He also spent 2 months enhancing a "
                f"RASA-based Conversational Chatbot in the Pharma SaaS domain."
            )
            sources = ["Projects: AI Agent for Development", "Projects: RASA Conversational Chatbot"]
            
        elif "backend" in query_lower or "python" in query_lower or "fastapi" in query_lower or "flask" in query_lower:
            answer = (
                f"Sushil is an expert backend engineer. At IntegriChain, he designed and developed "
                f"scalable backend microservices and RESTful APIs using Python, Flask, FastAPI, "
                f"and SQLAlchemy, while managing asynchronous tasks via Celery."
            )
            sources = ["Experience: IntegriChain Fullstack Role", "Technical Skills Matrix"]
            
        elif "frontend" in query_lower or "angular" in query_lower or "ui" in query_lower:
            answer = (
                f"On the frontend, Sushil builds clean, modular enterprise architectures. "
                f"He utilizes Angular along with PrimeNG to build highly reusable components, "
                f"significantly improving user interface consistency."
            )
            sources = ["Experience: IntegriChain Frontend Architecture", "Technical Skills Matrix"]
            
        else:
            # Fallback general agent routing
            answer = (
                f"Sushil Kumar is a Fullstack Software Engineer with 4.5+ years of experience "
                f"specializing in Python, FastAPI, Angular, and enterprise cloud data pipelines. "
                f"He currently contributes to IntegriChain's ICyte Platform serving over 250 manufacturers."
            )
            sources = ["Profile Summary Data"]

        return AiAgentQueryResponse(
            answer=answer,
            context_sources=sources
        )