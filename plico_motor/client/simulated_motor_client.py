from plico_motor.client.abstract_motor_client import AbstractMotorClient, \
    SnapshotEntry
from plico.utils.decorator import override, returns
from plico.utils.snapshotable import Snapshotable
from plico_motor.types.motor_status import MotorStatus


class SimulatedMotorClient(AbstractMotorClient):

    def __init__(self):
        self._name = 'mySimulatedMotor'
        self._position = 0
        self._was_homed = False

    @override
    def position(self):
        return self._position

    @override
    def move_to(self, position_in_steps):
        self._position = position_in_steps

    @override
    def move_by(self, position_in_steps):
        self._position += position_in_steps

    @override
    def home(self):
        self._position = 0
        self._was_homed = True

    @override
    def snapshot(self, prefix):
        snapshot = {}
        snapshot[SnapshotEntry.MOTOR_NAME] = self._name
        snapshot[SnapshotEntry.POSITION] = self.position()
        return Snapshotable.prepend(prefix, snapshot)

    @override
    @returns(MotorStatus)
    def status(self):
        status = MotorStatus(self._name,
                             self._was_been_homed)
        return status

