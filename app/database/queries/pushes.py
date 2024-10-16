from sqlalchemy import select

from app.database.session import async_session
from app.database.models import Link


async def push_users_from_txt(users: list) -> None:
    async with async_session() as session:
        for user in users:
                if user.startswith("+") and (not await session.scalar(select(Link)
                                                                      .where(Link.phonenumber == user))):
                    session.add(Link(phonenumber=user))
                elif user.startswith("@") and (not await session.scalar(select(Link)
                                                                        .where(Link.username == user))):
                    session.add(Link(username=user))
                elif user.startswith("https://") and (not await session.scalar(select(Link)
                                                                               .where(Link.link == user))):
                    session.add(Link(link=user))
                
        await session.commit()