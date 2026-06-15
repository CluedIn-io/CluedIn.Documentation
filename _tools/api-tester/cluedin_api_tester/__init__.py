"""CluedIn REST API smoke-tester.

Acquires an OAuth bearer token via the IdentityServer resource-owner-password
grant (client_id + username + password) and exercises a catalog of REST
endpoints, prioritising the GraphQL-backed surface.

See the package README for usage.
"""

__version__ = "0.1.0"

from .auth import AuthError, TokenResult, get_access_token  # noqa: F401
from .catalog import Endpoint, load_catalog  # noqa: F401
from .tester import ApiTester, TestResult  # noqa: F401
