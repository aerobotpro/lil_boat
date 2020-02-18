from time import sleep
def main():
    while True:     
        cmd = input(strings.hlp)
        try: open("null", "w+").write(cmd)
        except: pass    
        sleep(3)
class strings:
    hlp = """
-----------------------------------------
[] [Bot Controller]
[]
[] [Shell] - "run {command}"
[]
[] [Utils] - "stat"
-----------------------------------------
"""
main()   
