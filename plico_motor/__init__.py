from plico_motor.utils.constants import Constants


def _getDefaultConfigFilePath():
    from plico.utils.config_file_manager import ConfigFileManager
    cfgFileMgr = ConfigFileManager(Constants.APP_NAME,
                                   Constants.APP_AUTHOR,
                                   Constants.THIS_PACKAGE)
    return cfgFileMgr.getConfigFilePath()


defaultConfigFilePath = _getDefaultConfigFilePath()


def motor(hostname, port, axis):

    from plico_motor.client.motor_client import MotorClient
    from plico.rpc.zmq_remote_procedure_call import ZmqRemoteProcedureCall
    from plico.rpc.zmq_ports import ZmqPorts
    from plico.rpc.sockets import Sockets

    rpc = ZmqRemoteProcedureCall()
    zmqPorts = ZmqPorts(hostname, port)
    sockets = Sockets(zmqPorts, rpc)
    return MotorClient(rpc, sockets, axis)


def list_motors(timeout_in_seconds=2):
    from plico.utils.discovery_server import DiscoveryClient
    return DiscoveryClient().run(timeout_in_seconds=timeout_in_seconds)

def find(motor_name, axis, timeout_in_seconds=2):
    from plico.utils.discovery_server import DiscoveryClient
    server_info = DiscoveryClient().run(motor_name, timeout_in_seconds)
    return motor(server_info.host, server_info.port, axis)