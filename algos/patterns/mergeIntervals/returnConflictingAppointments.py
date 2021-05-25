# Given a list of appointments, find all the conflicting appointments.

# Example:

# Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]
# Output: 
# [4,5] and [3,6] conflict. 
# [3,6] and [5,7] conflict.

 

def can_attend_all_appoitnments(intervals):
    can_attend = []
    intervals.sort(key=lambda x:x[0])
    start = intervals[0][0]
    end = intervals[0][1]
    for i in range(1, len(intervals)):
        interval = intervals[i]

        if interval[0] < end and interval[0] > start:
            print(f"[{start}, {end}], and [{interval[0]}, {interval[1]}] are conflicting.")
        else:
            start = interval[0]
            end = interval[1]
    return

if __name__ == '__main__':
    print(str(can_attend_all_appoitnments([[4,5], [2,3], [3,6], [5,7], [7,8]])))
    # print("Can attend a;; appointments: " + str(can_attend_all_appoitnments([[6,7], [2,4], [8,12]])))
    # print("Can attend a;; appointments: " + str(can_attend_all_appoitnments([[4,5], [2,3], [3,6]])))
