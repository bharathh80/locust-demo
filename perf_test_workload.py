"""
perf_test_workload.py

This file is meant to be boilerplate code that will showcase how to get started
with a perf test for APIs and UIs

This python file is the main driver that will run the load test. This is
equivalent to the locustfile.py in the official documentation on
https://locust.io

"""

from locust import HttpLocust, TaskSet, task, between

"""
Import statements explanation

HttpLocust
-----------
There are 2 primary locust clients that can be invoked. The default is
HTTPLocust. The other is the lite version of the client (FastHttpLocust)
Use this sparingly.

The default client can perform all the standard HTTP operations. It handles
the standard components of a HTTP request and response such as headers,
cookies, etc. HTTPLocust creates instances of HTTPSession to create and handle
requests and responses

TaskSet
--------
Simply put, this class defines the performance workload. There are methods 
such as on_start, on_stop etc where setup and teardown methods can be specified

task
-----
Tasks are functions annotated by the @task function that perform user actions/tests

Tasks can be run in parallel or sequentially. Furthermore, it is possible to specify
what ratio of tasks need to run. Multiple tasks can comprise of one action as well

For example: Let's say in order to validate that user signup is to be tested we need to:
1. Load the login landing page
2. Go to the sign up page and fill out the register new user form
3. Return the login landing page and enter the credentials

All the above tasks can be run sequentially within a task method with each of the above
actions in their own method but called within a master task method 

between
--------
between is a keyword used to specify the waiting period for HTTP responses. This is 
optional - but it is good to override this

"""

class ApiPerfWorkload(TaskSet):
    """ This class defines the workload for the API tests """

    def on_start(self):
        """ Define any setup here """
        pass

    def on_stop(self):
        """ Define any teardown steps here. Usually goes at the bottom but keeping
            it here for visibility """
        pass

    @task(1)
    def get_pasta_recipes(self):
        # Create a GET Request
        response = self.client.get(
            "/api/?q=pasta",
            name="Find all pasta recipes"
        )
        # I can assert using the builtin assert library or I can do
        if response.status_code != 200:
            print(response.text)
            import sys
            sys.exit(1)

        # Else Do something with the response object


    @task(2)     # Run this task twice as much as the base 1
    def get_recipes_with_ingredients(self):
        # Create a GET Request
        response = self.client.get(
            "/api/?i=onion",
            name="Find all recipes with onions in them"
        )
        # I can assert using the builtin assert library or I can do
        if response.status_code != 200:
            print(response.text)
            import sys
            sys.exit(1)

        # Else Do something with the response object


class LocustClientDemo(HttpLocust):
    """ This class defines the perf test settings """

    # To run from your local machine uncomment the lines below
    # These ensure that your machine can perform enough i/o operations
    import resource
    resource.setrlimit(resource.RLIMIT_NOFILE, (10240, 9223372036854775807))

    # Test settings
    wait_time = between(0.5, 3)
    host = "http://www.recipepuppy.com" # It is good to set your host separately from the
                                        # from the rest of the URL so that in case the env
                                        # changes but the rest is the same it is easy to
                                        # maintain the code

    task_set = ApiPerfWorkload          # Call the workload (TaskSet class) to run here



