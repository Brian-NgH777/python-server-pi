import click
# import subprocess
import helper.scapy as scapyHelper
import helper.request as req


@click.group()
def pythoncli():
    '''
    Commands to manage your assets
    '''
    pass

@click.command(name='finddevices')
def findDevices():
    '''
    Find Devices
    '''
    body = scapyHelper.new()
    print("bodybodybody", body)
    result = req.Post({}, 'http://13.229.69.223:8700/webhook/devices', {"data": body})
    if result is None or result.status_code != 201:
        click.echo(f'Webhook find devices is false!')
        exit(404)
    click.echo(f'Done')


@click.command(name='livestreaming')
@click.argument('url')
def liveStreaming(url):
    '''
    livestreaming
    '''
    print(url)
    click.echo(f'Done')


pythoncli.add_command(findDevices)
pythoncli.add_command(liveStreaming)
   