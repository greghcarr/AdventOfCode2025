def read_file(file_path: str) -> list[str]:
    with open(file_path) as f:
        return f.read().splitlines()