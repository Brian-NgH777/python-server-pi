import os
import click
import helper.scapy as scapy
# import helper.nmap as nmap
import helper.request as req
import helper.snapshot as snapshot
import helper.streaming as streaming
from pathlib import Path

mypath = Path().absolute()
listLocalDevices = []
host = "http://13.229.69.223:8700"

@click.group()
def pythoncli():
    '''
    Commands to manage your assets
    '''
    pass

@click.command(name='fd') # Find device 
def findDevices():
    '''
    Find Devices
    '''
    # find ip mac vencher in local used lib scapy 
    body = scapy.new()
    # Add data scan devices to global listLocalDevices
    global listLocalDevices
    listLocalDevices = body
    # Webhook go server update list devices
    path = "/webhook/devices"
    api = "%s%s"%(host,path)
    result = req.Post({}, api, {"data": body})
    if result is None or result.status_code != 201:
        click.echo(f'Webhook find devices is false!')
        exit(404)
    click.echo(f'Done')

@click.command(name='ls')
@click.option('--rtsp', required=True)
@click.option('--rtmp', required=True)
def liveStreaming(rtsp, rtmp):
    '''
    Live streaming ffmpeg
    '''
    # Check ip in listLocalDevices
    # isCheck = checkIp(rtsp)
    # if isCheck == False :
    #     click.echo(f'IP not in list devices!')
    #     exit(404)
    
    # Live streaming thread
    streaming.new(rtsp, rtmp)
    click.echo(f'Done')

@click.command(name='ss')
@click.option('--rtsp', required=True)
@click.option('--namefile', required=True)
def screenshots(rtsp, namefile):
    '''
    Get JPEG snapshot from RTSP-stream (ffmpeg)
    '''
    # Check ip in listLocalDevices
    # isCheck = checkIp(rtsp)
    # if isCheck == False :
    #     click.echo(f'IP not in list devices!')
    #     exit(404)

    # screenshots
    path = str(mypath) + "/snapshots/"+ namefile
    # isSuccess = snapshot.new(rtsp, path)
    # if isSuccess == False :
    #     click.echo(f'snapshot is false!')
    #     exit(404)

    # Webhook go server upload to s3 
    whPath = "/webhook/snapshots"
    api = "%s%s"%(host,whPath)
    result = req.PostFile(api, path)
    if result is None or result.status_code != 200:
        click.echo(f'Webhook Post File is false!')
        exit(404)
    
    # Remove file 
    # if os.path.exists(path):
    #     os.remove(path)
    # else:
    #     click.echo(f'Remove file path: %s is false!'%(path))

    click.echo(f'Done')

@click.command(name='ping')
def ping():
    '''
    Ping
    '''
    click.echo(f'Ping Pong Pong')

def checkIp(rtsp):
    isCheck = False
    arrRTSP = rtsp.split("@", 1)
    ip = arrRTSP[1].split(":")
    for d in listLocalDevices:
        if d.ip == ip:
            isCheck = True
            break
    return isCheck

pythoncli.add_command(findDevices)
pythoncli.add_command(liveStreaming)
pythoncli.add_command(screenshots)
pythoncli.add_command(ping)
   