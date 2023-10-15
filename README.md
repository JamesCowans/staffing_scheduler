# DC Staff Scheduler

## Project Brief
The brief for this project came from a busy Distribution Centre wanting to look at continous improvement from a staffing perspective. 

The delivery volumes for the week would be known in advance and they also know how many units each department can process in an hour.

The General Merchandise side of the operation had the most complex path, needing to go through inbound processing, decanting, picking and putaway, the beauty side was only processed once.

The idea was to allow a user to enter the weekly volumes for each General Merchandise and Beauty seperatly, 5 days in total Monday - Friday which covered the working week.

The staffing requirements were to complete all work within the day that the delivery arrived.

## Functions

daily_volume_general - This allowed the user to input each days delivery for General Merchandise.
daily_volume_beauty - This allowed the user to input each days delivery for Beauty products.



## Worksheet Information

[Worksheet link](https://docs.google.com/spreadsheets/d/1VbqBGZ6_eDtFS35rRN_9dYAKmh-yTLNb64U_x0tdLK4/edit?usp=sharing)


The Google Docs sheet has 12 tabs:

delivery_volumes_general - This is where the user inputed General Merchandise data will be uploaded to 

delivery_volumes_beauty - This is where the user inputed Beauty delivery data will be uploaded to

There are also 5 tabs for the staffing requirments of each department, on top of this there are an additonal 5 tabs that allow the department managers to input their most up to date hourly productivity targets, these are what the program uses to determine the daily staffing requirments.



## Future Developments

In the future I would like to adapt the program to schedule staff more effectively, currently the work pattern has been set as an 8am start and working for 8 hours, with future development the program should be able to take into account how long each process will need to run before the next process can start. This should feed into a longer working day, scheduling more effectivly to improve the flow of work.

## Bugs and testing

There is a known issue with the error handling, when the program finds an error it is displaying the error message twice before asking the user to re-enter the correct information, other than this it is able to handle incorrect number of variable or incorrect type correctly.







