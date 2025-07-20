import os

def get_files_info(working_directory, directory=".") -> str:
    try:
        path = os.path.abspath(os.path.join(working_directory, directory))

        if not path.startswith(os.path.abspath(working_directory)):
            return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
        
        if not os.path.isdir(path):
            return f"Error: \"{directory}\" is not a directory"
        
        contents = os.listdir(path)

        file_info = ""
        for content in contents:
            content_path = os.path.join(path, content)
            is_dir = os.path.isdir(content_path)
            file_size = os.path.getsize(content_path)
            file_info += f" - {content}: file_size={file_size} bytes, is_dir={is_dir}\n"
        return file_info
    
    except Exception as e:
        return f"Error: {e}"
