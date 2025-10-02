import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

account = os.getenv("SNOWFLAKE_ACCOUNT")
user = os.getenv("SNOWFLAKE_USER")
password = os.getenv("SNOWFLAKE_PASSWORD")

if not all([account, user, password]):
    raise ValueError("Missing one or more Snowflake env vars in .env")

# Path to Snowflake config.toml (Windows: %LOCALAPPDATA%\snowflake\config.toml)
config_path = Path.home() / ".snowflake" / "config.toml"
config_path.parent.mkdir(parents=True, exist_ok=True)

config = f"""
[connections.dev]
account = "{account}"
user = "{user}"
password = "{password}"
role = "ACCOUNTADMIN"
warehouse = "COMPUTE_WH"
database = "COURSE_REPO"
schema = "PUBLIC"
"""

config_path.write_text(config)
print(f"✅ Wrote Snowflake config to {config_path}")
