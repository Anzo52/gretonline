import asyncio
from maigret.sites import MaigretSite
from maigret.maigret import maigret as maigret_search
from maigret.maigret import extract_ids_from_page
from maigret.maigret import extract_ids_from_results
from maigret.result import QueryResult, QueryStatus
from gretlogger import setup_logger
from maigret.result import QueryResult
from maigret.result import QueryResult

logger = setup_logger(__name__)


def format_maigret_results(results: list[QueryResult]) -> list[dict]:
    """Format Maigret results for use in Jinja template."""
    formatted_results = []
    for result in results:
        formatted_result = {
            "site": result.site_name,
            "status": result.status,
            "url": result.site_url_user,
            "details": result.context
        }
        formatted_results.append(formatted_result)
    return formatted_results


async def perform_maigret_search(username: str) -> list[QueryResult]:
    """Perform Maigret search asynchronously."""
    # Create MaigretSite object
    site = MaigretSite(username)

    return await maigret_search(site)


def perform_maigret_search_sync(username: str) -> list[QueryResult]:
    """Perform Maigret search synchronously."""
    # Create MaigretSite object
    site = MaigretSite(username)

    return asyncio.run(maigret_search(site))


async def perform_maigret_search_with_ids(username: str) -> list[QueryResult]:
    """Perform Maigret search asynchronously with IDs."""
    # Create MaigretSite object
    site = MaigretSite(username)

    # Extract IDs from page
    ids = await extract_ids_from_page(site)

    # Extract IDs from results
    ids = await extract_ids_from_results(site, ids)

    return await maigret_search(site, ids=ids)


def perform_maigret_search_with_ids_sync(username: str) -> list[QueryResult]:
    """Perform Maigret search synchronously with IDs."""
    # Create MaigretSite object
    site = MaigretSite(username)

    # Extract IDs from page
    ids = asyncio.run(extract_ids_from_page(site))

    # Extract IDs from results
    ids = asyncio.run(extract_ids_from_results(site, ids))

    return asyncio.run(maigret_search(site, ids=ids))
