from ingest.policies import process_policy

def ingest_file(file_name: str, s3_url: str):
    # You can add preprocessing / validation here

    result = process_policy(file_name, s3_url)

    return result