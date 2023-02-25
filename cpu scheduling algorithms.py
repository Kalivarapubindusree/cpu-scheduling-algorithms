def findWaitingTimeFCFS(processes, n,
					bt, wt):
	wt[0] = 0
	for i in range(1, n ):
		wt[i] = bt[i - 1] + wt[i - 1]

def findTurnAroundTimeFCFS(processes, n,
					bt, wt, tat):

	for i in range(n):
		tat[i] = bt[i] + wt[i]

def findavgTimeFCFS( processes, n, bt):
	wt = [0] * n
	tat = [0] * n
	total_wt = 0
	total_tat = 0
	findWaitingTimeFCFS(processes, n, bt, wt)
	findTurnAroundTimeFCFS(processes, n,
					bt, wt, tat)

	
	
	print( "Processes Burst time " +
				" Waiting time " +
				" Turn around time")

	
	
	for i in range(n):
	
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" " + str(i + 1) + "\t\t" +
					str(bt[i]) + "\t " +
					str(wt[i]) + "\t\t " +
					str(tat[i]))

	print( "Average waiting time = "+
				str(total_wt / n))
	print("Average turn around time = "+
					str(total_tat / n))



	
	
	
	


# Python3 program to implement Shortest Remaining Time First
# Shortest Remaining Time First (SRTF)

# Function to find the waiting time
# for all processes
def findWaitingTimeSJF(processes, n, wt):
	rt = [0] * n

	# Copy the burst time into rt[]
	for i in range(n):
		rt[i] = processes[i][1]
	complete = 0
	t = 0
	minm = 999999999
	short = 0
	check = False

	# Process until all processes gets
	# completed
	while (complete != n):
		
		# Find process with minimum remaining
		# time among the processes that
		# arrives till the current time`
		for j in range(n):
			if ((processes[j][2] <= t) and
				(rt[j] < minm) and rt[j] > 0):
				minm = rt[j]
				short = j
				check = True
		if (check == False):
			t += 1
			continue
			
		# Reduce remaining time by one
		rt[short] -= 1

		# Update minimum
		minm = rt[short]
		if (minm == 0):
			minm = 999999999

		# If a process gets completely
		# executed
		if (rt[short] == 0):

			# Increment complete
			complete += 1
			check = False

			# Find finish time of current
			# process
			fint = t + 1

			# Calculate waiting time
			wt[short] = (fint - proc[short][1] -	
								proc[short][2])

			if (wt[short] < 0):
				wt[short] = 0
		
		# Increment time
		t += 1

# Function to calculate turn around time
def findTurnAroundTimeSJF(processes, n, wt, tat):
	
	# Calculating turnaround time
	for i in range(n):
		tat[i] = processes[i][1] + wt[i]

