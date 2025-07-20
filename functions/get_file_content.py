import os
from config import MAX_CHARS
    
def get_file_content(working_directory, file_path) -> str:
    path = os.path.abspath(os.path.join(working_directory, file_path))

    if not path.startswith(os.path.abspath(working_directory)):
        return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"
        
    if not os.path.isfile(path):
        return f"Error: File not found or is not a regular file: \"{file_path}\""
    
    try:
        with open(path, "r") as f:
            file_content = f.read(MAX_CHARS)
            if os.path.getsize(path) > MAX_CHARS:
                file_content += f"[... File \"{file_path}\" truncated at {MAX_CHARS} characters]"

        
        return file_content
    except Exception as e:
        return f"Error: {e}"