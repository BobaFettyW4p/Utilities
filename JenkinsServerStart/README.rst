I have a personal Jenkins server hosted in an EC2 instance that I use to build my own CI/CD pipelines.
Since it's an EC2 instance, I don't want to leave it running all the time and incur the associated costs.

To this end, I've written two scripts: one to start and one to stop the instance.

the start script will iterate through all of the EC2 instances in the given region and start the one with the given tag.
the stop script will iterate through the EC2 instances in the given region and stop the one with the given tag.