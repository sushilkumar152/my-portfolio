from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers import portfolio_controller  # Import your new controller layer

app = FastAPI(
    title="Sushil Kumar - Enterprise Portfolio API",
    description="Production-ready backend layered architecture for professional portfolio application.",
    version="1.0.0"
)

# Configure strict CORS policies allowing communication from your Angular local instance
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Controller Endpoints
app.include_router(portfolio_controller.router)

@app.get("/health", tags=["Health Check"])
async def health_check():
    """Simple system health monitoring verification endpoint."""
    return {"status": "healthy", "service": "portfolio-api-engine"}