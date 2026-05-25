from fastapi import APIRouter, Depends, HTTPException, status
from app.services.portfolio_service import PortfolioService
from app.models.schemas import ProfileDataResponse, AiAgentQueryRequest, AiAgentQueryResponse

# Define routing isolation for portfolio operations
router = APIRouter(prefix="/api/v1/portfolio", tags=["Portfolio Endpoints"])

# Dependency Injection helper for cleanly spinning up our service layer instances
def get_portfolio_service() -> PortfolioService:
    return PortfolioService()

@router.get("/profile", response_model=ProfileDataResponse, status_code=status.HTTP_200_OK)
def get_portfolio_profile(service: PortfolioService = Depends(get_portfolio_service)):
    """API entry point to pull down full professional profile data[cite: 1]."""
    try:
        return service.get_complete_profile()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.post("/agent/query", response_model=AiAgentQueryResponse, status_code=status.HTTP_200_OK)
async def query_portfolio_agent(
    request: AiAgentQueryRequest, 
    service: PortfolioService = Depends(get_portfolio_service)
):
    """API entry point targeting the interactive portfolio agent engine."""
    try:
        return await service.orchestrate_ai_agent(request.query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent Execution Failure: {str(e)}")