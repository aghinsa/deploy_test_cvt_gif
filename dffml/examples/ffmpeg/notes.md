dffml service dev export -config yaml ffmpeg.dataflow:DATAFLOW > deploy/df/ffmpeg.yaml
dffml service http server -insecure -mc-config deploy -port 8080
curl -v --request POST --data-binary @input.mp4 http://localhost:8080/ffmpeg -o out.gif

bytes:post_input.output_file