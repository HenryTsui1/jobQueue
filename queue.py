'''
Name: Henry Tsui
Student ID: 20105575
'''

import time

def new_jobs(job_queue, cmds): #adds jobs to job_queue
    timestamp = time.ctime() #sets date/time stamp
    cmds.append(timestamp) #adds to job
    job_queue.append(cmds) #adds to job_queue array


def respond(job_queue): #removes the first job in queue
    job_queue = job_queue[1:]
    return job_queue


def active_jobs(job_queue): #sees the number of active jobs in job_queue
    avg_priority = []
    for jobs in job_queue:
        avg_priority.append(int(jobs[2])) #appends priority of each jobs into avg_priority array
    avg = sum(avg_priority) #sums up all priority 
    average_p = avg / len(avg_priority) #calculates average of priority
    return average_p


def modify_jobs(job_queue, cmds): #modifies information on the job
    for jobs in job_queue:
        if cmds[1] == jobs[1]: #if job id is equal to one another
            jobs[2] = cmds[2] #modifies job priority
            jobs[3] = cmds[3] #modifies job description


def remove(job_queue, cmds): #removes a specific job in job_queue array
    i = 0
    while i < len(job_queue): #keep track of the len of job_queue
        if cmds[1] != job_queue[i][1]: #traverses the list
            i = i + 1
        elif cmds[1] == job_queue[i][1]: #if the job id matches the job_queue[i] job id, pops the whole list
            job_queue.pop(i)


def statistics(job_queue): #counts how many types of jobs are there in job_queue
    main_count = 0
    clean_count = 0
    carp_count = 0

    list1 = []

    for i in range(len(job_queue)):
        if job_queue[i][3] == "maintenance":
            main_count = main_count + 1 #each time the program spots the string, it adds 1
                   
        elif job_queue[i][3] == 'cleaning':
            clean_count += 1      

        elif job_queue[i][3] == 'carpentry':
            carp_count += 1

    list1.append(main_count)
    list1.append(clean_count)
    list1.append(carp_count)
    return list1
    
