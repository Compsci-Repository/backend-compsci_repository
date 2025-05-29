from flask import request

from typing import List

from app.models.App import App
from app.models.File import File

def getfile() -> dict:
  code: int = 200
  try:
    db = App.get_db()

    if db is None:
      code = 500
      raise Exception("Database connection error")


    semester: str = request.args.get('semester')
    subject:  str = request.args.get('subject')
    category: str = request.args.get('category')

    if not semester or not subject or not category:
      code = 400
      missing_data: List[str] = []

      if not semester:
        missing_data.append('semester')

      if not subject:
        missing_data.append('subject')

      if not category:
        missing_data.append('category')

      raise Exception(f'Missing required parameters: {", ".join(missing_data)}')


    if not semester.isdigit():
      code = 400
      raise ValueError("Invalid semester format. It must be numeric.")

    if not all(char.isalnum() or char.isspace() for char in subject):
      code = 400
      raise ValueError("Invalid subject format. It must be alphanumeric.")

    if not category.isalpha():
      code = 400
      raise ValueError("Invalid category format. It must be alphanumeric.")


    try:
      files_request: List[File] = db.session.query(File).filter_by(
        semester=semester, subject=subject, category=category
      ).all()
    except Exception as db_error:
      code = 500
      raise Exception(f"Database query failed: {str(db_error)}")


    return {
      'status_code': code,
      'count': len(files_request),
      'data': [
        file.to_json() for file in files_request
      ],
      'message': 'Files retrieved successfully',
    }

  except ValueError as ve:
    return {
      'status_code': code,
      'message': str(ve),
      'data': None,
    }

  except Exception as e:

    print(f"Error: {str(e)}")

    if code == 200:
      code = 500

    return {
      'status_code': code,
      'message': 'An unexpected error occurred',
      'data': None,
    }
