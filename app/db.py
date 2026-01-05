from __future__ import annotations

import os
from typing import Optional
from urllib.parse import quote_plus

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

load_dotenv()

_engine: Optional[Engine] = None


def build_connection_url() -> str:
    host = os.getenv("MSSQL_HOST")
    port = os.getenv("MSSQL_PORT", "1433")
    db = os.getenv("MSSQL_DB")
    user = os.getenv("MSSQL_USER")
    pwd = os.getenv("MSSQL_PASSWORD")

    driver = os.getenv("MSSQL_DRIVER", "ODBC Driver 18 for SQL Server")
    encrypt = os.getenv("MSSQL_ENCRYPT", "yes")  # Driver 18 için genelde yes
    trust = os.getenv("MSSQL_TRUST_CERT", "yes")
    timeout = os.getenv("MSSQL_CONN_TIMEOUT", "30")

    if not all([host, db, user, pwd]):
        raise RuntimeError("Missing MSSQL env vars")

    # MSSQL'de port için en sağlam format: SERVER=host,port  (virgül!)
    server = f"{host},{port}" if port else host

    odbc_str = (
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={db};"
        f"UID={user};"
        f"PWD={pwd};"
        f"Encrypt={encrypt};"
        f"TrustServerCertificate={trust};"
        f"Connection Timeout={timeout};"
    )

    return f"mssql+pyodbc:///?odbc_connect={quote_plus(odbc_str)}"


def get_engine() -> Engine:
    global _engine
    if _engine is None:
        _engine = create_engine(
            build_connection_url(),
            pool_pre_ping=True,
            future=True,
            # Debug için açabilirsin:
            # echo=True,
        )
    return _engine