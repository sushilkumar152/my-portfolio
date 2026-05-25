from typing import Dict, Any

class ProfileDAO:
    """
    Data Access Object handling data retrieval operations for the portfolio.
    Isolates data access logic from core business services.
    """
    
    def get_raw_profile_data(self) -> Dict[str, Any]:
        """Simulates a database fetch returning your professional resume details[cite: 1]."""
        return {
            "name": "Sushil Kumar", #[cite: 1]
            "title": "Fullstack Software Engineer", #
            "contact": {
                "email": "kumarsu0701@gmail.com", #[cite: 1]
                "phone": "+91-9262352538", #[cite: 1]
                "location": "Pune, INDIA", #[cite: 1]
                "linkedin": "linkedin.com/in/skumar0701" #[cite: 1]
            },
            "summary": (
                "Full Stack Software Engineer with 4.5+ years of experience developing scalable, "
                "enterprise-grade applications in the Healthcare and Pharmaceutical SaaS domain."
            ),
            "skills": [
                {"category": "Languages & Core", "items": ["Python", "Java", "PHP", "JavaScript"]}, #
                {"category": "Frameworks & UI", "items": ["FastAPI", "Flask", "Angular", "React.js", "PrimeNG"]}, #
                {"category": "Databases & Cloud", "items": ["PostgreSQL", "Snowflake", "SQL Server", "MySQL", "AWS"]}, #
                {"category": "AI & Automation", "items": ["Agentic AI", "Generative AI", "Claude Code", "Github Copilot"]} #
            ],
            "experience": [
                {
                    "role": "Fullstack Software Engineer", #
                    "company": "IntegriChain", #
                    "duration": "Jan 2022 - Present", #
                    "highlights": [
                        "Designed and developed scalable backend microservices and RESTful APIs using Python, Flask, FastAPI, and SQLAlchemy.",
                        "Developed reusable and modular frontend components with Angular and PrimeNG, significantly improving user experience.",
                        "Managed enterprise data analytics and reporting by leveraging PostgreSQL, MS SQL Server, and Snowflake."
                    ]
                }
            ],
            "projects": [
                {
                    "title": "AI Agent for Development, Automated Unit Testing and Code Review", #
                    "duration": "6 Days", #
                    "technologies": ["Python", "pytest", "Agentic AI", "Generative AI"], #
                    "description": [
                        "Developed an AI-powered automation workflow to optimize unit testing and code review processes.",
                        "Enhanced engineering productivity by reducing manual review efforts by 80%, accelerating development timelines."
                    ]
                },
                {
                    "title": "RASA-based Conversational Chatbot", #
                    "duration": "2 Months", #
                    "technologies": ["RASA Framework", "Python", "Conversational AI"], #
                    "description": [
                        "Built and enhanced a conversational AI chatbot using the RASA framework to support intelligent workflow automation.",
                        "Integrated analytics tracking to monitor user interactions, measure bot performance, and generate operational insights."
                    ]
                }
            ]
        }