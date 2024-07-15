
from plico_motor.client.client_map import client_map
from plico_motor.client.motor_client import MotorClient
from plico_motor.utils.constants import Constants
from plico.client.discovery import plico_list, plico_get, plico_client


def _getDefaultConfigFilePath():
    from plico.utils.config_file_manager import ConfigFileManager
    cfgFileMgr= ConfigFileManager(Constants.APP_NAME,
                                  Constants.APP_AUTHOR,
                                  Constants.THIS_PACKAGE)
    return cfgFileMgr.getConfigFilePath()


defaultConfigFilePath= _getDefaultConfigFilePath()


def motor(hostname, port):
    '''Generic DeformableMirrorClient, kept for backward compatibility'''
    return plico_client(MotorClient, hostname, port)


def list_motors(timeout_in_seconds=2):
    return plico_list(server_type='plico_motor', timeout_in_seconds=timeout_in_seconds)


def get(motor_name, axis, timeout_in_seconds=2):
    return plico_get(server_type='plico_motor', name=motor_name, default_class=MotorClient,
                     timeout_in_seconds=timeout_in_seconds, client_map=client_map, axis=axis)
