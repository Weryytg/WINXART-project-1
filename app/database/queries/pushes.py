from sqlalchemy import select

from app.database.session import async_session
from app.database.models import User


async def push_users_from_txt(users: list) -> None:
    async with async_session() as session:
        for user in users:
            if user.startswith("+"):
                session.add(User(phonenumber=user))
            elif user.startswith("@"):
                session.add(User(username=user))
            elif user.startswith("https://"):
                session.add(User(link=user))
                
        await session.commit()