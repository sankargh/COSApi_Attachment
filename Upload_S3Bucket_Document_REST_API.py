from com.ibm.tivoli.maximo.cos import COSApi
from java.io import File, FileOutputStream, FileInputStream
from java.net  import URL, HttpURLConnection;
from org.apache.http.entity.mime import MultipartEntityBuilder;

cosApi = COSApi(False)
bucketname = service.getProperty(mxe.cosbucketname)
urlString = filePath.split()
fileName = urlString[-1]

#Create Temporary File in Pod
FILEPATH = "root\maximo\temp\fileName.txt";
uploadFile =  File(FILEPATH);
uploadFile.createNewFile();
fos = FileOutputStream(uploadFile);

## Option - 1 

#Get byteArray from S3 Bucket
docBytes=cosApi.getFile(bucketname,fileName)

# Write the Bytes to File Outputstream
fos.write(docBytes);
print(Successfully+  byte inserted);
# Close the file connections
fos.close();

'''
## Option - 2
# Get Input Stream from s3 bucket
fis=cosApi.streamFile(bucketname,fileName)

byteRead=0
#Read byte by byte
while ((byteRead = fis.read()) != -1)
    #Write byte by byte
    fos.write(byteRead)
'''

#Upload File Outputstream to REST API
#(This is an Example; Please modify depending on authentication, content type)

builder = MultipartEntityBuilder.create();
builder.addBinaryBody(file, uploadFile);
entity = builder.build();

url = URL("https:\\clientdomainhostname\restapi\fileupload");
conn = url.openConnection();
conn.setDoOutput(True);
conn.setRequestMethod(POST);
conn.addRequestProperty(Content-Length, str(entity.getContentLength()));
fos = conn.getOutputStream();
entity.writeTo(fos);
fos.close();
conn.connect();
conn.getInputStream().close();
statusCode = conn.getResponseCode();
		
#Delete the Temporary File After Upload

uploadFile.delete()

