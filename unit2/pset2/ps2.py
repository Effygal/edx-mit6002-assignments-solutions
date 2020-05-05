# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.7:
from ps2_verify_movement37 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width, self.height = width, height
        self.cleanedTiles = []
        
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        tile_x = int(pos.getX())
        tile_y = int(pos.getY())
        if (tile_x, tile_y) not in self.cleanedTiles:
            self.cleanedTiles.append((tile_x, tile_y))

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return (m, n) in self.cleanedTiles
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return int(self.width * self.height)

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.cleanedTiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.uniform(0, self.width)
        y = random.uniform(0, self.height)
        return Position(x, y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return 0 <= pos.getX() < self.width and 0 <= pos.getY() < self.height
#test
#random.seed(0)
room1 = RectangularRoom(5, 5) 
#position1 = room1.getRandomPosition()  
#print(position1)  
#room1.cleanTileAtPosition(position1)
#print(room1.cleanedTiles)
#print(room1.getNumCleanedTiles())
#print(room1.isPositionInRoom(Position(0.00, 0.00)))
# === Problem 2

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.pos = self.room.getRandomPosition()
        self.dir = 360*random.random()
        self.room.cleanTileAtPosition(self.pos)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.pos
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.dir

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.pos = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.dir = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!
#test
#robot1 = Robot(room1, 1.25)
#print(robot1.pos)
#print(robot1.dir)
# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        while True:
            self.pos = self.pos.getNewPosition(self.dir, self.speed)
            if self.room.isPositionInRoom(self.pos):
                self.room.cleanTileAtPosition(self.pos)
                break
            else:
                self.dir = 360*random.random()
                
                

                    
#test
#robot2 = StandardRobot(room1, 1.0)
#print(robot2.pos)
#robot2.updatePositionAndClean()
#print(robot2.pos)
                

# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    count_lst = [] 
    for trial in range(num_trials):
        anim = ps2_visualize.RobotVisualization(num_robots, width, height)
        room = RectangularRoom(width, height)
        total_coverage = room.getNumTiles()
        required_coverage = int(min_coverage * total_coverage)
        robots = []
        for i in range(num_robots):
            robot = robot_type(room, speed)
            robots.append(robot)
        count = 0
        while (room.getNumCleanedTiles()/room.getNumTiles()) < min_coverage:
            count += 1
            for robot in robots:
                anim.update(room, robots)
                robot.updatePositionAndClean()
        count_lst.append(count)
        anim.done()
        return sum(count_lst) / len(count_lst)
    
                    
                
        

# Uncomment this line to see how much your simulation takes on average



# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        next_pos = self.pos.getNewPosition(360*random.random(), self.speed)
        if not self.room.isPositionInRoom(next_pos):
            self.setRobotDirection(360*random.random())
        else:
            self.setRobotPosition(next_pos)
            self.setRobotDirection(360*random.random())
            self.room.cleanTileAtPosition(self.pos)
            
                
#print(runSimulation(1, 1.0, 10, 10, 0.75, 30, RandomWalkRobot))

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 6
# NOTE: If you are running the simulation, you will have to close it 
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)


#Problem 6: Data Plotting

#Now, you'll use your simulation to answer some questions about the robots' performance.
#
#In order to do this problem, you will be using a Python tool called PyLab. 
#
#Below is an example of a plot. This plot does not use the same axes that your plots will use; it merely serves as an example of the types of images that the PyLab package produces.

#Note to those who did the optional visualization: For problem 6, we make calls to runSimulation() to get simulation data and plot it. However, you don't want the visualization getting in the way. If you chose to do the visualization exercise, before you get started on problem 6 (and before you submit your code in submission boxes), make sure to comment the visualization code out of runSimulation(). There should be 3 lines to comment out. If you do not comment these lines, your code will take a REALLY long time to run!!
#
#For the questions below, call the given function with the proper arguments to generate a plot using PyLab.
#
#Problem 6-1
#3/3 points (graded)
#Examine showPlot1 in ps2.py, which takes in the parameters title, x_label, and y_label. Your job is to examine the code and figure out what the plot produced by the function tells you. Try calling showPlot1 with appropriate arguments to produce a few plots. Then, answer the following 3 questions.
#
#Which of the following would be the best title for the graph?
#
#Time It Takes 1 - 10 Robots To Clean 80% Of A Room

#correct
#Which of the following would be the best x-axis label for the graph?
#

#Number of Robots

#correct
#Which of the following would be the best y-axis label for the graph?

#Time-steps

#correct
    
#You have used 1 of 2 attemptsSome problems have options such as save, reset, hints, or show answer. These options follow the Submit button.
#
#Problem 6-2
#3/3 points (graded)
#Examine showPlot2 in ps2.py, which takes in the parameters title, x_label, and y_label. Your job is to examine the code and figure out what the plot produced by the function tells you. Try calling showPlot2 with appropriate arguments to produce a few plots. Then, answer the following 3 questions.
#
#Which of the following would be the best title for the graph?
#
#Time It Takes Two Robots To Clean 80% Of Variously Shaped Rooms

#correct
#Examine showPlot2 in ps2.py, which takes in the same parameters as showPlot1. Your job is to examine the code and figure out what the plot produced by the function tells you. Try calling showPlot2 with appropriate arguments to produce a few plots. Then, answer the following 3 questions.
#
#Which of the following would be the best x-axis label for the graph?
#
#Aspect Ratio

#correct
    
#Which of the following would be the best y-axis label for the graph?
#
#Time-steps

#correct
