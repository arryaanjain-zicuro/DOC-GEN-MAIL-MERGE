def save_uploaded_file(file, upload_folder):
    import os
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)
    return file_path