import click
import helper.scapy as scapy
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
    Find Devices
    '''
    body = scapy.new()
    host = "http://localhost:8700"
    path = "/webhook/devices"
    api = "%s%s"%(host,path)

    result = req.Post({}, api, {"data": body})
    if result is None or result.status_code != 201:
        click.echo(f'Webhook find devices is false!')
        exit(404)
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


pythoncli.add_command(findDevices)
pythoncli.add_command(liveStreaming)
   