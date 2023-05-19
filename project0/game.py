import numpy as np

observations_num = 1000
min_number = 1
max_number = 100

def random_predict(number: int = 1) -> int:
    """Predict a number

    Args:
        number (int, optional): Made up number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    
    count = 0
    left_boundary = min_number
    right_boundary = max_number

    while True:
        count += 1
        pivot_number = (left_boundary + right_boundary) // 2
        
        if pivot_number > number:
            right_boundary = pivot_number - 1
        elif pivot_number < number:
            left_boundary = pivot_number + 1
        else:
            break
        
    return(count)


def score_game(random_predict) -> int:
    """How many attempts does it take on average to predict a number in 1000 rounds

    Args:
        random_predict (_type_): prediction function

    Returns:
        int: average number of attempts
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(min_number, max_number + 1, size = observations_num)

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))

    print(f'Your algorithm predicts a number on average in: {score} attempts')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)