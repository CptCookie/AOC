from .solution import Processor


def test_jnz():
    cpu = Processor(["set a 4", "set b 1", "mul b 2", "sub a 1", "jnz a -2"])
    cpu.execute()
    assert cpu.registers["b"] == 16
