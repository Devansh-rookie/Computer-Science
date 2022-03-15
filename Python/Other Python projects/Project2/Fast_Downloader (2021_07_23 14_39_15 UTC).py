from pySmartDL import SmartDL

url = input("What to download?")
dest = "D:\\Down_from_python"

obj = SmartDL(url, dest)
obj.start()

path = obj.get_dest()
