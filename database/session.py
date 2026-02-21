from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from config.settings import settings

# Construct the Async URL
# Assumes postgres:// in the original URL which needs to be postgresql+asyncpg://
db_url = settings.DATABASE_URL
if db_url.startswith("postgresql://"):
    db_url = db_url.replace("postgresql://", "postgresql+asyncpg://", 1)
elif db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql+asyncpg://", 1)

# Remove the query parameters that asyncpg doesn't understand (like sslmode, channel_binding)
if "?" in db_url:
    db_url = db_url.split("?")[0]

# Neon needs some SSL mode handling in some cases
engine = create_async_engine(
    db_url,
    echo=False,
    future=True,
    connect_args={"ssl": "require"}
)

async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)

async def get_db():
    async with async_session_maker() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
