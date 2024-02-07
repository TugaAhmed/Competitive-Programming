# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    all_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        all_students.append([name , score])
    
    # sort students based on their scores
    sorted_students = sorted(all_students, key=lambda x: x[1])
    second_lowest_students = []
    second_lowest_score = -1
    
    for student in sorted_students[1:] : 
        # in case multiple students have highest score
        if second_lowest_score == -1 and student[1] != sorted_students[0][1] :
            second_lowest_score = student[1]
        
        if second_lowest_score != -1 and student[1] == second_lowest_score :
            second_lowest_students.append(student[0])
            
    for name in sorted(second_lowest_students):
        print(name)  