# Function to calculate average waiting
# and turn-around times.
def findavgTimeSJF(processes, n):
	wt = [0] * n
	tat = [0] * n

	# Function to find waiting time
	# of all processes
	findWaitingTimeSJF(processes, n, wt)

	# Function to find turn around time
	# for all processes
	findTurnAroundTimeSJF(processes, n, wt, tat)

	# Display processes along with all details
	print("Processes Burst Time	 Waiting",
					"Time	 Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", processes[i][0], "\t\t",
				processes[i][1], "\t\t",
				wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = ", total_tat / n)
	
# Driver code sjf



# Python3 program for implementation of
# RR scheduling

# Function to find the waiting time
# for all processes
def findWaitingTimeRR(processes, n, bt,
						wt, quantum):
	rem_bt = [0] * n

	# Copy the burst time into rt[]
	for i in range(n):
		rem_bt[i] = bt[i]
	t = 0 # Current time

	# Keep traversing processes in round
	# robin manner until all of them are
	# not done.
	while(1):
		done = True

		# Traverse all processes one by
		# one repeatedly
		for i in range(n):
			
			# If burst time of a process is greater
			# than 0 then only need to process further
			if (rem_bt[i] > 0) :
				done = False # There is a pending process
				
				if (rem_bt[i] > quantum) :
				
					# Increase the value of t i.e. shows
					# how much time a process has been processed
					t += quantum

					# Decrease the burst_time of current
					# process by quantum
					rem_bt[i] -= quantum
				
				# If burst time is smaller than or equal
				# to quantum. Last cycle for this process
				else:
				
					# Increase the value of t i.e. shows
					# how much time a process has been processed
					t = t + rem_bt[i]

					# Waiting time is current time minus
					# time used by this process
					wt[i] = t - bt[i]

					# As the process gets fully executed
					# make its remaining burst time = 0
					rem_bt[i] = 0
				
		# If all processes are done
		if (done == True):
			break
			
# Function to calculate turn around time
def findTurnAroundTimeRR(processes, n, bt, wt, tat):
	
	# Calculating turnaround time
	for i in range(n):
		tat[i] = bt[i] + wt[i]


# Function to calculate average waiting
# and turn-around times.
def findavgTimeRR(processes, n, bt, quantum):
	wt = [0] * n
	tat = [0] * n

	# Function to find waiting time
	# of all processes
	findWaitingTimeRR(processes, n, bt,
						wt, quantum)

	# Function to find turn around time
	# for all processes
	findTurnAroundTimeRR(processes, n, bt,
								wt, tat)

	# Display processes along with all details
	print("Processes Burst Time	 Waiting",
					"Time Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", i + 1, "\t\t", bt[i],
			"\t\t", wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = %.5f "% (total_tat / n))
	
# Driver code round robin



# Python3 program for implementation of
# Priority Scheduling

# Function to find the waiting time
# for all processes
def findWaitingTimePS(processes, n, wt):
	wt[0] = 0

	# calculating waiting time
	for i in range(1, n):
		wt[i] = processes[i - 1][1] + wt[i - 1]

# Function to calculate turn around time
def findTurnAroundTimePS(processes, n, wt, tat):
	
	# Calculating turnaround time by
	# adding bt[i] + wt[i]
	for i in range(n):
		tat[i] = processes[i][1] + wt[i]

# Function to calculate average waiting
# and turn-around times.
def findavgTimePS(processes, n):
	wt = [0] * n
	tat = [0] * n

	# Function to find waiting time
	# of all processes
	findWaitingTimePS(processes, n, wt)

	# Function to find turn around time
	# for all processes
	findTurnAroundTimePS(processes, n, wt, tat)

	# Display processes along with all details
	print("\nProcesses Burst Time Waiting",
		"Time Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):

		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", processes[i][0], "\t\t",
				processes[i][1], "\t\t",
				wt[i], "\t\t", tat[i])

	print("\nAverage waiting time = %.5f "%(total_wt /n))
	print("Average turn around time = ", total_tat / n)

def priorityScheduling(proc, n):
	
	# Sort processes by priority
	proc = sorted(proc, key = lambda proc:proc[2],
								reverse = True);

	print("Order in which processes gets executed")
	for i in proc:
		print(i[0], end = " ")
	findavgTimePS(proc, n)
	






while(1):
    print("Enter 1 for Priority scheduling, 2 for round robin, 3 for SJF, 4 for FCFS")

    ip = int(input())
    
    if ip==1:
        proc = [[1, 10, 1],
    			[2, 5, 0],
    			[3, 8, 1]]
        n = 3
        print("For Priority Scheduling algorithm: ")

        priorityScheduling(proc, n)
        
    elif ip==2:
        proc = [1, 2, 3]
        n = 3
        burst_time = [10, 5, 8]
        quantum = 2
        print("For Round robin algorithm: ")
        findavgTimeRR(proc, n, burst_time, quantum)
        
    elif ip==3:
        n=4
        proc = [[1, 6, 1], [2, 8, 1],[3, 7, 2], [4, 3, 3]];
        print("For SJF algorithm: ")

        findavgTimeSJF(proc, n)
        
    elif ip==4:
        processes = [ 1, 2, 3]
        n = len(processes)
        burst_time = [10, 5, 8]
        print("For FCFS algorithm: ")

        findavgTimeFCFS(processes, n, burst_time)