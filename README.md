ONERAGTIME_assignment_sample

The following interpretations can be drawn from the reading of the problem. 
each investor has one or more investments.
Bills are calculated on the basis of these investments. 
The type of bill generated is independent of the investments. 
In addition, more than one type of bill can be generated for an investor.
Each invoice groups one or a series of bills.

Are necessary 4 models to represent the investors, the investments, the bills and the invoices.

The solution develops the ENDPOINTS corresponding to the REST operations for investments and bills, the query that retrieves the bills per investor, the generation of the 3 types of bills: Membership, UpfrontFees and YearlyFees, and the query to check the status for a particular invoice.

A script (assessment/cashcall/management/commands/initscript.py) is incorporated for the initial creation of some records in the database (investors, investments and invoice) to test the generation of the different bills.

In the code review it is possible to iterate to refactor the code and use class based view.
Another iteration incorporate unit test code to allow CI/CD configuration when committing the code and generate the docker image of the service and deploy to the infrastructure.
Finally, attach documentation on ENDPOINTS and parameters.