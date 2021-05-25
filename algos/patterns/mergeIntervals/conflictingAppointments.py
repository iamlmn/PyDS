# Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

# Example 1:

# Appointments: [[1,4], [2,5], [7,9]]
# Output: false
# Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.
# Example 2:

# Appointments: [[6,7], [2,4], [8,12]] -> [[2,4], [6,7], [8, 12]]
# Output: true
# Explanation: None of the appointments overlap, therefore a person can attend all of them.
# Example 3:

# Appointments: [[4,5], [2,3], [3,6]]
# Output: false
# Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
 

def can_attend_all_appoitnments(intervals):
    can_attend = []
    intervals.sort(key=lambda x:x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        interval = intervals[i]

        if interval[0] < end and interval[0] > start:
            return False
        else:
            start = interval[0]
            end = interval[1]
    return True

if __name__ == '__main__':
    print("Can attend a;; appointments: " + str(can_attend_all_appoitnments([[1,4], [2,5], [7,9]])))
    print("Can attend a;; appointments: " + str(can_attend_all_appoitnments([[6,7], [2,4], [8,12]])))
    print("Can attend a;; appointments: " + str(can_attend_all_appoitnments([[4,5], [2,3], [3,6]])))
