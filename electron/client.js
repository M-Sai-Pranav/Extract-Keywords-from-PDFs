const grpc = require("@grpc/grpc-js");
var protoLoader = require("@grpc/proto-loader");
const { app } = require('electron')
const path = require('path')
const PROTO_PATH =  path.join(app.getAppPath(), "/electron/protoFiles/unary.proto")

const options = {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true,
};

var packageDefinition = protoLoader.loadSync(PROTO_PATH, options);


const unaryService = grpc.loadPackageDefinition(packageDefinition).Unary;
console.log(unaryService)
const unaryClient = new unaryService(
  "localhost:50051",
  grpc.credentials.createInsecure()
);
module.exports = {unaryClient}