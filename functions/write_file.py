import os

def write_file(working_directory, file_path, content) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_path.startswith(abs_working_dir):
        return f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory"
    
    if not os.path.exists(abs_path):
        try:
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    try:
        with open(abs_path, "w") as f:
            f.write(content)
        
        return f"Successfully wrote to \"{file_path}\" ({len(content)} characters written)"
    except Exception as e:
        return f"Error: writing to the file: {e}"