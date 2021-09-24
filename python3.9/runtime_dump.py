from __future__ import print_function

import os
import sys
import subprocess
import json
import boto3
import tarfile
from boto3.s3.transfer import S3Transfer

TRANSFER = S3Transfer(boto3.client('s3'))
BUCKET_NAME = 'aws-lambda-runtime'

def lambda_handler(event, context):
    if 'cmd' in event:
        return print(subprocess.check_output(['sh', '-c', event['cmd']]).decode('utf-8'))

    filename = 'python3.9.tgz'

    with tarfile.open(f"/tmp/{filename}", "w:gz") as tar:
        for file in ['/var/runtime', '/var/lang', '/var/rapid']:
            tar.add(file)

    print('Zipping done! Uploading...')

    TRANSFER.upload_file(f'/tmp/{filename}', BUCKET_NAME,
                         f'fs/{filename}', extra_args={'ACL': 'public-read'})

    print('Uploading done!')

    info = {'sys.executable': sys.executable,
            'sys.argv': sys.argv,
            'sys.path': sys.path,
            'os.getcwd': os.getcwd(),
            '__file__': __file__,
            'os.environ': {k: str(v) for k, v in os.environ.items()},
            'context': {k: str(v) for k, v in context.__dict__.items()}
            }

    print(json.dumps(info, indent=2))

    return info
