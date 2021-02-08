def amountOfR1OnCalls(model, i, k):
    return sum(model.Y[i, j, k] for j in model.j) == 26

def amountOfR2OnDailyCalls(model, i):
    return sum(model.Y[i, j, 1] for j in model.j) == 15

def amountOfR2OnNightCalls(model, i):
    return sum(model.Y[i, j, 2] for j in model.j) == 14

def amountOfR3OnCalls(model, i, k):
    return sum(model.Y[i, j, k] for j in model.j) == 10

def amountOfResidentsPerShift(model, j, k):
    return sum(model.Y[i, j, k] for i in model.i) == 2

def residentOnDailyShiftsCannotBeOnNightShiftsOfTheSameDay(model, i, j):
    return model.Y[i, j, 1] + model.Y[i, j, 2] <= 1

def residentOnDailyShiftsCannotBeOnDailyShiftsOfTheNextDay(model, i, j):
    return model.Y[i, j, 1] + model.Y[i, j+1, 1] <= 1

def residentOnNightShiftsCannotBeOnDailyShiftsOfTheNextDay(model, i, j):
    return model.Y[i, j, 2] + model.Y[i, j+1, 1] <= 1

def residentOnNightShiftsCannotBeOnNightShiftsOfTheNextDay(model, i, j):
    return model.Y[i, j, 2] + model.Y[i, j+1, 2] <= 1

def untilMayR1mustNotBeAlone(model, j, k):
    return sum(model.Y[i, j, k] for i in model.R1) <= 1

def residentMustNotBeOnCall(model, residents, timeBox, shift):
    return model.Y[residents, timeBox, shift] == 0

def varianceOfWeekendsAndHolidaysWorked(model):
    average = sum(model.Y[i, j, k] for i in model.i for j in model.weekendsAndHolidays for k in model.k)/42.0
    total = 0
    for i in model.i:
        total += (sum(model.Y[i, j, k] for j in model.weekendsAndHolidays for k in model.k) - average)**2
    return total/42.0
