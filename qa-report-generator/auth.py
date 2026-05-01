# auth.py - Simulated Authentication Service

from dataclasses import dataclass
from typing import Optional

@dataclass
class Token:
    """Represents a simulated authentication token."""
    token: str
    expiration: str

@dataclass
class UserSession:
    """Represents a user session in the local authentication service."""
    user_id: str
    role: str
    permissions: list

class LocalAuthService:
    """
    Simulated Local Authentication Service for the QA Testing Lab.
    
    This service simulates an authentication backend that handles user login,
    token generation, and session management for local agents. It is designed
    to run entirely within the local environment, without relying on external
    cloud providers.
    """
    
    def __init__(self):
        self.sessions: dict[str, UserSession] = {}
        self.tokens: dict[str, Token] = {}
        self.default_user = UserSession(
            user_id="qa-analyst",
            role="qa_analyst",
            permissions=["read_results", "summarize_failures", "generate_reports"]
        )
        self.default_token = Token(token="local-simulated-token-xyz", expiration="never")
    
    def authenticate(self, username: str, password: str) -> Optional[Token]:
        """
        Simulates a user login attempt and returns a token if successful.
        
        Args:
            username: The user's login username.
            password: The user's login password.
            
        Returns:
            A Token object on successful login, None otherwise.
        """
        # Simulate simple authentication logic
        # In a real implementation, this would query a local database or LDAP
        if username == "qa-analyst" and password == "local-secret":
            print(f"✅ User '{username}' authenticated successfully.")
            print(f"📋 Role: {self.default_user.role}")
            print(f"🔑 Token: {self.default_token.token}")
            return self.default_token
        else:
            print(f"❌ Authentication failed for user '{username}'.")
            return None
    
    def create_token(self) -> Token:
        """
        Generates a new simulated authentication token.
        
        Returns:
            A new Token object with a generated token string.
        """
        new_token = Token(token="local-simulated-token-xyz", expiration="never")
        self.tokens[new_token.token] = new_token
        return new_token
    
    def revoke_token(self, token: str) -> bool:
        """
        Revokes (invalidates) an existing token.
        
        Args:
            token: The token to revoke.
            
        Returns:
            True if the token was revoked, False otherwise.
        """
        if token in self.tokens:
            del self.tokens[token]
            print(f"Token revoked: {token}")
            return True
        return False

# Global authentication service instance
local_auth_service = LocalAuthService()
