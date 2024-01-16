# Load Testing with k6

This repository contains examples for using the k6 tool to conduct load testing for your web application.

## Repository Contents
This repository contains the following files:

#### Collection4LoadTest.postman_collection.json: 
This file is a Postman collection that includes only GET methods requests. It was created using Postman and includes valid requests for load testing purposes.

#### load-test.js: 
This file is generated using the command:

```bash
postman-to-k6 Collection4LoadTest.postman_collection.json > load-test.js
```

It serves as a script for conducting load testing using the k6 utility. The generated JavaScript file can be utilized for load testing scenarios, providing a convenient way to simulate various API requests and assess system performance under different conditions.

## Installing k6

Start by installing k6 on your machine:

```bash
npm install -g k6
```
Note: [More about installing K6](https://k6.io/open-source/,"https://k6.io/open-source/")


## Running Tests
Simple test with 1 virtual user for 1 minute
```bash
k6 run --duration 1m --vus 1 path/to/test-script.js
```
Test with 10 virtual users for 5 minutes
```bash
k6 run --duration 5m --vus 10 path/to/test-script.js
```
Running a test with custom parameters
```bash
k6 run --duration 10s --vus 5 --iterations 100 path/to/test-script.js
```

## Interpreting Results
During the test execution, k6 outputs various performance statistics. Sample output:

```bash
     data_received..................: 56 MB  938 kB/s
     data_sent......................: 26 MB  429 kB/s
     http_req_blocked...............: avg=1.89µs   min=0s     med=0s      max=9.54ms   p(90)=0s     p(95)=0s
     http_req_connecting............: avg=0s       min=0s     med=0s      max=0s       p(90)=0s     p(95)=0s
     http_req_duration..............: avg=1.04ms   min=0s     med=999.6µs max=640.25ms p(90)=1.06ms p(95)=1.16ms
     http_req_failed................: 40.00% ✓ 40656       ✗ 60984
     http_req_receiving.............: avg=33.1µs   min=0s     med=0s      max=61.69ms  p(90)=0s     p(95)=44.8µs
     http_req_sending...............: avg=14.35µs  min=0s     med=0s      max=1.47ms   p(90)=0s     p(95)=0s
     http_req_tls_handshaking.......: avg=0s       min=0s     med=0s      max=0s       p(90)=0s     p(95)=0s
     http_req_waiting...............: avg=997.91µs min=0s     med=998.4µs max=639.25ms p(90)=1.06ms p(95)=1.11ms
     http_reqs......................: 101640 1693.876948/s
     iteration_duration.............: avg=5.89ms   min=2.99ms med=4.74ms  max=657.19ms p(90)=6ms    p(95)=7ms
     iterations.....................: 20328  338.77539/s
     vus............................: 2      min=2         max=2
     vus_max........................: 2      min=2         max=2
```	 

Key parameters for analysis:

http_req_duration: Average time for HTTP requests.
http_req_failed: Percentage of failed HTTP requests.
http_reqs: Total number of executed HTTP requests.
vus: Current number of virtual users.
vus_max: Maximum number of virtual users.