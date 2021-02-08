import pandas as pd
from pathlib import Path
import pyomo.environ as pyomo

fileName = 'dailyindexes.xlsx'
filePath = Path(__file__).resolve().parent / fileName

daysData = pd.read_excel(filePath)
weekendsIndexes = [1, 7]
firstDayOfJune = pd.to_datetime('20210601', format='%Y%m%d')
weekendsAndHolidays = daysData[daysData["WeekDay"].isin(weekendsIndexes) | daysData["Holiday"] == 1]
weekendsAndHolidaysThatOnlyR1Works = weekendsAndHolidays[weekendsAndHolidays["Day"] >= firstDayOfJune]

model = pyomo.ConcreteModel()

model.R1 = pyomo.RangeSet(1, 16)
model.R2 = pyomo.RangeSet(17, 28)
model.R3 = pyomo.RangeSet(29, 42)
model.R2andR3 = model.R2 | model.R3
model.R1andR3 = model.R1 | model.R3

model.R1Dot1 = pyomo.RangeSet(1,1)
model.R1Dot2 = pyomo.RangeSet(2,2)
model.R1Dot3 = pyomo.RangeSet(3,3)
model.R1Dot4 = pyomo.RangeSet(4,4)
model.R1Dot5 = pyomo.RangeSet(5,5)
model.R1Dot6 = pyomo.RangeSet(6,6)
model.R1Dot7 = pyomo.RangeSet(7,7)
model.R1Dot8 = pyomo.RangeSet(8,8)
model.R1Dot9 = pyomo.RangeSet(9,9)
model.R1Dot10 = pyomo.RangeSet(10,10)
model.R1Dot11 = pyomo.RangeSet(11,11)
model.R1Dot12 = pyomo.RangeSet(12,12)
model.R1Dot13 = pyomo.RangeSet(13,13)
model.R1Dot14 = pyomo.RangeSet(14,14)
model.R1Dot15 = pyomo.RangeSet(15,15)
model.R1Dot16 = pyomo.RangeSet(16,16)
model.R2Dot1 = pyomo.RangeSet(17,17)
model.R2Dot2 = pyomo.RangeSet(18,18)
model.R2Dot3 = pyomo.RangeSet(19,19)
model.R2Dot4 = pyomo.RangeSet(20,20)
model.R2Dot5 = pyomo.RangeSet(21,21)
model.R2Dot6 = pyomo.RangeSet(22,22)
model.R2Dot7 = pyomo.RangeSet(23,23)
model.R2Dot8 = pyomo.RangeSet(24,24)
model.R2Dot9 = pyomo.RangeSet(25,25)
model.R2Dot10 = pyomo.RangeSet(26,26)
model.R2Dot11 = pyomo.RangeSet(27,27)
model.R2Dot12 = pyomo.RangeSet(28,28)

model.firstWeek = pyomo.RangeSet(1, 7)
model.rangeOfDaysWhereR1CannotBeAlone = pyomo.RangeSet(8, 92)

model.lastDayOfYear = pyomo.RangeSet(365, 365)

model.weekendsAndHolidays = pyomo.Set(initialize=weekendsAndHolidays.index, within=pyomo.PositiveIntegers)
model.weekendsAndHolidaysAfterMay = pyomo.Set(initialize=weekendsAndHolidaysThatOnlyR1Works.index, within=pyomo.PositiveIntegers)

model.march = pyomo.RangeSet(1, 31)
model.april = pyomo.RangeSet(32, 61)
model.may = pyomo.RangeSet(62, 92)
model.june = pyomo.RangeSet(93, 122)
model.july = pyomo.RangeSet(123, 153)
model.august = pyomo.RangeSet(154, 184)
model.september = pyomo.RangeSet(185, 214)
model.october = pyomo.RangeSet(215, 245)
model.november = pyomo.RangeSet(246, 275)
model.december = pyomo.RangeSet(276, 306)
model.january = pyomo.RangeSet(307, 337)
model.february = pyomo.RangeSet(338, 365)

