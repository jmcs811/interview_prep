import random 
import datetime
def generate_date():
    start_date = datetime.date(2005, 10, 1)
    end_date = datetime.date(2005, 10, 30)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)

    return str(start_date + datetime.timedelta(days=random_number_of_days))

def generate_rater():
    return random.choice(['A', 'B', 'C', 'D', 'E'])

def generate_answer3():
    return random.choice(['Low', 'Average', 'High'])

def generate_answer5():
    return random.choice(['Bad', 'Okay', 'Intermediate', 'Great', 'Exceptional'])

def generate_agreement():
    return random.choice([True, False])

def generate_dataset():
    '''
    date, rater, correct(3), correct(5), answer(3), answer(5), taskID, agreement(3), agreement(5)
    '''
    data_set = []
    for i in range(10000):
        date = generate_date()
        rater = generate_rater()
        correct3 = generate_answer3()
        correct5 = generate_answer5()
        rater3 = generate_answer3()
        rater5 = generate_answer5()
        TaskId = i
        agreement3 = generate_agreement()
        agreement5 = generate_agreement()
        row = [date, rater, correct3, correct5, rater3, rater5, TaksId, agreement3, agreement5]
        data_set.append(row)

    return data_set



dataset = generate_dataset()

def highestAgreementRate(dataset):
    # returns the rater with the highest agreement rate

def lowestAgreementRate(dataset):
    # returns the rater with the lowest agreement rate

def mostCompleteTaskIds(dataset):
    # returns rater with most completed tasks

def leastCompleteTaskIds(dataset):
    # returns rater with least completed tasks

def precisionOf5labels(dataset):
    # returns precision for each of the 5 labels

def precisionOf3Labels(dataset):
    # returns precision for each of the 5 labels

def overallAgreementRate(dataset):
    # returns overall agreement rate


