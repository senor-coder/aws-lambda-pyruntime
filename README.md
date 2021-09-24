# aws-lambda-pyruntime

Docker images for AWS lambda runtime for python3.9. 

## How to build the Lambda runtime?

* Upload and execute runtime_dump in the respective lambda environment. 
It will package the runtime binaries and upload it to the declared S3 bucket.
* Run the build.sh file to publish the docker images (Both runtime and build env images)

## Available public docker images

### Python 3.9
```
Runtime: senorcoder/aws-lambda-env:python3.9
Build  : senorcoder/aws-lambda-env:python3.9_build
```

## Credits
Reference: https://github.com/lambci/docker-lambda



