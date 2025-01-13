//--web true
//--param minio_key $TESTUSER_SECRET_MINIO
function main(args) {
    return {
        statusCode: 200,
        body: {
            authenticated: true,
            minio_key: args.minio_key,
        }
    }
}