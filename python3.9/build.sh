RUNTIME_IMAGE_NAME="senorcoder/aws-lambda-env:python3.9"
BUILD_IMAGE_NAME="${RUNTIME_IMAGE_NAME}_build"

docker build -t "$RUNTIME_IMAGE_NAME" --build-arg RUNTIME_PACKAGE_URL=https://aws-lambda-runtime.s3.amazonaws.com/fs/python3.9.tgz -f runtime/Dockerfile .
docker push $RUNTIME_IMAGE_NAME
echo "Published image -> ${RUNTIME_IMAGE_NAME}"

docker build -t "${BUILD_IMAGE_NAME}" --build-arg RUNTIME_IMAGE=$RUNTIME_IMAGE_NAME -f build/Dockerfile .
docker push "${BUILD_IMAGE_NAME}"
echo "Published image -> ${BUILD_IMAGE_NAME}"
