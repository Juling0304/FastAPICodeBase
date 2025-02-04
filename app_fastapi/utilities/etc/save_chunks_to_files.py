import os


def save_chunks_to_files(
    full_string: str, file_name: str, chunk_size: int = 2000, folder: str = "chunks"
):

    os.makedirs("storage/" + folder, exist_ok=True)

    for i in range(0, len(full_string), chunk_size):
        chunk = full_string[i : i + chunk_size]
        file_path = os.path.join(
            "storage/" + folder, f"{file_name}_chunk_{i//chunk_size + 1}.txt"
        )
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(chunk)
