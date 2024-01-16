import asyncio
from maigret.sites import MaigretSite
from maigret.maigret import maigret as maigret_search
from maigret.result import QueryResult
import logging

# Set up logging for this module
logger = logging.getLogger(__name__)

def format_maigret_results(results: list[QueryResult]) -> list[dict]:
    """
    Format Maigret results for use in Jinja template.
    
    Args:
        results (list[QueryResult]): A list of QueryResult objects from Maigret search.

    Returns:
        list[dict]: Formatted results as a list of dictionaries.
    """
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
    """
    Perform an asynchronous Maigret search.

    Args:
        username (str): Username to search for.

    Returns:
        list[QueryResult]: The results from the Maigret search.
    """
    # Placeholder information for MaigretSite
    info = {
        'username_claimed': 'claimed_username',
        'username_unclaimed': 'unclaimed_username',
    }

    # Create a MaigretSite object with the provided username and info
    site = MaigretSite(username, info)

    # Perform the search and return results
    return await maigret_search(site)

def perform_maigret_search_sync(username: str) -> list[QueryResult]:
    """
    Perform a synchronous Maigret search.

    Args:
        username (str): Username to search for.

    Returns:
        list[QueryResult]: The results from the Maigret search.
    """
    return asyncio.run(perform_maigret_search(username))

