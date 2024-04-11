import os
from notion_client import Client

notion = Client(auth="your_integration_token")
database_id = "your_notion_database_id"

def upload_file_to_notion(file_path):
    file_name = os.path.basename(file_path)
    # Implement the logic to create a new page in Notion or upload the file content
    # For example, creating a new page with the file name as the title
    notion.pages.create(parent={"database_id": database_id}, properties={"Name": {"title": [{"text": {"content": file_name}}]}})

# Add your logic to monitor a directory and call upload_file_to_notion for new files
