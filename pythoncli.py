import click
import helper.scapy as scapy
import helper.nmap as nmap
import helper.request as req
import helper.streaming as streaming


@click.group()
def pythoncli():
    '''
    Commands to manage your assets
    '''
    pass

@click.command(name='fd')
def findDevices():
    '''
    Find Devices used lib scapy
    '''
    body = scapy.new()
    host = "http://13.229.69.223:8700"
    path = "/webhook/devices"
    api = "%s%s"%(host,path)

    result = req.Post({}, api, {"data": body})
    if result is None or result.status_code != 201:
        click.echo(f'Webhook find devices is false!')
        exit(404)
    click.echo(f'Done')

@click.command(name='fd2')
def findDevices2():
    '''
    Find Devices2 nmap
    '''
    body = nmap.new()
    click.echo(f'Done')

@click.command(name='ls')
@click.option('--type', required=True, default="ffmpeg", show_default=True)
@click.option('--rtsp', required=True)
@click.option('--rtmp', required=True)
def liveStreaming(type, rtsp, rtmp):
    '''
    livestreaming
    '''
    streaming.new(type, rtsp, rtmp)

@click.command(name='ping')
def ping():
    '''
    Ping
    '''
    click.echo(f'Ping Pong Pong')

pythoncli.add_command(findDevices)
pythoncli.add_command(findDevices2)
pythoncli.add_command(liveStreaming)
pythoncli.add_command(ping)
   