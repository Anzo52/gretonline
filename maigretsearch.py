import asyncio
import logging
from maigret.sites import MaigretSite
from maigret.maigret import maigret as maigret_search
from maigret.result import QueryResult, QueryResultWrapper

# Set up logging for this module
logger = logging.getLogger(__name__)

def format_maigret_results(results: QueryResultWrapper) -> list[dict]:
    """
    Format Maigret results for use in Jinja template.
    
    Args:
        results (QueryResultWrapper): The results from the Maigret search.

    Returns:
        list[dict]: Formatted results as a list of dictionaries.
    """
    formatted_results = []
    for site, result in results.items():
        for query_result in result:
            formatted_result = {
                "site": query_result.site_name,
                "status": query_result.status,
                "url": query_result.site_url_user,
                "details": query_result.context
            }
            formatted_results.append(formatted_result)
    return formatted_results

async def perform_maigret_search(username: str) -> QueryResultWrapper:
    """
    Perform an asynchronous Maigret search.

    Args:
        username (str): Username to search for.

    Returns:
        QueryResultWrapper: The results from the Maigret search.
    """
    # Placeholder information for MaigretSite
    info = {
        'username_claimed': 'claimed_username',
        'username_unclaimed': 'unclaimed_username',
    }

    # Create a MaigretSite object with the provided username and info
    site = MaigretSite(username, info)

    # Perform the search and return results
    return await maigret_search(site, site_
