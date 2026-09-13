from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # URLs
    base_url: str = Field(default="https://sauce-demo.myshopify.com/")

    # Browser settings
    browser_type: str = Field(default="chromium")
    headless: bool = Field(default=False)
    timeout: int = Field(default=10_000)
    slow_mo: int = Field(default=0)

    # Pydantic configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

settings = Settings()