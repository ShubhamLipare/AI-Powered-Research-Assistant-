import os
from pathlib import Path

folder_list =[
    f"data/",
    f"src/__init__.py",
    f"src/ingestion/__init__.py",
    f"src/ingestion/load_data.py",
    f"src/ingestion/chunk_data.py",
    f"src/retriever/__init__.py",
    f"src/retriever/vectorstore.py",
    f"src/api/__init__.py",
    f"src/api/main.py",
    f"src/agents/__init__.py",
    f"src/agents/researcher.py",
    f"src/agents/summarizer.py",
    f"src/agents/critic.py",
    f"src/logger.py",
    f"src/exception.py",
    f"src/utils.py",
    f"tests/",
    f"ui/__init__.py",
    f"ui/app.py",
    f".github/workflows/ci_cd.yml",
    f"requirements.txt",
    f"src/tasks/__init__.py",
    f"src/tasks/researcher_task.py",
    f"src/tasks/summarizer_task.py",
    f"src/tasks/critic_task.py",
]


for path in folder_list:
    path=Path(path)

    file_dir,filename=os.path.split(path)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)

    if not (os.path.exists(path)) or os.path.getsize(path)==0:
        path.touch()
    else:
        print(f"{path} already exists")

