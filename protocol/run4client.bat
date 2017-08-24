del ../client/ddz_client/protocol/*

cd ../tools/node_modules/
protoc.exe --js_out=library=../../client/ddz_client/protocol/ddzproto,binary:. --proto_path ../../protocol/ ../../protocol/ddzproto.proto
node proto2ts/node_modules/protobufjs/bin/pbjs ../../protocol/ddzproto.proto > ../../client/ddz_client/protocol/ddzproto.json
node proto2ts/command.js --file ../../client/ddz_client/protocol/ddzproto.json --out ../../client/ddz_client/protocol/DDZProto.d.ts

cd ../../client/ddz_client/protocol/
del *.json