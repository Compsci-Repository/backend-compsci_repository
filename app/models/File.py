from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, TIMESTAMP, ARRAY, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class FileCategory(enum.Enum):
    exam, activity, video, book = 'exam', 'activity', 'video', 'book'

class File(Base):
    __tablename__ = 'files'

    id          = Column(Integer, primary_key=True, autoincrement=True)
    url         = Column(Text, nullable=False, unique=True)
    title       = Column(Text, nullable=False)
    author      = Column(Text, nullable=True)
    private     = Column(Boolean, nullable=False, default=False)
    usuario_id  = Column(String, ForeignKey('users.student_id'), nullable=False)
    file_type   = Column(Text, nullable=True)
    category    = Column(Enum(FileCategory), nullable=False)
    semester    = Column(Integer, nullable=False)
    subject     = Column(Text, nullable=False)
    tags        = Column(ARRAY(Text), nullable=True)
    created_at  = Column(TIMESTAMP, nullable=False, default=datetime.now())

    def to_json(self) -> dict:
        return {
            "id": self.id,
            "url": self.url,
            "title": self.title,
            "author": self.author,
            "private": self.private,
            "usuario_id": self.usuario_id,
            "file_type": self.file_type,
            "category": self.category.value,
            "semester": self.semester,
            "subject": self.subject,
            "tags": self.tags,
            "created_at": str(self.created_at)
        }