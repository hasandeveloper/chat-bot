
def process_policy(file_name: str, s3_url: str):
    print(f"Ingesting file: {file_name}")

    # Example: return metadata
    return {
        "file_name": file_name,
        "file_path": s3_url,
        "status": "ingested"
    }