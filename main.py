import os


class Reader:

    def readprojects(self, folder_name):
        result = []
        lines = self.readlines(folder_name)
        for i in lines:
            splited = i.split('\n')
            result.append(f"insert into DbProjects values (null, 1265, '{splited[0]}', null)\n")

        with open(os.curdir + "/result.txt", 'a') as file:
            file.writelines(result)

    def readlines(self, foleder_name):
        f = open(os.curdir + "/" + foleder_name, 'r')
        return f.readlines()

def __main__():
    reader = Reader()
    reader.readprojects("Projects.txt")

__main__()