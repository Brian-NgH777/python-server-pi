import click
import helper.scapy as scapy
# import helper.nmap as nmap
import helper.request as req
import helper.snapshot as snapshot
import helper.streaming as streaming
from pathlib import Path

mypath = Path().absolute()
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
    body = scapy.new()
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
    streaming.new(rtsp, rtmp)

@click.command(name='ss')
@click.option('--rtsp', required=True)
@click.option('--name', required=True)
def screenshots(rtsp, name):
    '''
    Get JPEG snapshot from RTSP-stream (ffmpeg)
    '''
    path = mypath + "/snapshots/"+ name
    isSuccess = snapshot.new(rtsp, path)
    if isSuccess == False :
        click.echo(f'Webhook find devices is false!')
        exit(404)

    # whPath = "/webhook/snapshots"
    # api = "%s%s"%(host,whPath)
    # result = req.PostFile(api, path)
    # if result is None or result.status_code != 201:
    #     click.echo(f'Webhook find devices is false!')
    #     exit(404)
    click.echo(f'Done')

@click.command(name='ping')
def ping():
    '''
    Ping
    '''
    click.echo(f'Ping Pong Pong')

pythoncli.add_command(findDevices)
pythoncli.add_command(liveStreaming)
pythoncli.add_command(screenshots)
pythoncli.add_command(ping)
   