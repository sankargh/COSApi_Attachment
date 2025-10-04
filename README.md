Retrieve file from S3 Bucket:
- Retrieving a file from doclinks is straightforward. We can pass the doclink URL to ‘File’ object as shown below.

	file=File("docklink-filepath")

However, if the attachments are using an S3 bucket, then we cannot directly fetch ‘File’ object from URL. 
- Few additional steps are required to convert as file before sending or uploading to an API 
Here are the steps:
- Get the byte array of attachment from S3 bucket
- Create a temporary file in server or pod
- Create ‘File-output stream’ of the temporary file
- Write the byte array into the ‘File-output stream’.
- Upload the ‘File-output stream’ to REST API to send as file attachment.
- Delete the temporary file
