from Algorithm import Algorithm
from Configuration import Configuration
from Schedule import Schedule
import csv
import os

def run():
    prototype = Schedule(3, 3, 75, 5)
    instance = Algorithm(100, 10, 10, prototype)
    config = Configuration()
    config.readcsv()
    instance.Start()
    bestChromosome = instance.GetBestChromosome()
    classes = bestChromosome.GetClasses()
    number_of_rooms = config.GetNumberOfRooms()
    number_of_groups = config.GetNumberOfStudentGroups()

    # Number of Studying day in a week
    DAYS_NUM = 5

    # Number of hours in a day
    DAY_HOURS = 8
    outputs = []
    id = 0
    for it in classes.keys():
        c = it
        p = int(classes[it])

        time = p % (number_of_rooms * DAY_HOURS)
        date = p // (number_of_rooms * DAY_HOURS) + 1
        r = time // DAY_HOURS
        time = time % DAY_HOURS + 1
        #for k in range(0, number_of_groups):
            #for l in c.GetGroups():
                #if l == config.GetStudentsGroupById(str(k + 1)):
        start = '2024-05-' + str(20+date) + ' '+ str(9+time)+':00:00'
        end = '2024-05-' + str(20+date) + ' '+ str(9+time+1)+':00:00'
        data = [id, c.GetCourse().GetName(), c.GetCourse().GetCredits(), c.GetProfessor().GetName(), config.GetRoomById(r).GetName(), start, end]
        id += 1
        outputs.append(data)

        # Get file path
        cwd = os.getcwd()
        path = os.path.join(cwd, 'database\output.csv')

        # Write output to output.csv file
        header = ['id','course','credits','professor','room','start','end']
        with open(path, 'w', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(header)
            csvwriter.writerows(outputs)

run()