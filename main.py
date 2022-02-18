import sys
from solution import solution_for_days

if __name__ == "__main__":
    try:
        days = int(sys.argv[1])
    except IndexError:
        print("Provide value for number of days as argument in command line")
    except ValueError:
        print("The value for number of days should be of int type")
    except Exception as e:
        print(e)
    else:
        solution = solution_for_days(days)
        print(solution)
