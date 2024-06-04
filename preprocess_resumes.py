import os

def load_resumes(folder_path):
    resumes = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r') as f:
                resumes.append(f.read())
    return resumes

resumes = load_resumes('path_to_resumes_folder')
