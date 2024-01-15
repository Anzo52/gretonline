from .adapter import Service
import aiohttp
from typing import Mapping

class Site:
    def __init__(self, name, check=None):
        self.name = name
        self.check = check

def from_func_list(func_list) -> dict[str, Site]:
    return {f.__name__: Site(f.__name__, check=f) for f in func_list}

CHECKERS = []  # Define the CHECKERS variable

class MailcatService(Service):
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.sites: Mapping[str, Site] = from_func_list(CHECKERS)

    async def check(self, site, username):
        check_result = await site.check(username, self.session)

        result = {
            'status': check_result.get('status', 'found') if check_result else None
        }
        result |= (check_result or {})

        return result
