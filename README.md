# locust-demo

This is a demo project that shows how to get started using Locust as a performance testing tool.

This project will show steps on how to run tests vs apis and web pages. There is boilerplate code here as well that 
shows how to customize this for your own tests.

I have added dependencies for this project in the requirements.txt file

Do check the official page of [Locust](https://www.locust.io) for further details

To run this from your local machine (once you have locust installed on your machine or preferably virtual env)

The command below states that  

--locustfile it should pick perf_test_workload.py as the runner file,
--no-web it should not spawn the web interface to run the test (recommended),
-c is the number of total locusts (users) to spawn,
-r is the hatch rate (#users to add per 2 second cycle),
-t is the duration run the test for. s stands for seconds, 

```$> locust --locustfile ./perf_test_workload.py --no-web -c 1 -r 1 -t 10s```

If all is well you should see the following below:

```
2020-04-29 14:52:38,305] x/INFO/locust.runners: Hatching and swarming 1 clients at the rate 1 clients/s...
[2020-04-29 14:52:39,309] x/INFO/locust.main: Run time limit set to 10 seconds
[2020-04-29 14:52:39,310] x/INFO/locust.main: Starting Locust 0.13.5
[2020-04-29 14:52:39,311] x/INFO/locust.runners: All locusts hatched: LocustClientDemo: 1

<snip>

 Name                                                          # reqs      # fails     Avg     Min     Max  |  Median   req/s failures/s
--------------------------------------------------------------------------------------------------------------------------------------------
 GET Find all pasta recipes                                         2     0(0.00%)     263     260     266  |     260    0.25    0.00
 GET Find all recipes with onions in them                           3     0(0.00%)     428     229     755  |     300    0.25    0.00
--------------------------------------------------------------------------------------------------------------------------------------------
 Aggregated                                                         5     0(0.00%)     362     229     755  |     270    0.50    0.00

[2020-04-29 14:52:49,310] x/INFO/locust.main: Time limit reached. Stopping Locust.
[2020-04-29 14:52:49,311] x/INFO/locust.main: Shutting down (exit code 0), bye.
[2020-04-29 14:52:49,312] x/INFO/locust.main: Cleaning up runner...
[2020-04-29 14:52:49,312] x/INFO/locust.main: Running teardowns...
 Name                                                          # reqs      # fails     Avg     Min     Max  |  Median   req/s failures/s
--------------------------------------------------------------------------------------------------------------------------------------------
 GET Find all pasta recipes                                         2     0(0.00%)     263     260     266  |     260    0.20    0.00
 GET Find all recipes with onions in them                           4     0(0.00%)     429     229     755  |     300    0.41    0.00
--------------------------------------------------------------------------------------------------------------------------------------------
 Aggregated                                                         6     0(0.00%)     374     229     755  |     270    0.61    0.00

Percentage of the requests completed within given times
 Type                 Name                                                           # reqs    50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100%
------------------------------------------------------------------------------------------------------------------------------------------------------
 GET                  Find all pasta recipes                                              2    270    270    270    270    270    270    270    270    270    270    270
 GET                  Find all recipes with onions in them                                4    430    430    760    760    760    760    760    760    760    760    760
------------------------------------------------------------------------------------------------------------------------------------------------------
 None                 Aggregated                                                          6    300    300    430    430    760    760    760    760    760    760    760

```

The log above can be exported to a csv file as well using the --csv <file_prefix> option while running the test

The results out of the box provide you with the # of requests made, the average, min, max, median response times along 
with the throughput for a particular perf activity