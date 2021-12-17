import click
import subprocess
import helper.scapy as scapy
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
    network = subprocess.call(["hostname","-I"])
    cidr= "/24" # /24	255.255.255.0	254
    ip= "%s%s" %(network, cidr)
    scanned_output = scapy.scan(ip)
    # scapy.display_result(scanned_output)

    result = req.Post({}, 'http://13.229.69.223:8700/webhook/devices', {"data": scanned_output})
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
   