from google.cloud import storage

def get_fake_client():
    import requests
    import urllib3
    from google.api_core.client_options import ClientOptions
    from google.auth.credentials import AnonymousCredentials
    from google.cloud import storage
    my_http = requests.Session()
    my_http.verify = False  # disable SSL validation
    urllib3.disable_warnings(
        urllib3.exceptions.InsecureRequestWarning
    )  # disable https warnings for https insecure certs

    client = storage.Client(
        credentials=AnonymousCredentials(),
        project="test",
        _http=my_http,
        client_options=ClientOptions(api_endpoint='https://127.0.0.1:4443'),
    )
    return client

def read_file_from_gcs(bucket_name, blob_name):
    # Create a storage client
    client = get_fake_client()

    # Get the bucket
    bucket = client.get_bucket(bucket_name)

    # Get the blob (file) from the bucket
    blob = bucket.blob(blob_name)

    # Read the content of the blob as text
    content = blob.download_as_text()

    return content

# Usage example
bucket_name = "sample-bucket"
blob_name = "some_file.txt"

file_content = read_file_from_gcs(bucket_name, blob_name)
print(file_content)