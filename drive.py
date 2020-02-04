#Name: Henry Tsui
#Student ID: 20105575

import time1
import queue

# average_p = 0

file = open("MaintenanceScheduler.txt", "r") #opens and reads MaintenanceScheduler.txt
lines = file.readlines() #reads each line

schedule = [] #adds each txt file into schedule array
for l in lines:
    schedule.append(l.rstrip('\n').split()) #removes any unwanted strings in the list


def main():  #main function where it calls on other modules to run their functionality
    job_queue = [] #where the 'jobs' are added
    for cmds in schedule: #looks through each array in schedule array
        if cmds[0] == "received":  #received command/adding new job
            queue.new_jobs(job_queue, cmds)
            print("Adding job:",job_queue[-1][1],"to the queue with timestamp",job_queue[-1][-1],"The priority of the job is",job_queue[-1][2],"The job type is",job_queue[-1][3])


        elif cmds[0] == "remove": #removes a job based on the job id
            queue.remove(job_queue, cmds)


        elif cmds[0] == "respond": #calculates how long has the job been in the job_queue, then removes the job in the queue
            timediff = time1.calctime(job_queue)
            print("Completed job",job_queue[0][1],"in",round(timediff, 2),"seconds")
            job_queue = queue.respond(job_queue)

            
        elif cmds[0] == "active" and cmds[1] == "jobs": #checks if there are jobs in the job_queue array
            if job_queue == []: #if job_queue array is empty, prints there are no jobs
                print("No Jobs Available")

            else:   
                calculate_average = queue.active_jobs(job_queue) #prints the total number of jobs, and also rounds up the priority
                total_jobs = len(job_queue)
                print("Total Number of jobs:",total_jobs,"Average Priority:", round(calculate_average)) 


        elif cmds[0] == "modify": #modifies job priority
            queue.modify_jobs(job_queue, cmds)

                     
        elif cmds[0] == "details":  #prints out the job details based on the job id
            for jobs in job_queue:
                if cmds[1] == jobs[1]: #cmds[1] is job id, if it matches the job id in job_queue array, it prints out the details
                    print("Job ID:",jobs[1],"Priorty:",jobs[2],"Job Type:",jobs[3])


        elif cmds[0] == "statistics": #counts how many specific jobs are there
            pending = queue.statistics(job_queue)
            print("Maintenance:",pending[0],"jobs pending") #prints the number of jobs 
            print("Cleaning:",pending[1],"jobs pending")
            print("Carpentry:",pending[2],"jobs pending")


        elif cmds[0] == "next" and cmds[1] == "job": #prints the first item of job_queue, as the 'next job' in queue
            if job_queue == []: #if array is empty, prints "no jobs remaining"
                print("No jobs remaining")
            else:
                print("Next job is",job_queue[0][1],"Job priority is",job_queue[0][2],"Job type is",job_queue[0][3]) #prints out details of the next job in the queue


        elif cmds[0] == "sleep": #when it sees "sleep", the program pauses for the time specified
            time1.sleep(cmds)


if __name__ == '__main__':

    main()
