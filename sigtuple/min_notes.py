#code
problem = '''John's wallet has one drawback. His wallet can contain no more than M notes or coins.
             So from his total salary , his boss pays him his max salary by the M notes possible.
             Tell John how much money will he have to lose.


             Input: 3
                    1712 4
                    1023 2
                    2341 3
             Output:
                    12
                    3
                    241
          '''

notes  = [1000, 500, 100, 50, 20, 10, 5, 2, 1]


def get_max_note(salary):
    for note in notes:
        if salary - note >= 0:
            return note     #  assuming notes is sorted, return first largest note
    return 0    #  No note can be drawn. remaining_salary cannot be further reduced
            
    
    
def get_cost(remaining_salary, num_notes):
    # loose no money, entire salary covered with num_notes
    if salary == 0:
        return 0
    
    # cannot keep any more notes, John has to loose remaining_salary
    if num_notes == 0:
        return remaining_salary

    # get_max_note that John can keep without exceeding his salary. Number of notes that John can hold reduces by one
    return get_cost(remaining_salary - get_max_note(salary), num_notes - 1)
    

T = int(input())

for i in range(T):
    salary, num_notes = map(int, raw_input().strip().split())
    print get_cost(salary,num_notes)
    
    
        
    
    