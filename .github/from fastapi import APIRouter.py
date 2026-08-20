from fastapi import APIRouter
from models.route_request import RouteRequest
from models.route import Route
from core.routing_engine import compute_route

router = APIRouter()

@router.post("/routes", response_model=Route)
async def create_route(request: RouteRequest):
    route = await compute_route(request)
    return route
