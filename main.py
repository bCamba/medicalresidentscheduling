from model import model
import pickle
import pyomo.environ as pyomo
from constraints import *

model.amountOfR1OnDailyCallsConstraint = pyomo.Constraint(model.R1, model.dailyShifts, rule=amountOfR1OnCalls)
model.amountOfR1OnNightlyCallsConstraint = pyomo.Constraint(model.R1, model.nightlyShifts, rule=amountOfR1OnCalls)
model.amountOfR2OnDailyCallsConstraint = pyomo.Constraint(model.R2, rule=amountOfR2OnDailyCalls)
model.amountOfR2OnNightCallsConstraint = pyomo.Constraint(model.R2, rule=amountOfR2OnNightCalls)
model.amountOfR3OnDailyCallsConstraint = pyomo.Constraint(model.R3, model.dailyShifts, rule=amountOfR3OnCalls)
model.amountOfR3OnNightlyCallsConstraint = pyomo.Constraint(model.R3, model.nightlyShifts, rule=amountOfR3OnCalls)
model.amountOfResidentsPerShiftConstraint = pyomo.Constraint(model.j, model.k, rule=amountOfResidentsPerShift)
model.residentOnDailyShiftsCannotBeOnNightShiftsOfTheSameDayConstraint = pyomo.Constraint(model.i, model.j, rule=residentOnDailyShiftsCannotBeOnNightShiftsOfTheSameDay)
model.residentOnDailyShiftsCannotBeOnDailyShiftsOfTheNextDayConstraint = pyomo.Constraint(model.i, model.jMinusLastDayOfYear, rule=residentOnDailyShiftsCannotBeOnDailyShiftsOfTheNextDay)
model.residentOnNightShiftsCannotBeOnDailyShiftsOfTheNextDayConstraint = pyomo.Constraint(model.i, model.jMinusLastDayOfYear, rule=residentOnNightShiftsCannotBeOnDailyShiftsOfTheNextDay)
model.residentOnNightShiftsCannotBeOnNightShiftsOfTheNextDayConstraint = pyomo.Constraint(model.i, model.jMinusLastDayOfYear, rule=residentOnNightShiftsCannotBeOnNightShiftsOfTheNextDay)
model.untilMayR1mustNotBeAloneConstraint = pyomo.Constraint(model.rangeOfDaysWhereR1CannotBeAlone, model.k, rule=untilMayR1mustNotBeAlone)
model.onlyR2areAllowedOnTheFirstWeekConstraint = pyomo.Constraint(model.R1andR3, model.firstWeek, model.k, rule=residentMustNotBeOnCall)
model.R2AndR3MustNotWorkOnWeekendsAndHolidaysAfterMayConstraint = pyomo.Constraint(model.R2andR3, model.weekendsAndHolidaysAfterMay , model.k, rule=residentMustNotBeOnCall)

model.R1Dot1mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot1, model.R1Dot1NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot2mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot2, model.R1Dot2NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot3mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot3, model.R1Dot3NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot4mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot4, model.R1Dot4NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot5mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot5, model.R1Dot5NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot6mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot6, model.R1Dot6NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot7mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot7, model.R1Dot7NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot8mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot8, model.R1Dot8NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot9mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot9, model.R1Dot9NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot10mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot10, model.R1Dot10NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot11mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot11, model.R1Dot11NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot12mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot12, model.R1Dot12NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot13mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot13, model.R1Dot13NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot14mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot14, model.R1Dot14NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot15mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot15, model.R1Dot15NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R1Dot16mustNotBeOnCallConstraint = pyomo.Constraint(model.R1Dot16, model.R1Dot16NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R2Dot1mustNotBeOnCallConstraint = pyomo.Constraint(model.R2Dot1, model.R2Dot1NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R2Dot2mustNotBeOnCallConstraint = pyomo.Constraint(model.R2Dot2, model.R2Dot2NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R2Dot3mustNotBeOnCallConstraint = pyomo.Constraint(model.R2Dot3, model.R2Dot3NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R2Dot4mustNotBeOnCallConstraint = pyomo.Constraint(model.R2Dot4, model.R2Dot4NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R2Dot5mustNotBeOnCallConstraint = pyomo.Constraint(model.R2Dot5, model.R2Dot5NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R2Dot6mustNotBeOnCallConstraint = pyomo.Constraint(model.R2Dot6, model.R2Dot6NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R2Dot7mustNotBeOnCallConstraint = pyomo.Constraint(model.R2Dot7, model.R2Dot7NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R2Dot8mustNotBeOnCallConstraint = pyomo.Constraint(model.R2Dot8, model.R2Dot8NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R2Dot9mustNotBeOnCallConstraint = pyomo.Constraint(model.R2Dot9, model.R2Dot1NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R2Dot10mustNotBeOnCallConstraint = pyomo.Constraint(model.R2Dot10, model.R2Dot10NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R2Dot11mustNotBeOnCallConstraint = pyomo.Constraint(model.R2Dot11, model.R2Dot11NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)
model.R2Dot12mustNotBeOnCallConstraint = pyomo.Constraint(model.R2Dot12, model.R2Dot12NotOnCallDateRange, model.k, rule=residentMustNotBeOnCall)

model.OBJ = pyomo.Objective(rule=varianceOfWeekendsAndHolidaysWorked)

model.OBJ.pprint()
opt = pyomo.SolverFactory('ipopt')
opt.options['print_level'] = 12
opt.options['output_file'] = "./testlog.txt"
results = opt.solve(model, tee=True)
results.write(filename='results.json', format='json')

modelSolutionFileHandler = open('model.txt', 'w')
pickle.dump(model.solutions, modelSolutionFileHandler)


