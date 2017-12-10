#monsijb
def check_single(x,y,result,i):
    """
    Function to check if an answer is correct or not
    """
    
    if x ==y:
        result[i] = True
    else:
        result[i] = False



def check_answers(my_answers,answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    Invloves three steps: Calls check_single,counts no.of correct/incorrect answers,
    and outputs the result string.
    """
    results= [None, None, None, None, None]
    
    
    for i in range(len(my_answers)):
        check_single(my_answers[i],answers[i],results,i)
   
    count_correct = 0
    count_incorrect = 0
    for result in results:
        if result == True:
            count_correct += 1
        if result != True:
            count_incorrect += 1
    if count_correct/5 > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif count_incorrect/5 >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."
        
my_answer = [0, 1, 1, 1, 1]
correct_answer = [1, 1, 1, 1, 0]
print(check_answers(my_answer,correct_answer))
