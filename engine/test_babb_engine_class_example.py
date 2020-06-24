import babb_engine_class_example
import pytest


class TestEngineClass:

    def setup_class(self):
        self.engine = babb_engine_class_example.Engine('Doge 351ci V8', 3000)

    def test_turn_on(self):
        self.engine.turn_on()
        assert self.engine.get_state() == 'ON', "Engine state is not ON"

    def test_turn_off(self):
        self.engine.turn_off()
        assert self.engine.get_state() == 'OFF', "Engine state is not OFF"

    def test_rpm_positive(self):
        self.engine.turn_on()
        self.engine.set_rpm(2000)
        assert self.engine.get_rpm() == 2000, "Engine rpm not correct"

    def test_rpm_over_max(self):
        self.engine.turn_on()
        over_max = self.engine.get_max_rpm() + 100.0
        self.engine.set_rpm(over_max)
        assert self.engine.get_state() == 'BLOWN', "Engine state is not BLOWN"
        assert self.engine.get_rpm() == 0, "Engine rpm not 0"

    def test_cant_start_blown_engine(self):
        self.engine.set_state('ON')
        over_max = self.engine.get_max_rpm() + 100.0
        self.engine.set_rpm(over_max)
        assert self.engine.get_state() == 'BLOWN', "Engine state is not BLOWN"
        assert self.engine.get_rpm() == 0, "Engine rpm not 0"
        self.engine.turn_on()
        assert self.engine.get_state() == 'BLOWN', "Engine state should be BLOWN"

