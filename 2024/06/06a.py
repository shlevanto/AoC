import numpy as np


class Direction():
    # the default direction is up
    def __init__(self):
        self.direction = (-1,0)


    def turn_right(self):
        match self.direction:
            case (-1,0):
                self.direction = (0,1)
            case (0,1):
                self.direction = (1,0)
            case (1,0):
                self.direction = (0,-1)
            case (0,-1):
                self.direction = (-1,0)


class Crawler:  

    def __init__(self, arr):
        self.arr = arr
        self.direction = Direction()
        self.route = np.zeros_like(self.arr, dtype=bool)
        self.location = self.find_start(self.arr)
        self.boundaries = self.arr.shape


    def find_start(self, arr):
        for x in range(arr.shape[0]):
            for y in range(arr.shape[1]):
                if arr[x,y] == "^":
                    return (x,y)
        return None


    def step(self):
        new_location = (self.location[0] + self.direction.direction[0], 
            self.location[1] + self.direction.direction[1])
        return new_location


    def out_of_bounds(self, location):
        negative = -1 in location
        rows = location[0] >= self.boundaries[0]
        columns = location[1] >= self.boundaries[1]

        return negative or rows or columns


    def crawl(self):
        while True:
            new_location = self.step()

            if self.out_of_bounds(new_location):
                self.route[self.location] = True
                print(f"The route is: {np.sum(self.route, axis = (0,1))}")
                return
            elif self.arr[new_location] == "#":
                self.route[self.location] = True
                self.direction.turn_right()
            else:
                self.route[self.location] = True
                self.location = new_location
                continue


def main():
    file_name = "06.input"

    with open(file_name, "r", encoding="utf-8") as f:
        rows = f.readlines()

    # read the input into a nump array of characters
    chars = [list(row.strip()) for row in rows]
    arr = np.stack(chars)

    crawler = Crawler(arr)
    crawler.crawl()


if __name__ == "__main__":
    main()