model.first15DaysOfMay = pyomo.RangeSet(62, 76)
model.last15DaysOfMay = pyomo.RangeSet(78, 92)
model.last15DaysOfJune = pyomo.RangeSet(108, 122)
model.first15DaysOfJuly = pyomo.RangeSet(123, 137)
model.last15DaysOfJuly = pyomo.RangeSet(139, 153)
model.first15DaysOfAugust = pyomo.RangeSet(154, 168)
model.last15DaysOfAugust = pyomo.RangeSet(170, 184)
model.last15DaysOfSeptember = pyomo.RangeSet(200, 214)
model.first15DaysOfOctober = pyomo.RangeSet(215, 229)
model.last15DaysOfOctober = pyomo.RangeSet(231, 245)
model.last15DaysOfNovember = pyomo.RangeSet(261, 275)
model.first15DaysOfDecember = pyomo.RangeSet(276, 290)
model.last15DaysOfDecember = pyomo.RangeSet(292, 306)
model.first15DaysOfJanuary = pyomo.RangeSet(307, 321)
model.last15DaysOfJanuary = pyomo.RangeSet(323, 337)
model.first15DaysOfFebruary = pyomo.RangeSet(338, 352)

model.R1Dot1NotOnCallDateRange = model.april | model.may | model.october
model.R1Dot2NotOnCallDateRange = model.may | model.june | model.november
model.R1Dot3NotOnCallDateRange = model.june | model.july | model.february
model.R1Dot4NotOnCallDateRange = model.july | model.august | model.september
model.R1Dot5NotOnCallDateRange = model.march | model.april | model.september
model.R1Dot6NotOnCallDateRange = model.july | model.september | model.october
model.R1Dot7NotOnCallDateRange = model.august | model.october | model.november
model.R1Dot8NotOnCallDateRange = model.september | model.november | model.december
model.R1Dot9NotOnCallDateRange = model.october | model.december | model.january
model.R1Dot10NotOnCallDateRange = model.november | model.january | model.february
model.R1Dot11NotOnCallDateRange = model.march | model.november | model.february
model.R1Dot12NotOnCallDateRange = model.june | model.august | model.september
model.R1Dot13NotOnCallDateRange = model.march | model.may | model.june | model.august | model.january
model.R1Dot14NotOnCallDateRange = model.april | model.may | model.july | model.september | model.december
model.R1Dot15NotOnCallDateRange = model.april | model.july | model.august | model.december | model.january
model.R1Dot16NotOnCallDateRange = model.march | model.july | model.august | model.september | model.october
model.R2Dot1NotOnCallDateRange = model.march | model.may | model.october | model.december | model.first15DaysOfJuly | model.first15DaysOfJanuary
model.R2Dot2NotOnCallDateRange = model.march | model.august | model.november | model.january | model.last15DaysOfMay | model.first15DaysOfFebruary
model.R2Dot3NotOnCallDateRange = model.april | model.may | model.december | model.january | model.last15DaysOfOctober | model.last15DaysOfNovember
model.R2Dot4NotOnCallDateRange = model.august | model.september | model.january | model.february | model.first15DaysOfMay | model.first15DaysOfOctober
model.R2Dot5NotOnCallDateRange = model.april | model.june | model.august | model.september | model.january | model.last15DaysOfJuly | model.first15DaysOfDecember
model.R2Dot6NotOnCallDateRange = model.march | model.april | model.june | model.november | model.last15DaysOfJuly | model.last15DaysOfOctober
model.R2Dot7NotOnCallDateRange = model.june | model.july | model.november | model.february | model.last15DaysOfAugust | model.first15DaysOfOctober
model.R2Dot8NotOnCallDateRange = model.june | model.july | model.september | model.december | model.february | model.last15DaysOfMay | model.last15DaysOfNovember
model.R2Dot9NotOnCallDateRange = model.may | model. july | model.september | model.october | model.last15DaysOfAugust | model.last15DaysOfDecember
model.R2Dot10NotOnCallDateRange = model.april | model.july | model.october | model.december | model.first15DaysOfAugust | model.last15DaysOfJanuary
model.R2Dot11NotOnCallDateRange = model.march | model.june | model.august | model.october | model.november | model.first15DaysOfMay | model.last15DaysOfSeptember
model.R2Dot12NotOnCallDateRange = model.may | model.july | model.january | model.february | model.last15DaysOfJune | model.last15DaysOfDecember


model.i = model.R1 | model.R2 | model.R3
model.j = pyomo.RangeSet(1, 365)
model.jMinusLastDayOfYear = model.j - model.lastDayOfYear
model.dailyShifts = pyomo.RangeSet(1,1)
model.nightlyShifts = pyomo.RangeSet(2,2)
model.k = model.dailyShifts | model.nightlyShifts
model.Y = pyomo.Var(model.i, model.j, model.k, within=pyomo.Binary)